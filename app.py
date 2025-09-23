from flask import Flask

app = Flask(__name__)

#CRUD - Create, Read, Update, Delete : Criar ler, Atualizar, Deletar
# Tabela - Tarefas

tasks = []

if __name__ == "__main__":
    app.run(debug=True)