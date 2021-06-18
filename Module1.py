## Task 8
import pyttsx3
import camelcase
import emoji
def task8():
    data = input("Enter your data: ")
    x = camelcase.CamelCase()
    if data==x.hump(data):
        print(emoji.emojize(':thumbs_up:'))
    else:
        x = camelcase.CamelCase()
        y = x.hump(data)
        print("Given data is converted into CamelCase: ",y)
        spk = pyttsx3.init()
        spk.say("Successfully converted your data into camel case")
        spk.runAndWait()