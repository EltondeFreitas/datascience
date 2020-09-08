# Chamada da biblioteca Pandas
import pandas as pd

# Definindo o header do arquivo a ser lido:
header_list = ["created_at",
               "id",
               "name",
               "screen_name",
               "text",
               "favorited",
               "tweet_trat"]

# Deve-se definir o caminho em que se encontra o arquivo CSV
df = pd.read_csv("C:/Users/USER/Documents/python/twitter/dados_twitter_SAUDADES NE MINHA FILHA_2020-09-04-12.csv",
                 sep = ";", names=header_list)

# Tratando os dados de tweet e RT's criando novas colunas 
df["rts"]= df["tweet_trat"].str.find('RT @')
df["rtu"]= df['tweet_trat'].str.split(':').str[0]
df["rtu"]= df['rtu'].str.replace('RT ', '')
df.loc[(df.rts < 0 ),'rtu']=''
df.loc[(df.rts > -1 ),'rts']=1
df.loc[(df.rts < 0 ),'rts']=0

# Verifica quantos tweets foram coletados
print(df['tweet_trat'].count())

# Verifica quantos RT's foram feitos
print(df[df["rts"]==0].count()["rts"])

# Verifica quem foram os 10 mais que tuitaram
print(df.groupby('screen_name')['screen_name'].count().nlargest(10).reset_index(name='TOT_TWEET'))

# Verifica quem foram os 10 mais que retuitaram
print(df.groupby('screen_name')['rts'].sum().nlargest(10).reset_index(name='TOT_RETWEET'))

# Cria-se um novo dataframe filtrando somente os casos igual a 1 no campo rts
df2 = df[df['rts']==1]

# Realiza um count no campo rtu
print(df2.groupby('rtu')['rtu'].count().nlargest(10).reset_index(name='TOT_RETUITADO'))

# Agrupamento de dados por screen_name e rtu realizando uma contagem por rts para os 10 mais
print(df[df["rts"] == 1].groupby(['screen_name','rtu'])['rts'].count().nlargest(10).reset_index(name='TOT_QUEM_RETWEET'))