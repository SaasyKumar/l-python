import random
#Hand Cricket 
# def toss:
#     if s%2==0:
#         t=2
#     if u_t==t:
#         print(You won )
    
print("Rules of hand cricket\n\t\tBatting\n*You can choose a number between 0 to 6 and it denotes runs\n*your scores will summed until you got out\n*if you and computer got same number you are out")
#Toss
# u_t=input("\t\tToss\nOdd('1')or Even('2')? ")
u=int(input("Start\n"))
c=random.randint(0,6)
if u in range(0,7):
    pass
else:
    print("No cheating")
    u=0
s=0
while(u!=c):
    s+=u
    u=int(input(f"Score: {s} next "))
    c=random.randint(3,6)
    if u in range(0,7):
        pass
    else:
        print("No cheating")
        s-=u
print(f"☝Out! Target: {s}")
print("\tYour turn to Bowling")
u=int(input("Start\n"))
c=random.randint(0,6)
s_c=0
while(u!=c):
    s_c+=c
    if s>=s_c and s-s_c<15:
        print(f"Comp Need {s-s_c+1} runs to win")
    elif s_c>s:break
    u=int(input(f"Score: {s_c} next "))
    c=random.randint(1,6)
else:print("Out! ☝")
if s_c>s:print("\tYou lose!Computer won 😎")
elif s_c==s:print("\t🤝Match Draw") 
else: print(f"\t🙌You won by {s-s_c} runs")
