# (project one)
import random
print("\nIts a rock ,paper and scissor game\n")

print("0 for Rock\n")
print("1 for paper\n")
print("2 for scissor\n")

list=[0,1,2]
computer=random.randint(0,2)
print("computer chose the number\n",computer)
you=int(input("enter any no.from 0,1,2:\n"))
print("you chose this nummber:",you,"\n")

if you == 0 & computer ==0 :
        print( "game is tie ")
 
elif   you  == 1 & computer ==1   :
        print ("game is tie") 
  
elif   you  == 2 & computer ==2   :
        print ("game is tie") 
  
elif   you  == 0 & computer ==1   :
        print ("you win") 
elif   you  == 0 & computer ==2   :
        print ("you win") 

elif   you  == 1 & computer ==0   :
        print ("computer win") 
   
elif   you  == 1 & computer ==2   :
        print ("computer win") 
   
elif   you  == 2 & computer ==0   :
        print ("computer win") 
         
elif   you  == 2 & computer ==1   :
        print ("computre wni")
       
elif   you  == 2 & computer ==2   :
        print ("game is tie") 
     
else:
        print("you win")
    
    # if you>computer:
    #     print("computer wins \n")

    # else:
    #     print("you wins\n")