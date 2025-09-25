import pytest
import requests

# CRUD

BASE_URL = 'http://127.0.0.1:5000'
tasks = []

def test_create_task():
    new_task_data = {
        "title": "Nova Tarefa",
        "description": "Isso é uma tarefa teste"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "id" in response_json
    assert "message" in response_json
    tasks.append(response_json["id"])

def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json
    assert response_json["total_tasks"] >= len(tasks)

def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json['id'] == task_id
        assert "title" in response_json
        assert "description" in response_json
        assert "completed" in response_json

def test_update_task():
    if tasks:
        task_id = tasks[0]
        payload = {
            "title": "Tarefa Atualizada",
            "description": "Descrição atualizada",
            "completed": False
        }
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        #Nova requisição para verificar se a tarefa foi atualizada
        get_response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert get_response.status_code == 200
        get_response_json = get_response.json()
        assert get_response_json["title"] == payload["title"]
        assert get_response_json["description"] == payload["description"]
        assert get_response_json["completed"] == payload["completed"]

def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        # Verificar se a tarefa foi realmente deletada
        get_response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert get_response.status_code == 404
        tasks.remove(task_id)