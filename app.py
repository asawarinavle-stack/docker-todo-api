from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory storage
tasks = []
task_id = 1


# Home page (UI)
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

    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Task name is required"}), 400

    task = {
        "id": task_id,
        "name": data["name"]
    }

    tasks.append(task)
    task_id += 1

    return jsonify(task), 201


# Delete task
@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    global tasks

    tasks = [t for t in tasks if t["id"] != id]

    return jsonify({"message": "Task deleted"})


# Health check route (important for debugging)
@app.route("/health")
def health():
    return jsonify({"status": "running"})


# Run app
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )