import tkinter
from tkinter import *
from tkinter import messagebox
 
val=""
A = 0
operator=""
 
def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)
 
def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)
 
def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)
 
def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)
 
def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)
 
def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)
 
def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)
 
def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)
 
def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)
 
def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)
 
def btn_add_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)
 
def btn_sub_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)
 
def btn_mul_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "×"
    val = val + "×"
    data.set(val)
 
def btn_div_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)
 
def btn_equal_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "="
    val = val + "="
    data.set(val)
 
def C_pressed():
    global A
    global operator
    global val
    val = ""
    A=0
    operator=""
    data.set(val)
 
 
def result():
    global A
    global operator
    global val
    val2 = val
    if operator == "+":
        x=int((val2.split("+")[1]))
        c = A + x
        data.set(c)
        val=str(c)
    elif operator == "-":
        x=int((val2.split("-")[1]))
        c = A - x
        data.set(c)
        val=str(c)
    elif operator == "×":
        x=int((val2.split("×")[1]))
        c = A * x
        data.set(c)
        val=str(c)
    elif operator == "/":
        x=float((val2.split("/")[1]))
        if x==0:
            messagebox.show("Error","Division by 0 Not Allowed")
            A==""
            val=""
            data.set(val)
        else:
            c=float(A/x)
            c = round(c, 2)
            data.set(c)
            val=float(c)

#root window
root = tkinter.Tk()
#geometry
root.geometry("300x400")
#resize
root.resizable(True,True)
#tiltle to your window
root.title("Calculator")

#Label
data= StringVar()
lbl=Label(
    root,
    text="Label",
    anchor=SE,
    font=("Comic Sans MS", 50, "bold"),
    textvariable=data,
    background="#252324",
    fg="#FFFDFA",
)

lbl.pack(expand=True,fill="both",)

#Frame Coding for Buttons
#Frame for root window
#Frame 1
btnrow1=Frame(root,bg="#000000")
btnrow1.pack(expand=True,fill="both",)
 
#Frame 2
btnrow2=Frame(root,bg="#000000")
btnrow2.pack(expand=True,fill="both",)
 
#Frame 3
btnrow3=Frame(root,bg="#000000")
btnrow3.pack(expand=True,fill="both",)
 
#Frame 4
btnrow4=Frame(root,bg="#000000")
btnrow4.pack(expand=True,fill="both",)

#Button row One
#Button 1
btn1=Button(
    btnrow1,
    text = "1️⃣",
    font = ("Comic Sans MS", 30),
    relief =RAISED,
    border=0,
    command = btn_1_isclicked,
    fg='#8EE4AF',
    
)

btn1.pack(side=LEFT,expand=True,fill="both",)
 
#Button 2
btn2=Button(
    btnrow1,
    text = "2️⃣",
    font = ("Comic Sans MS", 30),
    relief =RAISED,
    border=0,
    command = btn_2_isclicked,
)

btn2.pack(side=LEFT,expand=True,fill="both",)
 
#Button 3
btn3=Button(
    btnrow1,
    text = "3️⃣",
    font = ("Comic Sans MS", 30),
    relief =RAISED,
    border=0,
    command = btn_3_isclicked,
)

btn3.pack(side=LEFT,expand=True,fill="both",)
 
#Button add
btnadd=Button(
    btnrow1,
    text = "➕",
    font = ("Comic Sans MS", 30),
    relief =RAISED,
    border=0,
    command = btn_add_clicked,
)

btnadd.pack(side=LEFT,expand=True,fill="both",)
 
#Button row Two
#Button 4
btn4=Button(
    btnrow2,
    text = "4️⃣",
    font = ("Comic Sans MS", 30),
    relief =RAISED,
    border=0,
    command = btn_4_isclicked,
)

btn4.pack(side=LEFT,expand=True,fill="both",)
 
#Button 5
btn5=Button(
    btnrow2,
    text = "5️⃣",
    font = ("Comic Sans MS", 30),
    relief =RAISED,
    border=0,
    command = btn_5_isclicked,
)

btn5.pack(side=LEFT,expand=True,fill="both",)
 
#Button 6
btn6=Button(
    btnrow2,
    text = "6️⃣",
    font = ("Comic Sans MS", 30),
    relief =RAISED,
    border=0,
    command = btn_6_isclicked,
)

btn6.pack(side=LEFT,expand=True,fill="both",)
 
#Button Subtraction
btnsub=Button(
    btnrow2,
    text = "➖",
    font = ("Comic Sans MS", 30),
    relief =RAISED,
    border=0,
    command = btn_sub_clicked,
)

btnsub.pack(side=LEFT,expand=True,fill="both",)
 
#Button row Three
#Button 7
btn7=Button(
    btnrow3,
    text = "7️⃣",
    font = ("Comic Sans MS", 30),
    relief =RAISED,
    border=0,
    command = btn_7_isclicked,
)

btn7.pack(side=LEFT,expand=True,fill="both",)
 
#Button 8
btn8=Button(
    btnrow3,
    text = "8️⃣",
    font = ("Comic Sans MS", 30),
    relief =RAISED,
    border=0,
    command = btn_8_isclicked,
)

btn8.pack(side=LEFT,expand=True,fill="both",)
 
#Button 9
btn9=Button(
    btnrow3,
    text = "9️⃣",
    font = ("Comic Sans MS", 30),
    relief =RAISED,
    border=0,
    command = btn_9_isclicked,
)

btn9.pack(side=LEFT,expand=True,fill="both",)
 
#Button Multiply
btnmul=Button(
    btnrow3,
    text = "✖️",
    font = ("Comic Sans MS", 30),
    relief =RAISED,
    border=0,
    command = btn_mul_clicked,
)

btnmul.pack(side=LEFT,expand=True,fill="both",)
 
#Button row Four
#Button C
btnC=Button(
    btnrow4,
    text = "🔄",
    font = ("Comic Sans MS", 30),
    relief =RAISED,
    border=0,
    command = C_pressed,
)

btnC.pack(side=LEFT,expand=True,fill="both",)
 
#Button 0
btn0=Button(
    btnrow4,
    text = "0️⃣",
    font = ("Comic Sans MS", 30),
    relief =RAISED,
    border=0,
    command = btn_0_isclicked,
)

btn0.pack(side=LEFT,expand=True,fill="both",)
 
#Button Equal to
btnequal=Button(
    btnrow4,
    text = "=",
    font = ("Comic Sans MS", 57),
    relief =RAISED,
    border=0,
    command=result,
    fg="red",
)

btnequal.pack(side=LEFT,expand=True,fill="both",)
 
#Button Divide
btndiv=Button(
    btnrow4,
    text = "➗",
    font = ("Comic Sans MS", 30),
    relief =RAISED,
    border=0,
    command = btn_div_clicked,
     
)

btndiv.pack(side=LEFT,expand=True,fill="both",)
 
 
root.mainloop()