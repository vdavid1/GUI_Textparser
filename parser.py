import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfile
#import sys

window = tk.Tk()
window.title("Parser")
window.iconbitmap('triangle_and_circle_L4E_icon.ico')
window.geometry("450x100")

#function of the button

def OpenFile():
    name = askopenfile(initialdir="C:\ ",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choose a file"
                           )
    print (name.read() , file=open("dummy.txt", "w"))


def btn_action():

    with open('dummy.txt', 'r') as werther: #please note that you have to specify the correct path for the textfile
        magicword = str(entry_field1.get())
        wordcount=0
        for word in werther:
            if magicword in word.split():
                    wordcount +=1

    return wordcount

def btn_result():
    lookup=btn_action()

    #textfield
    btn_result = tk.Text(master=window, height=2, width=5)
    btn_result.grid(column=1, row=3)

    btn_result.insert(tk.END, lookup)

#Labeling
#Label search
title=tk.Label(text= "Browse for a file: ")
title.grid(column=0 , row =0)

title=tk.Label(text= "   Please enter the word you are looking for: ")
title.grid(column=0, row=1)

#Label2
title=tk.Label(text= "Number of entries is: ")
title.grid(column=0, row=3)



#Button
button0 =ttk.Button(text="Browse", command=OpenFile)
button0.grid(column=2, row=0)
button1 =ttk.Button(text="Submit", command=btn_result)
button1.grid(column=2, row=1)

#entry field
entry_field1=tk.Entry()
entry_field1.grid(column=1, row=1)

window.mainloop()