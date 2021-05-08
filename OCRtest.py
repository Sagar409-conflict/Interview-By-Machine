# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 14:20:33 2021

@author: SAGAR
"""


import pytesseract as tess
from tkinter import *

tess.pytesseract.tesseract_cmd = r'C:\\Users\\User\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
from PIL import Image
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer



def StoreToFile(imageName):
    #root = Tk()
    #s =input("entr")
    #print("Sagar")
    img = Image.open(imageName)
    #print(img)
    te = tess.image_to_string(img)
    #print(te)
    
    
    with open('checktext.txt',"w",encoding="utf-8") as f:
        f.write(te)
    #labelMy = Label(root,text=te)
    #labelMy.pack()
    #root.mainloop()
    #print(text)
