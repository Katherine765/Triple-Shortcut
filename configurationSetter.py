import json, os
from tkinter import *
from tkinter import PhotoImage, ttk
folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(folder)

pagKeys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','enter','esc','escape','tab','backspace','delete','insert','home','end','pageup','pagedown','up','down','left','right','space','capslock','numlock','scrolllock','[',']','{','}','(',')',';',':','\'','"','\\','|',',', '.', '/', '?','`','~','!','@','#','$','%','^','&','*','-','_','+','=',]

root = Tk()
root.title('Triple Shortcut Configurer')
root.config(bg='#7694FD')
img = PhotoImage(file='banner.png').subsample(2)
banner = Label(root, image=img, borderwidth=0)
banner.pack()
Label(root,text='Select any modifiers, then type one modified key (such as v, tab, or 4) in the box. Invalid configurations WON\'T be uploaded.',bg='#7694FD',relief='flat',font=('Segoe UI',10,'bold')).pack(padx=10,pady=7)

configFrame = Frame(root)
configFrame.config(bg='#7694FD')
configFrame.pack(pady=4)

listBoxes = []
stringVars = []
for i in range(3):
    keyFrame=Frame(configFrame)
    keyFrame.config(bg='#7694FD', width=281)
    keyFrame.pack(side=LEFT, ipadx=20)

    Label(keyFrame, text=['Left','Middle','Right'][i], bg='#7694FD', borderwidth=0, font=('Eras Bold ITC',25,'bold')).pack(pady=15)

    listBoxes.append(Listbox(keyFrame, height=6,selectmode='multiple', bg='#7694FD', borderwidth=0, font=('Helvetica',12,'bold'), exportselection=False, justify='center',selectbackground='#72CDFB',activestyle='none', selectforeground='black',highlightthickness=0))
    for modifier in ('Shift','Control','Command','Alt','Option','Win'):
        listBoxes[-1].insert(END, modifier)
    listBoxes[-1].pack()
    
    stringVars.append(StringVar())
    entry= Entry(keyFrame,bg='#7694FD', justify='center',bd=3,font=('Helvetica',12,'bold'), relief='flat', highlightthickness=3, highlightbackground="black", highlightcolor="black", textvariable=stringVars[-1])
    entry.pack(side=BOTTOM)

def upload():
    with open('configurations.json') as file:
        configurations = json.load(file)
    for i in range(3):
        keys  = [listBoxes[i].get(j) for j in listBoxes[i].curselection()]        
        keys.append(stringVars[i].get()) # last key in hotkey order
        if keys[-1] in pagKeys:
            configurations[str(i)] = keys
    with open('configurations.json','w') as file:
        json.dump(configurations, file)

Button(root, text='Upload configurations', command=upload, relief='flat').pack(anchor='ne', padx=20,pady=20)
root.mainloop()