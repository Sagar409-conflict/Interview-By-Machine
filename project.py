# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 14:06:54 2021

@author: SAGAR
"""

import time,os
import pandas as pd
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image
import pytesseract
from tkinter import filedialog
from ChatBotFile import chat_bot
from OCRtest import StoreToFile



pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\User\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'


root = Tk()
root.title("Code Run Learn")
root.iconbitmap('robot.ico')
root.geometry('400x400')
language = ['PHP,','php,','PHP','php','C,','c,','C','c','C++','c++','JAVASCRIPT','JAVA SCRIPT','JS,','JS','js,','js','java script','javascript','Java Script','Java script','Javascript','Java','java','JAVA','Python','python','PYTHON']

fetch_list = [1,2,3,4,5]
clicked = tk.StringVar()  
right_ans=0
wrong_ans=0
skip_ans=0
attempt_ans=0 

def verifyAns(whole):
    global right_ans,wrong_ans,attempt_ans,skip_ans,QA
    print(f"Real Answer is : {whole[5][0]}")
    print(f"USER Answer is : {clicked.get()}")
    attempt_ans += 1
    if whole[5][0] == clicked.get() :
        right_ans += 1
    elif "Skip" == clicked.get() or "Select an Option" == clicked.get():
        skip_ans += 1
    else:
        wrong_ans += 1
       
        
    file_data=f"""
                Right Answers :-  {right_ans}\n
                Wrong Answers :-  {wrong_ans}\n
                Skipped Answers :-  {skip_ans}\n
                ________________________________\n
                Total Attempted Question :-  {attempt_ans}\n
    """
    bot_Label.config(text=file_data)    
    
    """    
    with open("Candidate/OPresult.txt",'w') as file:    
        file.write(f"Right Answers :-  {right_ans}\n")
        file.write(f"Wrong Answers :-  {wrong_ans}\n")
        file.write(f"Skipped Answers :-  {skip_ans}\n")
        file.write("________________________________\n")
        file.write(f"Total Attempted Question :-  {attempt_ans}\n")
    """    
    QA.destroy()
   
def funct_q_gen(self):
    global QA
    
    
    filename = self.lower() +".csv"
    print(filename)
    df = pd.read_csv(filename)
    
    
    
    sample =  df.sample(1)
    print_sample = list(sample.Question)
    print_sample.append(list(sample.A))
    print_sample.append(list(sample.B))
    print_sample.append(list(sample.C))
    print_sample.append(list(sample.D))
    print_sample.append(list(sample.ANSWER))
    print_sample_text = f"{print_sample[0]} \n\n [A] {print_sample[1][0]} \t [B] {print_sample[2][0]} \n\n [C] {print_sample[3][0]} \t [D] {print_sample[4][0]}"
    
    QA.destroy()
    
    QA = Toplevel()
    QA.title("Attempt Question")
    QA.iconbitmap('robot.ico')
    QA.deiconify()
    QA.geometry('1500x500')
    
    te234 = Label(QA,justify=CENTER,font = "Helvetica 20 bold italic",fg="white",bg="#FF5733",text=print_sample_text)
    te234.pack()
    
    
    clicked.set("Select an Option")
    drop = OptionMenu(QA,clicked,"A","B","C","D","Skip")
    drop.pack()
    
    lock = Button(QA,text="Lock Answer",font = "Helvetica 18 bold italic",command = lambda : verifyAns(print_sample),padx=20,pady=5,fg="black",bg="#44cf52").place(x=380,y=180)
    stop = Button(QA,text="Stop Attempt",font = "Helvetica 18 bold italic",command = root.destroy,padx=20,pady=5,fg="white",bg="#ec2727").place(x=820,y=180)
    #clicked.set(clicked.get())
    #print(f"Answer {clicked.get()}")
    """
    print(clicked.get())
    print(type(clicked.get()))
    print(print_sample[5][0])
    print(type(print_sample[5][0]))

    
    if str(clicked.get()) == str(print_sample[5][0]):
        right_ans += 1
    elif clicked.get() == "Skip":
        skip_ans += 1
    else:
        wrong_ans += 1
      
        """
    
        
    #bot_Label.config(text=print_sample)
    
    
def upload_file():
    top.filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select a file",filetypes=(("PNG Files","*.png"),("JPG Files","*.jpg"),("JPEG Files","*.jpeg"),("All Files","*.*")))
    fileLabel = tk.Label(top,text="sagar")
    fileLabel.config(text=top.filename)
    fileLabel.pack()
    
    
    image1saved =Image.open(top.filename)
    imgCopy=top.filename
    
    arr = imgCopy.split("/")
    print(f"Sagar:-{arr[len(arr)-1]}")
    
    #imgsaved = img.resize((250, 250), Image.ANTIALIAS)
    imgdisp = ImageTk.PhotoImage(image1saved)
    imageStore = Label(top,image=imgdisp)
    imageStore.image = imgdisp
    imageStore.place(x=50,y=110)
    #imageStore.draw()
    top.filename=""
    StoreToFile(arr[len(arr)-1])
    
    count=1
    with open('checktext.txt','r') as k:
        data = k.readlines()
        print("---------------------------------------------")
        print("List of Computer Languages Candidate Know")
        print("---------------------------------------------")
        buttons_list = [5,6,7,8,9]
        exist_or_not = 0
        x_pos = 5
        for i in data:
            lis1 = i.split()
            #print(lis1)
            for lang in language:
                if lang in lis1:
                    print(f"{count}).{lang}")
                    exist_or_not = 1
                    refector_str = lang.strip()
                    if refector_str[len(refector_str)-1] == ",":
                        refector_str = refector_str[:-1]
                    
                    fetch_list[count-1]=refector_str
                    
                    buttons_list[count-1] = Button(root,text=refector_str.upper(),padx=10,pady=5,command=lambda m=refector_str : funct_q_gen(m),bg="black",fg="#fff")
                    
                    buttons_list[count-1].place(x=x_pos,y=300)
                    x_pos += 55
                    count+=1
        
        if exist_or_not == 0:
            notEligible = Button(root,text="Sorry, You are not eligible for this Interview",padx=10,pady=5,command=root.destroy,bg="#f5cc51",fg="black")
            notEligible.place(x=40,y=300)
            
    
def imageWindow():
    global top,right_ans,wrong_ans,attempt_ans,skip_ans
    
    
    top = Toplevel()
    top.iconbitmap('photo.ico')
    #top.attributes('-fullscreen', True)
    top.title("Upload an Image")
    top.geometry('400x400')
    top['background']='#856ff8'
    
    
    
    textLabel = Label(top,justify=CENTER,font = "Helvetica 20 bold italic",fg="white",bg="#856ff8",text="Upload your Image Here")
    textLabel.pack()
    
    openButton = Button(top,text="Upload Your CV",padx=20,pady=5,fg="white",bg="#C71585",command = upload_file).pack()
                        

    
    
    
def chatClick(textBox):
    
    
    bot_response = chat_bot.get_response(textBox)
    bot_Label.config(text=bot_response)
    
    
    
def myClick():
    global type_Label
    textBox = inputHere.get()
    
    user_Label.config(text=textBox)
    user_Label.pack_forget()    
    inputHere.delete(0,END)
    if textBox not in ['yes','YES','Yes']:
        chatClick(textBox)
    else:
        imageWindow()
        
   




#images here
imgChat = ImageTk.PhotoImage(Image.open("chat.jpg"))

my_label = Label(root,image=imgChat)
my_label.place(x=0,y=0,relwidth=1,relheight=1)

buttonSend = Button(root,text="Send",padx=20,pady=5,command=myClick,bg="green",fg="#fff")
buttonSend.place(x=320,y=350)

button_quit = Button(root,text="Exit",padx=23,pady=5,command=root.destroy,bg="#ED2165",fg="#fff")
button_quit.place(x=320,y=300)

inputHere = Entry(root,width=24,fg="white",font=('Helvetica',18))
inputHere.configure(bg="black", insertbackground='white')
inputHere.place(x=0,y=350)
user_Label = Label(root)
user_Label.place(x=250,y=50)
bot_Label = Label(root)
bot_Label.place(x=0,y=80)

QA = Toplevel()
QA.title("Attempt Question")
QA.iconbitmap('robot.ico')
QA.geometry('500x300')
QA.withdraw()
root.mainloop()
