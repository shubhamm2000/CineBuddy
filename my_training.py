import numpy as np
import pandas as pd
import pickle

df = pd.read_csv('D:\ML Videos and ppts\PPTs\CineBuddy\IMDB-Movie-Data.csv')

df = df.loc[:,['Title','Genre','Rating','Votes']]

x = df.iloc[:,2:4].values

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x[:,0:2]=sc.fit_transform(x[:,0:2])


from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
    k_means = KMeans(n_clusters = i,init='k-means++')
    k_means.fit(x[:,0:2])
    wcss.append(k_means.inertia_)


k_means = KMeans(n_clusters = 4,init='k-means++')
k_means.fit(x)
y_kmeans = k_means.predict(x)

#KNN
movie_features = pd.concat([df["Genre"].str.get_dummies(sep=","),df[["Rating"]]],axis=1)

from sklearn.neighbors import NearestNeighbors
knn = NearestNeighbors(n_neighbors=10)
knn.fit(movie_features)
distances, indices = knn.kneighbors(movie_features)

def get_index_from_Title(Title):
    return list(df[df["Title"]==Title].index)[0]
all_movie_names = (df.Title.values)

def Recommendations(query=None):
    found_id = get_index_from_Title(query)
    array=[]
    for i in indices[found_id][1:]:
        array.append(df.loc[i]["Title"])
    return array  

file = open('model.pkl','wb')

    #dump information to that file
pickle.dump(Recommendations, file)
file.close()
        