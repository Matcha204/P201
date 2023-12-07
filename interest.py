from tkinter import *
window=Tk()

# add widgets here


window.title('Interest Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

def calculate_interest():
    p = float(principal.get())
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t)/100
    interest = round(i, 2)
    Showlabel.destroy()

    output_message=Label(result_frame, text=name+', your interest payment is'+str(interest), bg = "lightcyan", font=("Calibri", 12), width=42)
    output_message.place(x=20, y=40)
    output_message.pack()

app_label=Label(window, text="Interest CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

name_label=Label(window, text="Your Name", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

principal_label=Label(window, text="Enter Principal", fg = "black", bg = "lightcyan", font=("Calibri", 12))
principal_label.place(x=20, y=140)

principal_entry=Entry(window, text="", bd=2, width=15)
principal_entry.place(x=150, y=142)

rate_label=Label(window, text="Enter Rate", fg = "black", bg = "lightcyan", font=("Calibri", 12))
rate_label.place(x=20, y=185)

rate_entry=Entry(window, text="", bd=2, width=15)
rate_entry.place(x=150, y=187)

time_label=Label(window, text="Enter Time", fg = "black", bg = "lightcyan", font=("Calibri", 12))
time_label.place(x=20, y=185)

time_entry=Entry(window, text="", bd=2, width=15)
time_entry.place(x=150, y=187)

calculate_button=Button(window,text="Calculate", fg= 'black', bg = "lightcyan", bd= 4 ,command=calculate_interest)
calculate_button.place(x= 20, y= 250)

result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()