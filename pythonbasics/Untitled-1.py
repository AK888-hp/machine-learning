#     s w g
#     0 1 2
# s 0 D W L
# w 1 L D W
# g 2 W L D
import random
swg=["Snake","Water","Gun"]
win_lose_matrix=[["D","W","L"],["L","D","W"],["W","L","D"]]
count=[0,0]

def snakewatergun(user_input):
    '''This  function takes user input, gets computer input from random and returns if the user has won or not'''
    pc_input=random.randint(0,2)
    print(f"Computer's choice is:{swg[pc_input]}")
    return win_lose_matrix[user_input][pc_input]

def take_input():
        inp=input("Enter your Choice(Snake,Water,Gun)")
        if inp.capitalize() not in swg:
            print("Not found enter a valid answer")
            return take_input()
        else:
            return inp

def print_result(result):
    if result=="W":
        print("You Won")
        count[0]+=1
        print(f"your wins:{count[0]} and computer wins:{count[1]}")
    elif result=="L":
        print("You lost")
        count[1]+=1
        print(f"your wins:{count[0]} and computer wins:{count[1]}")
    else:
        print("Match Drawn")
        print(f"your wins:{count[0]} and computer wins:{count[1]}")
    
def want_more_input():
    try:
            y_n=input("Do you want to play again:(y/n)")
            if y_n!="y" and y_n!="n":
                raise Exception
            if y_n=="y":
                global inp
                inp=take_input()
                return inp
            else:
                print(f"final scores are:\n your wins:{count[0]} and computer wins:{count[1]}")
                if count[0]>count[1]:
                     print("You have beaten the computer")
                elif count[0]<count[1]:
                     print("Computer has beaten you")
                else:
                     print("Match drawn")
                exit()
    except Exception:
        print("input y or n")
        return want_more_input()

inp=take_input()
outp=snakewatergun(swg.index(inp.capitalize()))
print_result(outp)
while True:
    inp=want_more_input()
    outp=snakewatergun(swg.index(inp.capitalize()))
    print_result(outp)


