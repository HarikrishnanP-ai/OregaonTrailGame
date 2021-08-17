import random
print("Game version 2")
alive= 1
history=""
def chal1():
    print("You encounter a bear andhave 2 choices")
    print("Option a:shoot with a gun \nOption b:Run")
    uinp1=input()
    if uinp1=="a":
        print("Lucky .You Survive for another challenge")
        alive=1
    elif uinp1=="b":
        print("Oops..wrong choice u die")
        alive=0
    else:
        print("You didn't follow the rules.As a punishment, just die to make up for it")
        alive=0
    return alive

def chal2():
    print("You encounter a witch . guess a lucky number between 10 and 15")
    randkey=random.randint(10,15)
    uinp2=int(input())
    if uinp2 ==randkey:
        print("Lucky.. you survive")
        alive=1
    elif uinp2>15 and uinp<10:
        print("You betrayed the rules.Die!!")
        alive=0
    else:
        print("Oops Unlucky you .See u in afterlife")
        alive=0
    return alive

def chal3():
    print("You encounter a pit of snakes. guess a lucky number between 1 to 10")
    uinp3=int(input())
    if uinp3 >=5 and uinp3<=8:
        print("You survive.")
        alive=1
    else:
        print("You are dead meat")
        alive=0
    return alive

while alive == 1:
    counter=random.randint(1,3)
    if counter == 1:
         alive=chal1()
         history=history+"1"
    if counter == 2:
         alive=chal2()
         history=history+"2"
    if counter == 3:
         alive=chal3()
         history=history+"3"
    
with open("historia.txt","w") as tf:
    tf.write(history)
    
    
