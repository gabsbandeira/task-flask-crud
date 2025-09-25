from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

#CRUD - Create, Read, Update, Delete : Criar ler, Atualizar, Deletar
# Tabela - Tarefas

tasks = []
task_id_control = 1

@app.route("/tasks", methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data['title'], description=data.get('description', ''))
    task_id_control += 1
    tasks.append(new_task)
    return jsonify({"message": "Nova tarefa criada com sucesso"})

@app.route("/tasks", methods=['GET'])
def get_tasks():
    task_list =  [task.to_dict() for task in tasks]
    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }
    return jsonify(output)

@app.route("/tasks/<int:task_id>", methods=['GET'])
def get_task(task_id):
    for t in tasks:
        if t.id == task_id:
            return jsonify(t.to_dict())
    return jsonify({"message": "Tarefa não encontrada"}), 404

@app.route("/tasks/<int:task_id>", methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task.id == task_id:
            task.title = data.get('title', task.title)
            task.description = data.get('description', task.description)
            task.completed = data.get('completed', task.completed)
            return jsonify({"message": "Tarefa atualizada com sucesso"})
    return jsonify({"message": "Tarefa não encontrada"}), 404

@app.route("/tasks/<int:task_id>", methods=['DELETE'])
def delete_task(task_id):
    for task in tasks:
        if task.id == task_id:
            print(task.to_dict())
            tasks.remove(task)
            return jsonify({"message": "Tarefa deletada com sucesso"})
    return jsonify({"message": "Tarefa não encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True)