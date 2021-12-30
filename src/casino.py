import random
from time import sleep
def driverfunc(player):
    win_amou=0
    print("\n============================================================")
    print(numls)
    print("============================================================")
    chips=100
    print("---> Choose your desired number and place your bet <---")
    x1=int(input("\n>>>>>> Player-%s enter how many numbers u wanna place bet on: "%player))
    if x1>15:
        x1=input("choice must be within 15 nums, try again: ")
    while(x1>0):
        nlsv=int(input("enter number: "))
        mlsv=int(input("enter bet: $"))
        if (chips-mlsv)<0:
            print("insufficient balance!!, your left amount:",chips,",try again entering vaild amount..") 
            mlsv=int(input("enter bet: $"))
        else:
            nls.append(nlsv)
            mls.append(mlsv)
            chips-=mlsv
            print(f"-------------> remaining bal: ${chips}")
        x1-=1
    for i in nls:
        if i==win_num:
            index=int(nls.index(i))
            win_amou+=int(mls[index]*2)
            #print("chips earn: ",win_amou)
            mls.pop(index)
        else:
            continue
    #chips-=sum(mls)
    return (chips+win_amou),win_amou   
players=int(input("enter no.of player: "))
low=int(input("enter lower limit: "))
high=int(input("enter higher limit: "))
if high<15:
    high=int(input("higher limit must be greater than 15,enter higher limit: "))
nls=[]
mls=[]
wals=[]
for i in range(1,players+1):
    print(f'\nplayer-{i} you are allocated with $100')
numls=((random.sample(range(low,high),15)))
win_num=random.choice(numls)
print("cheat: ",win_num)
player_chips_ls=[]
for i in range(1,players+1):
    player_chips_ls_var,wa=driverfunc(i)
    player_chips_ls.append(player_chips_ls_var)
    wals.append(wa)
print("\n       $$$$ WINNINGS $$$$ \n")    
for i in range(0,players):
    sleep(0.5)
    print(f"=====> player-{i+1} you won: ${wals[i]} <==============")
    print(f"your total amount: ${player_chips_ls[i]}")
    if (player_chips_ls[i]-100)>0:
        print(f"profit: ${player_chips_ls[i]-100}\n")
    else:
        print(f"you lost: ${100-player_chips_ls[i]}\n")    
    
