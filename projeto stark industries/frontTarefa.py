from tkinter import *
from tkinter.ttk import *
from backTarefa import Tarefa

tarefa = Tarefa()
                            ############## ATENÇÃO !!!!!!!!!!!!!!!!!!!! #################
######### SÓ INFORMAR ID NO FORMULÁRIO QUANDO DESEJAR DELETAR OU EDITAR UMA TAREFA ESPECÍFICA ############

def insert_data():
   
    id_value = id_input.get()
    name_value = name_user.get()
    task_value = task.get()
    start_value = start.get()
    end_value = end.get()
    status_value = status_var.get()
    
    start_value = start_value if start_value else ' '
    end_value = end_value if end_value else ' '
    
    table.insert("", "end", values=(id_value, name_value, task_value, start_value, end_value, status_value))
    tarefa.insert(name_value, task_value, start_value, end_value, status_value)
    update_table()
    
    id_input.delete(0, 'end')
    name_user.delete(0, 'end')
    task.delete(0, 'end')
    start.delete(0, 'end')
    end.delete(0, 'end')
    status_var.set('')

def update_data():
    id_value = id_input.get()
    name_value = name_user.get()
    task_value = task.get()
    start_value = start.get()
    end_value = end.get()
    status_value = status_var.get() 
    
    start_value = start_value if start_value else ' '
    end_value = end_value if end_value else ' '
    tarefa.update(id_value, name_value, task_value, start_value, end_value, status_value)
    update_table()

    id_input.delete(0, 'end')
    name_user.delete(0, 'end')
    task.delete(0, 'end')
    start.delete(0, 'end')
    end.delete(0, 'end')
    status_var.set('')
    

def delete_data():
    id_value = id_input.get()
    tarefa.delete(id_value)
    update_table()

def delete_done_front():
    tarefa.delete_done()
    update_table()

def update_table():
    
    for i in table.get_children():
        table.delete(i)
    
    tarefas = tarefa.list()
    
    for i in tarefas:
        table.insert("", "end", values=(i['id'], i['nome'], i['tarefa'], i['dataInicio'], i['dataFim'], i['status']))


janela = Tk()
janela.geometry("1300x500+400+100")
janela.configure(bg="black")  

style = Style()
style.configure('TButton', background='black', foreground='red')

titulo_label = Label(janela, text="Stark Industries", background="black", foreground="white", font=("Arial", 24, "bold"))
titulo_label.grid(row=0, column=0, columnspan=2, pady=5)

###### INPUTS
id_label = Label(text="ID", background="red", foreground='white')
id_label.grid(row=1, column=1)
id_input = Entry()
id_input.grid(row=2, column=1)

user_label = Label(text="Nome usuário", background="red", foreground='white')
user_label.grid(row=3, column=1)
name_user = Entry()
name_user.grid(row=4, column=1)

task_label = Label(text='Tarefa', background="red", foreground='white')
task_label.grid(row=5, column=1)
task = Entry()
task.grid(row=6, column=1)

start_label = Label(text='Data Inicio', background="red", foreground='white')
start_label.grid(row=7, column=1)
start = Entry()
start.grid(row=8, column=1)

end_label = Label(text='Data Fim', background="red", foreground='white')
end_label.grid(row=9, column=1)
end = Entry()
end.grid(row=10, column=1)

status_label = Label(text="Status", background="red", foreground='white')
status_label.grid(row=11, column=1)
status_var = StringVar()
status_combobox = Combobox(janela, textvariable=status_var, values=['', 'Concluída', 'Em Andamento', 'A Fazer'])
status_combobox.grid(row=12, column=1)

##### TABELA


table = Treeview(columns=('Id', 'Nome', 'Tarefa', 'DataInicio', 'DataFim', 'Status'), show='headings')
table.grid(row=13, column=1)
table.heading('Id', text='ID')
table.heading('Nome', text='Nome')
table.heading('Tarefa', text='Tarefa')
table.heading('DataInicio', text='Data Inicio')
table.heading('DataFim', text='Data Fim')
table.heading('Status', text='Status')

##### BOTOES
button_insert = Button(janela, text='Inserir', command=insert_data, style='TButton')
button_insert.grid(row=1, column=2)

button_update = Button(janela, text='Editar', command=update_data, style='TButton')
button_update.grid(row=2, column=2)

button_delete = Button(janela, text='Deletar', command=delete_data, style='TButton')
button_delete.grid(row=3, column=2)

button_delete_done = Button(janela, text="Deletar Conclusas", command=delete_done_front, style="TButton")
button_delete_done.grid(row=4, column=2)



update_table()
janela.mainloop()
