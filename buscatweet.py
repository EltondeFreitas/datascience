###################################################################
#### Retorna dados do Twitter a partir de uma palavra chave,
#### se conectando por meio da API do mesmo com as credenciais
#### de desenvolvedor, realizando alguns tratamentos de dados e 
#### gravando o resutlado em um arquivo CSV
#### Data: 25/08/2020
#### Autor: Elton
###################################################################

#### Bibliotecas necessárias para executar os comandos da aplicação
import tweepy
import csv
import datetime
import unidecode
import re

#### Credenciais do app fornecidas pelo Twitter, cade desenvolvedor deve ter a sua
consumer_key = 'fvSxxxxxxxxxxxxxxxxxxxFg7'
consumer_secret = 'BglxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxynG'
access_token = '0000000000-AQmxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxbrv'
access_token_secret = 'q5axxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxens'

### Definindo parâmetros para a API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

### Define o termo a ser buscado com ou sem #
busca='SAUDADES NE MINHA FILHA'

### Define o nome do arquivo que vai ser gerado, passando caminho, termo a ser buscado e data como nome do arquivo
csvFile = open("C:/Users/USER/Documents/python/twitter/dados_twitter_"+
                busca+
                "_"+
                (datetime.datetime.now().strftime("%Y-%m-%d-%H"))+
                ".csv", 
                "a")

### Chama a função que vai gravar o arquivo com os parâmetros, definindo como delimitador o ";"
csvWriter = csv.writer(csvFile,delimiter =";")

### Função para remover emojis
emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U0001F1F2-\U0001F1F4"  # Macau flag
        u"\U0001F1E6-\U0001F1FF"  # flags
        u"\U0001F600-\U0001F64F"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U0001F1F2"
        u"\U0001F1F4"
        u"\U0001F620"
        u"\u200d"
        u"\u2640-\u2642"
        "]+", flags=re.UNICODE)

### Faz a busca dos tweets, definindo a palavra, a linguagem e quantos tweets serão retornados
for tweet in tweepy.Cursor(api.search,q=busca,
                           lang='pt',
                           since='2020-08-24').items(5):
    
    ### Remove acentos
    tweet_sem_acento = unidecode.unidecode(tweet.text)
    
    ### Remove links https
    tweet_sem_link = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ", tweet_sem_acento)
    
    ### Chama a função para remover emojis
    tweet_sem_emoji = emoji_pattern.sub(r'', tweet_sem_link)

    ### cria uma nova variável para receber os dados tratados 
    tweet_trat = tweet_sem_emoji

    ### Grava os dados recuperados da busca no Twitter
    csvWriter.writerow([tweet.created_at,
    tweet.user.id,
    tweet.user.name.encode('utf-8'),
    tweet.user.screen_name.encode('utf-8'),
    tweet.text.encode('utf-8'),
    tweet_trat])