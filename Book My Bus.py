from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
import datetime
from datetime import date,datetime
import webbrowser

root = Tk()

# Setting Title and Geometry
root.title('Ajit Travels (Licenced_Version @2020-2021)')
root.geometry("960x530+228+170")

# Setting icon
icon = PhotoImage(file='bus.png')
root.iconphoto(False,icon)

# Setting Train Image
image = PhotoImage(file='bus3.png')
image_label = Label(image=image,relief=FLAT,bd=0)
image_label.place(x=500,y=160)

# Disabling maxsize and minsize
root.overrideredirect(1)
# Setting GUI background colour
root.configure(bg='white')

# Setting Heading of GUI
Label(root,text='Ajit Travels',font="Algerian 45 bold underline",bg='white',fg='black',pady=10).pack()

# Text labels  and its Placing with grid of gui
From_Label = Label(root,text='From',bg='white',fg='black',font='Cambria 14',padx=4).place(y=130)
To_Label = Label(root,text='To',bg='white',fg='black',font='Cambria 14',padx=4).place(y=162)
Date_Label = Label(root,text='Date',bg='white',fg='black',font='Cambria 14',padx=4).place(y=192)
name_Label = Label(root,text='Name',bg='white',fg='black',font='Cambria 14',padx=4).place(y=222)
age_Label = Label(root,text='Age',bg='white',fg='black',font='Cambria 14',padx=4).place(y=282)
contact_Label = Label(root,text='Contact no.',bg='white',fg='black',font='Cambria 14',padx=4).place(y=312)
rupee_Label = Label(root,text='Total(₹)',bg='white',fg='black',font='Cambria 14',padx=4).place(y=342)

# Tkinter variable for storing value
fromvalue = StringVar()
tovalue = StringVar()
datevalue = StringVar()
name_value = StringVar()
age_value = StringVar()
contact_value = StringVar()
rupee_value = StringVar()
foodservice_value = IntVar()
Gender_value = IntVar()

# Setting gender value default to 1
Gender_value.set(1)

# Entry widgets and its packing with grid of gui
name_entry = Entry(root,textvariable=name_value,font='Cambria 13',relief=GROOVE,bd=2,bg='snow',fg='black')
age_entry = Entry(root,textvariable=age_value,font='Cambria 13',relief=GROOVE,bd=2,bg='snow',fg='black')
contact_entry = Entry(root,textvariable=contact_value,font='Cambria 13',relief=GROOVE,bd=2,bg='snow',fg='black')
rupee_entry = Entry(root,textvariable=rupee_value,font='Cambria 13',relief=GROOVE,bd=2,bg='snow',fg='black')
foodservice = Checkbutton(variable=foodservice_value,text='Want to prebook your meals?',font='Cambria 13',bg='white')

# placing entries
name_entry.place(x=160,y=222)
age_entry.place(x=160,y=282)
contact_entry.place(x=160,y=312)
rupee_entry.place(x=160,y=342)
foodservice.place(x=134,y=372)

# Radio Button for male or female or others
def radio_clicked(value):
    print(value)

r1 = Radiobutton(root,text='Male',variable=Gender_value,bg='white',font='Cambria 12',value=1).place(x=160,y=252)
r2 = Radiobutton(root,text='Female',variable=Gender_value,bg='white',font='Cambria 12',value=2).place(x=230,y=252)
r3 = Radiobutton(root,text='Other',variable=Gender_value,bg='white',font='Cambria 12',value=3).place(x=310,y=252)

# Making Option Menu for From and To option
def From_combobox_clicked(event):
    # mylabel = Label(root,text=From_combobox.get())
    # mylabel.pack()
    pass


# Date Option
Date_List = [f'{date.today().strftime("%Y-%d-%m")}']
def Date_combo():
    def print_sel():
        Date_List.append(cal.selection_get())

    top = Toplevel(root)
    top.geometry('275x279+385+390')
    top.configure(bg='grey85',bd=2,relief=SUNKEN)
    cal = Calendar(top, font="Arial 14", selectmode='day', cursor="hand2")
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).place(y=242,x=0)
    ttk.Button(top, text='exit', command=top.destroy).pack(side=RIGHT)
    top.overrideredirect(1)

    print('man')
    print(len(str(Date_List)))
    print(str(Date_List))

