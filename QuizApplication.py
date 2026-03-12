import tkinter as tk

root=tk.Tk()
root.title("Quiz Application")
root.geometry("500x500")
Titile_label=tk.Label(root,text="Quiz Application",font=("Times New Roman",20)).pack(pady=5)
Question_label=tk.Label(root,text=" 1. What is the Output of : print([1,2,3,4]) ?" ,font=("Arial",14))
Question_label.pack(pady=20)

def Check_Answer(selectedOption):
    if selectedOption == "A. <class 'list'>":
        result_Label.config(text="Correct!!",fg="green")
    else :
        result_Label.config(text="Wrong !!",fg="red")
    

options =["A. <class 'list'>"," B. <class 'tuple'> ","C. <class 'set'>"," D. <class 'dict'>"]


for opt in options:
    option_button=tk.Button(root,text=opt,command=lambda o=opt:Check_Answer(o))
    option_button.pack(pady=5)


result_Label=tk.Label(root,text="",font=("Times New Roman",10))
result_Label.pack(pady=20)
root.mainloop()
