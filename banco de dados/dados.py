import tkinter as tk
from tkinter import messagebox, ttk
import json
import os 

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador (Tkinter)")
        self.root.geometry("600x400")

        self.tasks = []
        self.load_tasks()

        self.setup_ui()

    def setup_ui(self):
        #frame principal
        main_frame = tk.Frame(self.root, padx=10, pady=10)
        main_frame.pack(fill = tk.BOTH, expand=True)
        #entrada de tarefa
        tk.Label(main_frame, text="Nova Tarefa:").pack(anchor=tk.W)
        self.task_entry = tk.Entry(main_frame, width=50)
        self.task_entry.pack(pady=5)
        #botoes
        btn_frame = tk.Frame(main_frame)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text= "adicionar", command=self.add_task).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text= "Remover", command=self.remove_task).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text= "Concluir", command=self.complete_task).pack(side=tk.LEFT, padx=5)
        #lista tarefas
        self.task_list = tk.Listbox(main_frame, width=60, height=15)
        self.task_list.pack(pady= 10)
        self.update_task_list()

    def load_tasks (self):
        if os.path.exists('tasks.json'):
            with open ('tasks.json', 'r') as f:
                self.tasks = json.load(f)

    def save_tasks(self):
        with open(' tasks.json', 'w') as f:
            json.dump(self.tasks, f)


    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append({"text": task_text, "completed": False})
            self.save_tasks()
            self.update_task_list()
            self.task_entry.delete(0, tk.END)

        else:
            messagebox.showwarning("aviso", "digite uma tarefa!")

    def remove_task(self):
        try:
            index = self.task_list.curselection()[0]
            del self.tasks[index]
            self.save_tasks()
            self.update_task_list()
        except:
            messagebox.showwarning("Aviso" , "Selecione uma tarefa!")
    
    def complete_tasl(self):
        try:
            index = self.task_list.curselection()[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.save_tasks()
            self.update_task_list()
        except:
            messagebox.showwarning("Aviso", "Selecione uma tarefa!")

    def update_task


    




