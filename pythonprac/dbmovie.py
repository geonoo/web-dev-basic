from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:test@cluster0.lommb.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

score = db.movies.find_one({'title':'가버나움'})['score']
movies = list(db.movies.find({'score':score},{'_id':False}))

for movie in movies:
    print(movie['title'])

db.movies.update_one({'title':'가버나움'},{'$set':{'score':'0'}})
