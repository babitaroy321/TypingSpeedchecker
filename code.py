from time import *
import random as r

def mistakes(paratest,usertest):
    error=0
    for i in range(len(paratest)):
        if paratest[i]!= usertest[i]:
            error+=1
    return error

def speedtime(time_s,time_e,userinput):
    time_delay=(time_e-time_s)
    roundtime=round(time_delay)
    speed=len(userinput)/roundtime
    return round(speed)

test=[
    "My name is babita roy.I'm 20 years old.My hobby is study,reading books,drawing,singing etc.I've many dreams in my life e.g travelling,becoming very good engineer.",
      "I am pursuing btech in ECE.I am now 3rd year student.My college is located at Sonarpur,Kolkata under MAKAUT university.",
      "I wish i could become very good person.Bacause I beleive that personality is best reflection of a person rather that his/her academic qualification."
]
test1= r.choice(test)
print(" ********Typing Speed******** ")
print()
print(test1)
time_1=time()
userinput=input("Enter what showing on screen: ")
time_2=time()

print("speed: ", speedtime(time_1,time_2,userinput),"word/sec")
print("error: ", mistakes(test1,userinput))