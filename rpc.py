
import random
u=input("Enter one ,r for Rock,s for Scissors,p for Papers")
c=random.choice(['r','s','p'])
print("User choose ",c)
def f(u,c):
    #r>s,s>p,p>r
    if (u=='r' and c=='s')or(u=='s' and c=='p')or(u=='p' and c=='r'):
        return True
    return False
if(u==c):
    print("It's a draw")
else:
    if(f(u,c)):
        print("You won")
    else:
        print("You lost")