s = ttk.Style(root)
s.theme_use('clam')


date_button = Button(root,text='Date of Journey',bg='dodger blue',fg='white',relief=RAISED,bd=1,command=Date_combo).place(x=160,y=190)


# From
List_From = ["Mumbai","Kolkata","Lucknow","Chennai","Delhi","Pune","Hyderabad","Pernem","Ahmedabad"]
From_combobox = ttk.Combobox(root,value=List_From,state="readonly",width=33,height=15)
From_combobox.current(8)
From_combobox.bind("<<ComboboxSelected>>",From_combobox_clicked)
From_combobox.place(x=160,y=132)
# To
To_combobox = ttk.Combobox(root,value=List_From,state="readonly",width=33,height=15)
To_combobox.current(0)
To_combobox.bind("<<ComboboxSelected>>",From_combobox_clicked)
To_combobox.place(x=160,y=162)



# Checking entries validity
def checkname():
    try:
        var = name_value.get()
        print(var)
        if ((int(name_value.get())) or (int(name_value.get())) == 0):
            messagebox.showerror('Invalid Name!','Enter a Valid Name')
    except:
        if name_value.get() == "":
            messagebox.showerror('Invalid Name!','Enter a Valid Name')

def samecity():
    if From_combobox.get() == To_combobox.get():
        messagebox.showerror('Invalid Station!','Select Different Boarding/Destination Station')

def ageisstring():
    try:
        var2 = int(age_value.get())
        if var2 <= 0 or var2 >= 150:
            messagebox.showerror('Invalid Age!', 'Enter a Valid Age of Passenger')

    except ValueError:
        messagebox.showerror('Invalid Age!', 'Enter a Valid Age of Passenger')

def contact10digit():
    try:
        if int(contact_value.get())==0:
            messagebox.showerror('Invalid Contact!', 'Enter a Valid Contact Number')
        if int(contact_value.get()):
            if (len(str(int(contact_value.get()))) < 10 or len(str(int(contact_value.get()))) > 10):
                messagebox.showerror('Invalid Contact!', 'Enter a Valid Contact Number')
            if int(contact_value.get()) == 0:
                messagebox.showerror('Invalid Contact!', 'Enter a Valid Contact Number')
    except:
        messagebox.showerror('Invalid Contact!', 'Enter a Valid Contact Number')


def check_rupee():
    try:
        if int(rupee_value.get()):
            if int(rupee_value.get()) < 0:
                messagebox.showerror('Invalid Amount!','Enter a Valid Total(₹) Amount')
    except:
        messagebox.showerror('Invalid Amount!','Enter a Valid Total(₹) Amount')

# Making strip at bottom
frame = Frame(root,relief=FLAT,bd=0)
frame.pack(side=BOTTOM,fill=X)
strip_label = Label(frame,text='© 2018-2020 Ajit Travels All Rights Reserved',font='Arial 10 bold',fg='black',bg='snow2')
strip_label.pack(side=LEFT,expand=True,fill=X)


# Backend

