import random
print("[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]")
print("        TEST YOUR LUCK!!!      ")
print("[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]\n")
players=int(input("enter how many player: "))
print("-----------------------------------------")
print("........Game intiating for %s player......"%players)
print("-----------------------------------------")
player1=[]
player2=[]
player3=[]
player4=[]
x1=0
x2=0
x3=0
x4=0
low=random.randint(0,1000)
high2=random.randint(low,1000000)
high=random.randint(low,high2)
lucky_num=random.randint(low,high)
count=0
while lucky_num not in (player1 or player2 or player3 or player4):
    for i in range(1,players*10+1):
        if i<11 and x1<1:
            player1.append(random.randint(low,high))
        if (i>10 and i<21) and x2<1:
            player2.append(random.randint(low,high))
        if (i>20 and i<31) and x3<1:
            player3.append(random.randint(low,high))
        elif i>40 and x4<1:
            player4.append(random.randint(low,high))
    if lucky_num in player1:
        x1+=1
    else:
        player1=[]
    if lucky_num in player2:
        x2+=1
    else:
        player2=[]
    if lucky_num in player3:
        x3+=1
    else:
        player3=[]
    if lucky_num in player4:
        x4+=1
    else:
        player4=[]
    count+=1
print("\n=========================================")
print(f"----! lucky number is: {lucky_num} !----")
print("===========================================")
if lucky_num in player1:
    print("---------------------------------------------------------------------------------")
    print(">>>> Congratulations player 1, you won points %s"%(count+player1.index(lucky_num)))
    print("-------------------------------------------------------------------------------\n")
    print("$--> your list:",player1)
elif lucky_num in player2:
    print("---------------------------------------------------------------------------------")
    print(">>>> Congratulations player 2, you won points %s"%(count+player2.index(lucky_num)))
    print("-------------------------------------------------------------------------------\n")
    print("$--> your list:",player2)
elif lucky_num in player3:
    print("---------------------------------------------------------------------------------")
    print(">>>> Congratulations player 3, you won points %s"%(count+player3.index(lucky_num)))
    print("-------------------------------------------------------------------------------\n")
    print("$--> your list:",player3)
elif lucky_num in player4:
    print("---------------------------------------------------------------------------------")
    print(">>>> Congratulations player 4, you won points %s"%(count+player4.index(lucky_num)))
    print("-------------------------------------------------------------------------------\n")
    print("$--> your list:",player4)
print("\n==========TERIMINATING===============")