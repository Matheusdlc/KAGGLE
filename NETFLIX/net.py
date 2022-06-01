import pandas as pd 
from sklearn.tree import DecisionTreeRegressor
import re

titles = pd.read_csv("titles.csv",sep=',') #leitura arquvo CVS com os dados imporados
credits = pd.read_csv("credits.csv",sep=',') #eitura arquvo CVS com os dados imporados

features_titles = titles.columns.tolist()   #['id'
                                            #'title'
                                            #'type'
                                            #'description'
                                            #'release_year'
                                            #'age_certification'
                                            #'runtime'
                                            #'genres'
                                            #'production_countries'
                                            #'seasons'
                                            #'imdb_id'
                                            #'imdb_score'
                                            #'imdb_votes'
                                            #'tmdb_popularity'
                                            #'tmdb_score']

features_credits = credits.columns.tolist() #['person_id'
                                            #'id'
                                            #'name'
                                            #'character'
                                            #'role']

types = titles.groupby(['type']).count()
#         id  title  description  release_year  ...  imdb_score  imdb_votes  tmdb_popularity  tmdb_score
#type                                           ...
#MOVIE  3759   3758         3751          3759  ...        3407        3391             3698        3573
#SHOW   2047   2047         2037          2047  ...        1876        1876             2014        1915
#
#[2 rows x 14 columns]

age =  titles.groupby(['age_certification']).count()

#                    id  title  type  description  ...  imdb_score  imdb_votes  tmdb_popularity  tmdb_score
#age_certification                                 ...
#o                 131    131   131          131  ...         105         105              123         115
#NC-17               14     14    14           14  ...          13          13               14          14
#PG                 246    246   246          245  ...         238         237              245         244
#PG-13              440    440   440          440  ...         424         418              439         435
#R                  575    575   575          575  ...         548         546              575         574
#TV-14              470    470   470          467  ...         436         436              458         433
#TV-G                76     76    76           76  ...          72          72               76          74
#TV-MA              841    841   841          841  ...         792         792              836         814
#TV-PG              186    186   186          184  ...         172         172              181         167
#TV-Y               105    105   105          102  ...          94          94              101          92
#TV-Y7              112    112   112          110  ...         104         104              111         103
#
#[11 rows x 14 columns]



#--------------------------QUANTIDADE DE FILMES PARA CADA GENERO e QUANTIDADE DE SERIES PARA CADA GENERO::




#Name  - FILMES+SERIES
#                   68
#action           1053
#animation         665
#comedy           2269
#crime             891
#documentation     910
#drama            2901
#european          460
#family            622
#fantasy           631
#history           233
#horror            380
#music             238
#reality           223
#romance           958
#scifi             587
#sport             166
#thriller         1178
#war               149
#western            44
#

titles1 = titles.assign(action=0)
titles1 = titles.assign(animation=0)
titles1 = titles.assign(comedy=0)
titles1 = titles.assign(crime=0)
titles1 = titles.assign(documentation=0)
titles1 = titles.assign(drama=0)
titles1 = titles.assign(european=0)
titles1 = titles.assign(family=0)
titles1 = titles.assign(fantasy=0)
titles1 = titles.assign(history=0)
titles1 = titles.assign(horror=0)
titles1 = titles.assign(music=0)
titles1 = titles.assign(reality=0)
titles1 = titles.assign(romance=0)
titles1 = titles.assign(scifi=0)
titles1 = titles.assign(sport=0)
titles1 = titles.assign(thriller=0)
titles1 = titles.assign(war=0)
titles1 = titles.assign(western=0)
titles1 = titles.assign(no_genre=0)
    
for o in titles1.index:
    u = titles1.loc[o, 'genres']
    l = re.sub(r"""[!?'" .<>(){}@%&*/[/]""", "", u)
    l = re.sub(r"""]""", "", l)
    l = l.split(',')
    for i in l:
        if i =='action':
            titles1.loc[o, 'action'] = 1
        if i =='animation':
            titles1.loc[o, 'animation'] = 1
        if i =='comedy':
            titles1.loc[o, 'comedy'] = 1
        if i =='crime':
            titles1.loc[o, 'crime'] = 1
        if i =='documentation':
            titles1.loc[o, 'documentation'] = 1
        if i =='drama':
            titles1.loc[o, 'drama'] = 1
        if i =='european':
            titles1.loc[o, 'european'] = 1
        if i =='family':
            titles1.loc[o, 'family'] = 1
        if i =='fantasy':
            titles1.loc[o, 'fantasy'] = 1
        if i =='history':
            titles1.loc[o, 'history'] = 1
        if i =='horror':
            titles1.loc[o, 'horror'] = 1
        if i =='music':
            titles1.loc[o, 'music'] = 1
        if i =='reality':
            titles1.loc[o, 'reality'] = 1
        if i =='romance':
            titles1.loc[o, 'romance'] = 1
        if i =='scifi':
            titles1.loc[o, 'scifi'] = 1
        if i =='sport':
            titles1.loc[o, 'sport'] = 1
        if i =='thriller':
            titles1.loc[o, 'thriller'] = 1
        if i =='war':
            titles1.loc[o, 'war'] = 1
        if i =='western':
            titles1.loc[o, 'western'] = 1
        if i =='':
            titles1.loc[o, 'no_genre'] = 1
genr = ['type','action','animation','comedy','crime','documentation','drama','european','family','fantasy','history','horror','music','reality','romance','scifi','sport','thriller','war','western']
filmes_qnty = titles1[genr]
#print(filmes_qnty.groupby(['type']).sum())
#       action  animation  comedy  crime  documentation  drama  ...  romance  scifi  sport  thriller  war  western
#type                                                           ...
#MOVIE     641        271    1543    524            590   1864  ...      694    210    111       830   94       31
#SHOW      412        394     726    367            320   1037  ...      264    377     55       348   55       13




#----------------------NUMERO DE FILMES E NUMERO DE SERIES PARA CADA PAÍS

#h = []
#for g in titles['production_countries']:
#    p = re.sub(r"""[!?'" .<>(){}@%&*/[/]""", "", g)
#    p = re.sub(r"""]""", "", p)
#    p = p.split(',')
#    h = h + p
#df0 =  pd.DataFrame(h, columns = ['Name'])
#df0 = df0.assign(c=1)
#print(df0.groupby(['Name']).sum())

#--------MEDIA DAS NOTAS PARA CADA GENERO VERSUS A QUANTIDADE DE FILMES PARA CADA GENERO
act = ['type','imdb_score','tmdb_score','action']
action = titles1[act]
action = action.fillna(0)
print(action.info())


#--------MEDIA DAS NOTAS PARA CADA PAÍS VERSUS A QUANTIDADE DE FILMES PARA CADA PAÍS
#--------PAISES COM FILMES MAIS POPULARES DE ACORDO COM IMDB
#--------PAÍSES COM SERIE MAIS POPULARES DE ACODO COM IMDB