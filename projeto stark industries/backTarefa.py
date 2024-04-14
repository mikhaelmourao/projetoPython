import pymysql.cursors
from datetime import datetime

######################### É IMPORTANTE CRIAR A TABELA NO SQL ANTES DE EXECUTAR O CÓDIGO#################
# CREATE DATABASE tarefas;
# USE tarefas;
# CREATE TABLE Tarefa (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     nome VARCHAR(50) NOT NULL,
#     tarefa VARCHAR(50) NOT NULL,
#     dataInicio DATE,
#     dataFim DATE,
#     status VARCHAR(50)
# );
    
class Tarefa:
    def __init__(self):
        self.conexao = pymysql.connect(
            user='root',
            host='localhost',
            password='busquei1990', ##MUDAR A SENHA CONFORME O ACESSO DO USUÁRIO SQL
            database='tarefas',  
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.conexao.cursor()

    def insert(self, name_value, task_value, start_value, end_value, status_value):
        try:
            if start_value and end_value:
                start_date = datetime.strptime(start_value, '%Y-%m-%d') if start_value.strip() else None
                end_date = datetime.strptime(end_value, '%Y-%m-%d') if end_value.strip() else None
          
                
            sql = "INSERT INTO tarefa (nome, tarefa, dataInicio, dataFim, status) " \
                  "VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(sql, ((name_value, task_value, start_date, end_date, status_value)))
            self.conexao.commit()
           
        except Exception as error:
            print(f"Erro ao cadastrar! Erro: {error}")
            
    def update(self,id_value, name_value, task_value, start_value, end_value, status_value):
        try:
            if start_value and end_value:
                start_date = datetime.strptime(start_value, '%Y-%m-%d') if start_value.strip() else None
                end_date = datetime.strptime(end_value, '%Y-%m-%d') if end_value.strip() else None
                
            sql= "UPDATE tarefa SET nome=%s, tarefa=%s, dataInicio=%s, dataFim=%s, status=%s WHERE id=%s"
            self.cursor.execute(sql,((name_value, task_value, start_date, end_date, status_value, id_value)))
            self.conexao.commit()
        except Exception as error:
            print(f"Erro ao editar! Erro: {error}")
    
    def delete(self, id_value):
        try:
            sql=" DELETE FROM tarefa WHERE id=%s"
            self.cursor.execute(sql, id_value)
            self.conexao.commit()
        except Exception as error:
            print(f"Erro ao deletar! Erro: {error}")
            
    def delete_done(self):
        try:
            sql="DELETE FROM tarefa WHERE status='Concluída'"
            self.cursor.execute(sql)
            self.conexao.commit()
        except Exception as error:
            print(f"Erro ao deletar tarefas feitas! Erro: {error}")
    
    def list(self):
        try:
            sql="SELECT * FROM tarefa"
            self.cursor.execute(sql)
            self.conexao.commit()
            tarefas = self.cursor.fetchall()
            return tarefas
        except Exception as error:
            print(f"Erro ao listar! Erro: {error}")
            
            



