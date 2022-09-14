import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
data = pd.read_csv("data_fin.csv")
vec = TfidfVectorizer()
vector = vec.fit_transform(data.genre)
indexed = pd.Series(data = data.index, index=data.music)
def sercher(music,n=10):
    loc = indexed[music] 
    dis = linear_kernel(vector[loc],vector)
    val = pd.DataFrame(dis)
    val = val.transpose()
    val.columns = ["name"]
    val = val.sort_values(by = "name", ascending=False)
    name = []
    gen = []
    rate = []
    pop = []
    for i in range(0,n):
        name.append(data.music[val.index[i]])
        gen.append(data.genre[val.index[i]])
        rate.append(data.rating[val.index[i]])
        pop.append(data.Popularity[val.index[i]])
    return name , gen , rate , pop
def checker(music):
    if music in indexed:
        res = 1
    else:
        res = 0
    return res

def lists():
    liss = []
    gen = []
    for i in range (0,len(data)):
        liss.append(data.music[i])
        gen.append(data.genre[i])
    return liss , gen
    