# Function runs when submit button is clicked
def Submit():

    checkname()
    samecity()
    ageisstring()
    contact10digit()
    check_rupee()

    Gender_List = []
    meals_list = []
    def confir_gender():
        if Gender_value.get() ==1:
            Gender_List.append('Male')
        elif Gender_value.get() == 2:
            Gender_List.append('Female')
        elif Gender_value.get() == 3:
            Gender_List.append('Other')

    def confir_meal():
        if foodservice_value.get() == 1:
            meals_list.append('Yes')
        else:
            meals_list.append('No')
    confir_gender()
    confir_meal()

    if (len(name_value.get()) > 0 and len(age_value.get()) > 0 and len(contact_value.get()) >= 10 and len(rupee_value.get()) > 0 and From_combobox.get() != To_combobox.get() ):
        submit_message = messagebox.askquestion('Submit To Ajit Travels!','Are you sure, you want to Submit to Ajit Travels')

    else:
        messagebox.showwarning('Warning','Fill the Details Carefully!')


    from_data = From_combobox.get()
    to_data = To_combobox.get()
    date_data = Date_List[-1]
    name_data = name_value.get()
    age_data = age_value.get()
    gender_data = Gender_List[-1]
    contact_data = contact_value.get()
    meals_data = meals_list[0]
    rupee_data = rupee_value.get()


    if submit_message == 'yes':

        time = datetime.now().time().strftime("%H:%M:%S")

        ampm = 0  # 0 = Am(default)
        if time >= '12:00:00':
            ampm = 1

        f = open(r'C:\Users\HP\Desktop\My Apps\Ajit Travels\Ajit Travels.txt','w')

        f.write('~~~~~~~~~~~~~~~~~~~~~~~NEW~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

        if ampm == 0:
            f.write(f'{datetime.now().time().strftime("%H:%M:%S")} AM\n')  #Today's Time
        elif ampm == 1:
            f.write(f'{datetime.now().time().strftime("%H:%M:%S")} PM\n')  #Today's Time

        f.write(f'{date.today().strftime("%B %d, %Y")}\n')  # Today's date

        f.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        f.write(f' From              |      {from_data}\n')
        f.write('----------------------------------------------------\n')
        f.write(f' To                |      {to_data}\n')
        f.write('----------------------------------------------------\n')
        f.write(f' Date              |      {date_data}\n')
        f.write('----------------------------------------------------\n')
        f.write(f' Name              |      {name_data}\n')
        f.write('----------------------------------------------------\n')
        f.write(f' Age               |      {age_data}\n')
        f.write('----------------------------------------------------\n')
        f.write(f' Gender            |      {gender_data}\n')
        f.write('----------------------------------------------------\n')
        f.write(f' Contact           |      +91 {contact_data}\n')
        f.write('----------------------------------------------------\n')
        f.write(f' Prebook Meals?    |      {meals_data}\n')
        f.write('----------------------------------------------------\n')
        f.write(f' Total Fare        |      {rupee_data}.00 Rupees Only\n')


        g = open(r'C:\Users\HP\Desktop\My Apps\Ajit Travels\Ajit Travels Data.txt', 'a')
        g.write('~~~~~~~~~~~~~~~~~~~~~~~NEW~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

        if ampm == 0:
            g.write(f'{datetime.now().time().strftime("%H:%M:%S")} AM\n')  # Today's Time
        elif ampm == 1:
            g.write(f'{datetime.now().time().strftime("%H:%M:%S")} PM\n')  # Today's Time

        g.write(f'{date.today().strftime("%B %d, %Y")}\n')  # Today's date

        g.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        g.write(f' From              |      {from_data}\n')
        g.write('----------------------------------------------------\n')
        g.write(f' To                |      {to_data}\n')
        g.write('----------------------------------------------------\n')
        g.write(f' Date              |      {date_data}\n')
        g.write('----------------------------------------------------\n')
        g.write(f' Name              |      {name_data}\n')
        g.write('----------------------------------------------------\n')
        g.write(f' Age               |      {age_data}\n')
        g.write('----------------------------------------------------\n')
        g.write(f' Gender            |      {gender_data}\n')
        g.write('----------------------------------------------------\n')
        g.write(f' Contact           |      +91 {contact_data}\n')
        g.write('----------------------------------------------------\n')
        g.write(f' Prebook Meals?    |      {meals_data}\n')
        g.write('----------------------------------------------------\n')
        g.write(f' Total Fare        |      {rupee_data}.00 Rupees Only\n')
        g.write('\n\n\n')


        g.close()
        f.close()

        webbrowser.open_new(r'C:\Users\HP\Desktop\My Apps\Ajit Travels\Ajit Travels.txt')

    else:
        pass



def exit():
    exit_message = messagebox.askquestion(title='Exit!',message='Are you sure you want to exit Ajit Travels?')
    if exit_message=='yes':
        root.quit()
    else:
        pass

# Submit To Ajit Travels
Button(root,text='Submit To Ajit Travels',font='Arial 13',bg='gray86',fg='black',relief=GROOVE,bd=2,command=Submit).place(x=30,y=430)
Button(root,text='Exit From Ajit Travels',font='Arial 13',bg='gray86',fg='black',relief=GROOVE,bd=2,command=exit).place(x=230,y=430)


root.mainloop()