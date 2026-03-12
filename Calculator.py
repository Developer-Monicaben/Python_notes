import tkinter as tk


def Calculate():
    try:
        num1=int(label1_entry.get())
        num2=int(label2_entry.get())
        operations=operations_var.get()

        if operations == "Add":
            result=num1+num2
        elif operations == "Substract":
            result=num1-num2
        elif operations =="Multiply":
            result=num1*num2
        elif operations =="Division":
            if num2!=0:
                result=num1/num2
            else:
                result_Label.config(window,text="Cant divide by Zero !!")
        else:
            result_Label.config(window,text="Select Operation!!")

        result_Label.config(text=f"result : {result}")
    except ValueError:
        result_Label.config(window,text="Enter Valid Numbers ")


# Created window
window=tk.Tk()
window.title("Calculate")
window.geometry("400x400")

# Label and Entry field
label1=tk.Label(window,text="Number1",font=("Arial",11)).pack(pady=5)
label1_entry=tk.Entry(window)
label1_entry.pack(pady=5)

label2=tk.Label(window,text="Number2" ,font=("Arial",11)).pack(pady=5)
label2_entry=tk.Entry(window)
label2_entry.pack(pady=5)

operations_var=tk.StringVar(value="Add")
operations=["Add","Substract","Multiply","Division"]

for option in operations :
    tk.Radiobutton(window,text=option,variable=operations_var,value=option).pack()

# calculate result 
result_button=tk.Button(window,text="Calculate", command=Calculate).pack()

# for result 
result_Label=tk.Label(window,text=" ")
result_Label.pack(pady=5)


        
window.mainloop()
