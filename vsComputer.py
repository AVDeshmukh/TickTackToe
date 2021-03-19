

print('1 |2 | 3')
print("--+--+--")
print('4 |5 | 6')
print("--+--+--")
print('7 |8 | 9')


print("""
	If you want your mark at 6
	then simply press 6
	""")

A=[' ',' ',' ',' ',' ',' ',' ',' ',' ']


 
def print1():
 print(A[0],'|',A[1],'|',A[2])
 print("--+---+--")
 print(A[3],'|',A[4],'|',A[5])
 print("--+---+--")
 print(A[6],'|',A[7],'|',A[8])
 print("         ")

def check():
 if A[0]==A[1]==A[2]=='O'or A[3]==A[4]==A[5]=='O' or A[6]==A[7]==A[8]=='O' or A[0]==A[3]==A[6]=='O' or A[1]==A[4]==A[7]=='O' or A[2]==A[5]==A[8]=='O' or A[0]==A[4]==A[8]=='O' or A[2]==A[4]==A[6]=='O':
  print("Player 1 Wins")
  return 1
 elif A[0]==A[1]==A[2]=='X'or A[3]==A[4]==A[5]=='X' or A[6]==A[7]==A[8]=='X' or A[0]==A[3]==A[6]=='X' or A[1]==A[4]==A[7]=='X' or A[2]==A[5]==A[8]=='X' or A[0]==A[4]==A[8]=='X' or A[2]==A[4]==A[6]=='X':
  print("Player 2 Wins")
  return 1
input_no=0
player=1
last_check=0
while True:
 print1()
 last_check=check()
 if input_no == 9:
  print("Its a tie")
  break
 elif last_check == 1:
  break
 Test=[1,2,3,4,5,6,7,8,9]
 while True:
  if player==1:   
   print("Player 1")
   m=int(input()) 
   if m<10:
    A[m-1]='O'
    Test.remove(m)
    player=2
    break
  else:
   print("player 2")
   import random
   n=random.choice(Test)
   Test.remove(n)
   if n<10:
    A[n-1]='X'
    player=1
    break
 input_no+=1
