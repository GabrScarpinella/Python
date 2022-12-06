import time
import random

#Rock,paper,scissors

pchoices=[1,2,3,4]  #Possible choices:1=rock,2=paper,3=scissors,4=give up;
victories=0         #Number of times player won
defeats=0           #Number of times player lost
draws=0             #Total number of draws
total=0             #Total games played
osurrend=0          #Number of times player's opponent surrendered
psurrend=0          #Number of times player surrendered

while True:
    mchoi=int(input("\n1-Game\n2-Statistics\n"))
    while True:
        if mchoi==1:
            pchoi=int(input("\n1-Rock\n2-Paper\n3-Scissors\n4-Give Up\n"))
            ochoi=random.choice(pchoices)
            if pchoi==4 or ochoi==4:                #Someone surrenders
                if pchoi==4 and ochoi!=4:           #Player surrenders
                    print("You surrendered.")
                    mchoi=0
                    psurrend=psurrend+1
                elif pchoi!=4 and ochoi==4:         #Opponent surrenders
                    print("Your opponent surrendered.")
                    mchoi=0
                    osurrend=osurrend+1
                else:                               #Both surrender
                    print("You both surrendered.")
                    mchoi=0
                    osurrend=osurrend+1
                    psurrend=psurrend+1
                break
            if pchoi==ochoi+1 or pchoi==ochoi-2:    #Player wins
                print("You won this round.")
                victories=victories+1
            elif ochoi==pchoi+1 or ochoi==pchoi-2:  #Player loses
                print("You lost this round.")
                defeats=defeats+1
            elif pchoi==ochoi:                      #Draw occurs
                print("This round was a draw")
                draws=draws+1

        elif mchoi==2:
                print(f"\n    Statistics\n\n    Victories:{victories}")
                print(f"    Defeats:{defeats}\n    Draws:{draws}")
                print(f"    Total played:{total}\n    Times you surrendered:{psurrend}")
                print(f"    Times your opponent surrendered:{osurrend}\n")
                time.sleep(6)
                mchoi=0