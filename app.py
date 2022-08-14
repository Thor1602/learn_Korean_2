from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/quiz')
def quiz():
    online_users = mongo.db.users.find({"online": True})
    return render_template('quiz.html', online_users=online_users)

if __name__ == '__main__':
    app.run()
