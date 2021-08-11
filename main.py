from numpy.core.records import array
from my_training import Recommendations
from flask import Flask, render_template, request
import pickle
import requests,json

app = Flask(__name__, static_url_path='')

#open a file where you want to store the data
file = open('model.pkl','rb')
Recommendations = pickle.load(file)
file.close()
api_key = '9fc6b26943971ad4b324fe111981af31'

@app.route('/', methods=["GET","POST"])
def get_movie():
    if request.method =="POST":
        myDict = request.form
        name = str(myDict['name'])
        array = []
        array = Recommendations(name)
        print(array)
    # if request.method=="GET":    
        for movie in array:
            query = 'https://api.themoviedb.org/3/search/movie?api_key='+api_key+'&query='+movie+''
            response = requests.get(query)
            if(response.status_code == 200):
                array1 = response.json()
                text = json.dumps(array1)
                print(text)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)