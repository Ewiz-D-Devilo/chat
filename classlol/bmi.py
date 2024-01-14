from tkinter import *

def bmi_calculate():
    heightValue=int(heightEntry.get())/100
    weightValue=int(weightEntry.get())
    bmi=weightValue/(heightValue*heightValue)
    bmi = round(bmi,1)
    print(bmi)

    name = userName.get()
    result_label.destroy()

    msg=""

    if bmi < 18.5:
        msg="you are underweight"
    elif bmi > 18.5 and bmi <=24.9:
        msg="you are normal"
    elif bmi > 25 and bmi <= 29.9:
        msg="you are overweight"
    elif bmi > 30:
        msg="obese"
    else:
        msg="smth wrong with you"

    output= Label(result_frame,text=name+", heres ur bmi: "+str(bmi)+"! and " +msg,bg="gray",font=("Calibri",10),width=40)
    output.place(x=20,y=40)
    output.pack()


window= Tk()

window.title("bmi calculator")
window.geometry('380x400')
window.configure(bg="gold")

app_label=Label(window,text="bmi calculator",fg="red",bg="gold",font=("Calibri",30))
app_label.place(x=50,y=20)

name_label=Label(window,text="Your name", fg="black",bg="gold",font=("Calibri",20))
name_label.place(x=20,y=90)

userName= Entry(window,text="",bd=2,width=25)
userName.place(x=170,y=92)

height_label=Label(window,text="height (cm)",fg="black",bg="gold",font=("Calibri",15))
height_label.place(x=20,y=140)
heightEntry=Entry(window,text="",bd=2, width=25)
heightEntry.place(x=150,y=150)

weight_label=Label(window,text="weight (kg)",fg="black",bg="gold",font=("Calibri",15))
weight_label.place(x=20,y=190)
weightEntry=Entry(window, text="",bd=2,width=25)
weightEntry.place(x=150,y=190)

calc_button=Button(window,text="calculate",fg="black",bg="lightblue",font=("Calibri",12),command=bmi_calculate)
calc_button.place(x=220,y=250)

result_frame= LabelFrame(window,text="Result",bg="gray",font=("Calibri",12))
result_frame.place(x=20,y=300)

result_label= Label(result_frame,text="",bg="gray",font=("Calibri",12),width=25)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()