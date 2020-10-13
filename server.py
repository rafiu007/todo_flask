from flask import Flask, request
import json

app = Flask(__name__)
todo_list = []

@app.route('/')
def hello():
    return "Hello World..!"

@app.route('/todo/add/<todo>', methods=['GET'])
def todo(todo):
    todo_string = todo
    data = {
        "Todo": todo_string
    }
    todo_list.append(data)
    return json.dumps(todo_list)

@app.route('/todo/add', methods=['GET'])
def todo_param():
    todo_string = request.args.get('todo')
    data = {
        "Todo": todo_string
    }
    todo_list.append(data)
    return json.dumps(todo_list)

@app.route('/api/todo/add', methods=['POST'])
def todo_post():
    todo_string = request.form['todo']
    data = {
        "Todo":todo_string
    }
    todo_list.append(data)
    return json.dumps(todo_list)

if __name__ == "__main__":
    app.run(debug=True)



