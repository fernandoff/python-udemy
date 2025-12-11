import tkinter as tk

window = tk.Tk()
window.title("Simple Tkinter Window")
window.geometry("600x300")
label = tk.Label(window, text="Hello, Tkinter!", font=("Arial", 15))
label.pack(pady=20)


#adicionar um frame
frame = tk.Frame(window, borderwidth=2, relief="sunken")
frame.pack(pady=10, padx=10, fill="both", expand=True)

#adicionar uma entry que ocupa todo o frame
entry = tk.Entry(frame, font=("Arial", 15))
entry.pack(pady=10, fill="x", expand=True)

#label para mostrar o texto do entry
result_label = tk.Label(frame, text="", font=("Arial", 15))
result_label.pack(pady=10)

#função para atualizar o label com o texto do entry
def update_label():
    result_label.config(text=entry.get())

button = tk.Button(frame, text="Click Me", command=update_label, font=("Arial", 15))
button.pack(pady=10)



window.mainloop()