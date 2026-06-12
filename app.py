from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

tasks = []
task_id = 1

# UI Route
@app.route("/")
def home():
    return render_template("index.html")

# Get all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

# Add task
@app.route("/tasks", methods=["POST"])
def add_task():
    global task_id
    data = request.json

    task = {
        "id": task_id,
        "name": data["name"]
    }

    tasks.append(task)
    task_id += 1

    return jsonify(task)

# Delete task
@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    global tasks
    tasks = [t for t in tasks if t["id"] != id]
    return jsonify({"message": "Task deleted"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)