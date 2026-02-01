import tkinter as tk
from tkinter import *
root = Tk()
name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
print("Hello", name)
print("You", age, "years old", name)
print("Hello", gender)
if gender == "M":
    print("SOrry You Are Not allowed")
elif gender == "f":
    print("Welcome To Our Party")
else:
    print("Sorry It Is just for M")
root.mainloop()


 

