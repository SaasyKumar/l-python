import random
from webbrowser import Elinks
def emoji(x):
    if x=='r':print("✊",end='\t')
    elif x=='p':print("📃",end='\t')
    else:print("✂",end='\t')
def wincal(u,c):
    #r>s,s>p,p>r
    if (u=='r' and c=='s') or (u=='s' and c=='p') or (u=='p' and c=='r'):return 'w'
    elif u==c:return 't'
    return 'l'

user=input("Choose ('r' for) Rock or Paper('p') or Scissor('s') ")
print("You",end='\t')
emoji(user)
computer=random.choice(['r','p','s'])
emoji(computer)
print(f"computer")
who_wins= wincal(user,computer)
if who_wins =='w':
    print("You won")
elif who_wins=='t':print("It's a tie")
else:print("You Lose")
