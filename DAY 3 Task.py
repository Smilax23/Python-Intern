from tkinter import *
import tkinter.messagebox
root =Tk()
root.title("Registration Form")
root.geometry('700x400')
root.configure(background = "#33FFA4")



label1=Label(root ,text= "Intern Registration Form ",bg="#33FFA4",fg="#143D59", font=("bold", 20)).grid(row =0, column=2)
Firstname = Label(root ,text = "First Name",width=20,fg="#143D59",bg="#33FFA4",font=("bold", 10)).grid(row = 1,column = 1)
LastName = Label(root ,text = "Last Name",width=20,fg="#143D59",bg="#33FFA4",font=("bold", 10)).grid(row = 2,column = 1)
Address = Label(root,text = "Address",width=20,fg="#143D59",bg="#33FFA4",font=("bold", 10)).grid(row = 3,column = 1)
Mobile = Label(root ,text = "Contact Number",fg="#143D59",width=20,bg="#33FFA4",font=("bold", 10)).grid(row = 8,column = 1)
Email = Label(root ,text = "Email Id",width=20,fg="#143D59",bg="#33FFA4",font=("bold", 10)).grid(row = 9,column = 1)
Gender =Label(root ,text = "Gender",width=20,fg="#143D59",bg="#33FFA4",font=("bold", 10)).grid(row = 10,column = 1)
var = IntVar()
Radiobutton(root, text="Male",fg="#143D59",bg="#33FFA4",padx = 30, variable=var, value=1).grid(row = 10,column = 2)
Radiobutton(root, text="Female",fg="#143D59",bg="#33FFA4",padx = 20, variable=var, value=2).grid(row = 10,column = 3)

Department = Label(root ,text = "Department",bg="#33FFA4",fg="#143D59",width=20,font=("bold", 10)).grid(row = 7,column = 1)
list1 = ['Cse','Ece','It','Mech']
c=StringVar()
droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)

c.set('Select ur Dept')
City = Label(root ,text = "City",width=20,bg="#33FFA4",fg="#143D59",font=("bold", 10)).grid(row = 4,column = 1)
State= Label(root,text = "state",width=20,bg="#33FFA4",fg="#143D59",font=("bold", 10)).grid(row = 5,column = 1)
droplist.grid(row = 7,column = 2)
label_12 = Label(root, text="Language",bg="#33FFA4",fg="#143D59",width=20,font=("bold", 10))
label_12.grid(row = 12,column = 1)

var1 = IntVar()
Checkbutton(root, text="English",bg="#33FFA4",fg="#143D59", variable=var1).grid(row = 12,column = 2)
var2 = IntVar()
Checkbutton(root, text="Tamil",bg="#33FFA4",fg="#143D59", variable=var2).grid(row = 12,column = 3)

# Creating CheckBox
# The variable 'variable' mentioned here holds Integer value, by default 0
variable=IntVar()

# This will creates checkbutton widget and uses place() method.


Firstname1 = Entry(root).grid(row = 1,column = 2)
Lastna = Entry(root).grid(row = 2,column = 2)
Adderss1=Entry(root).grid(row = 3,column = 2)
city1=Entry(root).grid(row = 4,column = 2)
state1=Entry(root).grid(row = 5,column = 2)
Email1 = Entry(root).grid(row = 9,column = 2)
Mobile1 = Entry(root).grid(row = 8,column = 2)



def onClick():
    tkinter.messagebox.showinfo("Welcome", "Your Details Submitted  Successfully !")


# Create a Button
Button(root, text="Submit", command=onClick,width=20,bg="#0C2DEE",fg='white').grid(row = 14,column = 2)


root.mainloop()
