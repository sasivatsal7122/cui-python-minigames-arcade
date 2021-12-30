# import matplotlib.pyplot as plt
# import random
# import statistics
# i=10
# while(i>0):
#     sdl=[]
#     x1 = ((random.sample(range(0,100),30)))
#     x1.sort()
#     x2 = ((random.sample(range(100,150),30)))
#     x2.sort()
#     x1.extend(x2)
#     def yplot(y1,sdl):
#         for i in range(11):
#             var_low=random.randint(0,100)
#             var_high=random.randint(var_low,100)
#             if (var_high-var_high)<5:
#                 var_high+=5
#             y_var = ((random.sample(range(var_low,var_high),5)))
#             y_var.sort()
#             a=min(y_var)
#             b=max(y_var)
#             sdl.append(a)
#             sdl.append(b)
#             y1+=y_var
#         return y1
#     y1 = ((random.sample(range(0,100),5)))
#     y1.sort()
#     a=min(y1)
#     b=max(y1)
#     sdl.append(a)
#     sdl.append(b)
#     yplot(y1,sdl)
#     print(f"{i}) Standard Deviation of sample is %s"% (statistics.stdev(sdl)))
#     plt.plot(x1, y1)
#     plt.xlabel('x - axis')
#     plt.ylabel('y - axis')
#     plt.title('Your stock performance')
#     plt.show()
#     i-=1


import random
print("======================================================")
print("--welcome to hand kriket or more like binary kriket--")
print("======================================================\n")
c="bowl"
def bat_bowl(var_name,ini_num,target):
    print(f"\n>>>>>>>>>>>>> ! {ini_num} innings !<<<<<<<<<<<\n")
    if ini_num=="second":
        print(f"------->Target: {target+1}<-------\n")
    sys_chose=0
    user_skore=0
    syst_skore=0
    user_chose=int(input("enter runs between 1-9: "))
    sys_chose=random.randint(1,9)
    print(f"                              {sys_chose}: computer choice <<<<<<")
    if sys_chose==user_chose:
        print(f"{var_name} duck out")
    else:
        while((sys_chose!=user_chose) or (user_skore>=int(target)) or (syst_skore>=int(target))):
            user_chose=int(input(("enter runs between 1-9: ")))
            if int(user_chose)>9:
                user_chose=input(("error!, enter runs between 1-9: "))
            sys_chose=random.randint(1,9)
            if sys_chose!=user_chose:
                print(f"                              {sys_chose}: computer choice <<<<<<")
                user_skore+=user_chose
                syst_skore+=sys_chose
            else:
                print(f"                              {sys_chose}: computer choice <<<<<<")
                print("\n=====================================")
                print(f"-----------{var_name} out-------------")
                print("======================================")
            user_skore+=user_chose
            syst_skore+=sys_chose
    if var_name=="computer":
        print(f"\n----->{var_name} score is : {sys_skore}<-----")
    else:
         print(f"\n----->{var_name} score is : {sys_skore}<-----")
    return user_skore,syst_skore
toss=input(("choose toss--> 'h' for head or 't' tails : "))
win_toss=random.randint(1,2)
if (win_toss==1 and toss=='h') or (win_toss==2 and toss=='t'):
    user_choice=input("you won the toss--> 'b' for bat or 'bw' for bowl: " )
    if user_choice=="b":
        u_skore,sys_skore=bat_bowl("you're","first",9999)
        sys_skore,u_skore=bat_bowl("computer","second",u_skore)
    else:
        sys_skore,u_skore=bat_bowl("computer","first",9999)
        u_skore,sys_skore=bat_bowl("you're","second",sys_skore)
else:
    sys_choice=random.randint(1,2)
    if sys_choice==1:
        c="bat"
        print(f"computer won the toss--> computer chooses to {c}")
        sys_skore,u_skore=bat_bowl("computer","first",9999)
        u_skore,sys_skore=bat_bowl("you're","second",sys_skore)
    else:
        print(f"computer won the toss--> computer chooses to {c}")
        u_skore,sys_skore=bat_bowl("you're","first",9999)
        sys_skore,u_skore=bat_bowl("computer","second",u_skore)
if u_skore>sys_skore:
    print("============== ! stats ! ============")
    print(f"$ you're score is {u_skore}")
    print(f"$ computer score is {sys_skore}")
    print(f"$ you won the match by {u_skore-sys_skore} runs")
else:
    print(f"$ you're score is {u_skore}")
    print(f"$ computer score is {sys_skore}")
    print(f"$ computer won the match by {sys_skore-u_skore} runs")







