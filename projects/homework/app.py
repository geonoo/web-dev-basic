from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:test@cluster0.lommb.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/homework", methods=["POST"])
def homework_post():
    comment_receive = request.form['comment_give']
    name_receive = request.form['name_give']

    doc ={
        'comment':comment_receive,
        'name':name_receive
    }

    db.fans.insert_one(doc)

    return jsonify({'msg': '저장완료'})


@app.route("/homework", methods=["GET"])
def homework_get():
    fan_list = list(db.fans.find({}, {'_id': False}))
    return jsonify({'fans': fan_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
