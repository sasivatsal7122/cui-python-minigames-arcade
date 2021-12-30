import random
players=int(input("enter no.of players: "))
c=1
print("-----------------------------------------")
print(".......Intiating Game for %s player......."%players)
print("-----------------------------------------")
low=int(input("enter lower limit: "))
high=int(input("enter higher limit: "))
numls=[]
rand=random.randint(low,high)
numls.append(rand)
guesslst=[]
user_input=int(input("guess a number between %s and %d:"%(low,high)))
while user_input!=rand:
    if c==(players*2):
        c=-1
        rand=random.randint(low,high)
        numls.append(rand)
        guesslst.append('new')
        print("---------Number changed------------")
    elif(user_input>rand):
        print("\nyour guess is just a bit higher")
        guesslst.append(user_input)
        user_input=int(input("try again: "))
    else:
        print("\noops! your guess is less than expected")
        guesslst.append(user_input)
        user_input=int(input("try again: "))
    c+=1    
print("\ncongratulations u guessed it right!!!")
if ((len(guesslst)+1)%players)==0:
    x=players
else:
    x=(len(guesslst)+1)%players
print("-----------------------------------------")
print("..............player %s won............."%(x))
print("-----------------------------------------")
print("\nit took",len(guesslst)+1,"guess to make a right choice")
print("\npreviously guessed numbers before guessing %i are:"%rand)
print("choosen numbers: ",numls)
print(guesslst)        