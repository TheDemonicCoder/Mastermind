import random

num = random.randrange(1000, 10000)

def inpDig():
    while True:
        try:
            no = int(input("Guess the number (4 digit) "))
            if ((no>=10000) or (no<=1000)):
                print ("Enter a valid 4 digit number!!")
            else:
                return no
        except ValueError:
            print ("Enter a valid 4 digit number!!")
    else:
        return no

n = inpDig()

if (n == num):
    print("Congrats!! You are the real Mastermind!")
else:
    score = 0
    while(n != num):
        score += 1 
        count = 0
        n = str(n)
        num = str(num)
        cor = ['X', 'X', 'X', 'X']
        for i in range(0, 4):
            if (n[i] == num[i]):
                count += 1
                cor[i] = n[i]
            else:
                continue
        if (count <4 and count !=0):
            print("You didn't get the number but close enough.")
            print("You had ", count, "digits correct")
            for j in cor:
                print(j, end='')
            print("\n \n")
            n = inpDig()
        elif(count == 0):
            print("You did not gues any digits correctly.\n Try again. ")
            n = inpDig()
    
    if n==num:
        print("You did it. You guessed the number correctly!\n It took you ", score, " tries.")
        if ( score > 25):
            print("\nIt took you too many tries.")
        else:
            a = 25-int(score)
            print("\nYour total score is ", a)