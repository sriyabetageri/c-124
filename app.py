from re import U
from flask import Flask, jsonify,request

app = Flask(__name__)

tasks = [
    {
        "id":1,
        "title":U"buy groceries",
        "description":U"milk,cheese,fruits,pizza,vegetables,rice,ice cream",
        "done":False
    },
    {
        "id":2,
        "title":U"learn python",
        "description":U"you need to find a good python tutorial on the web",
        "done": False
    }
]

@app.route("/")
def hello_world():
    return "hello world"

@app.route("/add-data",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data",
                    },400)
    task = {
        "id": tasks[-1]["id"]+1,
        "title": request.json["title"],
        "description": request.json.get("description",""),
        "done": False
            }
    tasks.append(task)
    return jsonify({
        "status":"succsess",
        "message": "provide the data"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data": tasks
        
    })
    
if(__name__ =="__main__"):
    app.run(debug = True)

