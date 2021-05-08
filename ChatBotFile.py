# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 15:21:27 2021

@author: SAGAR
"""


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

my_bot = ChatBot(name='PyBot', read_only=True,
          logic_adapters = ['chatterbot.logic.MathematicalEvaluation',
          'chatterbot.logic.BestMatch'])

chat_bot = ChatBot(name='PyBot', read_only=True,
          logic_adapters = ['chatterbot.logic.MathematicalEvaluation',
          'chatterbot.logic.BestMatch'])

small_talk = ['hi there!',
          'hi!',
          'how do you do?',
          'how are you?',
          'i\'m cool.',
          'fine, you?',
          'always cool.',
          'i\'m ok',
          'glad to hear that.',
          'i\'m fine',
          'glad to hear that.',
          'i feel awesome',
          'excellent, glad to hear that.',
          'not so good',
          'sorry to hear that.',
          'what\'s your name?',
          'i\'m pybot. ask me a math question, please.']

upload_talk = [
          'image',
          'Do you have an image and upload it ?',
          'picture',
          'Do you have an image and upload it?'
          'cv',
          'Do you have an image and upload it?'
          'resume',
          'Do you have an image and upload it?'
          ]
    
math_talk_1 = ['pythagorean theorem',
          'a squared plus b squared equals c squared.']
math_talk_2 = ['law of cosines',
          'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']

list_trainer = ListTrainer(my_bot)
list_trainer1 = ListTrainer(chat_bot)

for item in (small_talk,upload_talk,math_talk_1, math_talk_2):
    
    list_trainer1.train(item)
    

# print(my_bot.get_response("what's your name?"))
"""
while True:
    usr = input("You : ")
    if usr == "q":
        print("Thank You")
        break
    else:
        print(my_bot.get_response(usr))
"""