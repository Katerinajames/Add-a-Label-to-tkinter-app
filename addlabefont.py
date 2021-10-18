
import Tkinter
from Tkinter import*
window=Tk()

window.title("Welcome")
label=Label(window,text="Hello",font=("Arial ",50)).grid(column=0,row=0)
window.geometry('200x200')

window.mainloop()
