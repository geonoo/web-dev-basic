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

@app.route("/mars", methods=["POST"])
def web_mars_post():
    name_give = request.form['name_give']
    address_give = request.form['address_give']
    size_give = request.form['size_give']

    doc = {
        'name':name_give,
        'address':address_give,
        'size':size_give
    }

    db.mars.insert_one(doc)

    return jsonify({'msg': '주문완료'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
    order_list = list(db.mars.find({}, {'_id': False}))
    return jsonify({'orders':order_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)