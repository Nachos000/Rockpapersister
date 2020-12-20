#random numbers/letters/choices
import random
#Rockpaperscissor: 9 options
#Rock<Paper<Scissor 

#important for all three games
x=random.randint(1,3)#random number

#important for game 1
pointoneyou=0#pointsoneyou=3 you win
pointonecomputer=0#piontsonecomputer=3 you win
rounds=0#best of 5 doesnt has more than 5 rounds but at least 3

#important for game 3
pointthreeyou=0#pointthreeyou=2 you win  
pointthreecomputer=0#pointthreecomputer=2 computer wins

#welcome
print('Welcome to Ultimat Rock Paper Scissor')
print('Here you can choose between many diferent gamemodes')
while True:#flowchart
    print('You can play BEST OF 5 (Write 1)')#game 1
    print('Or you can play just 1 GAME (Write 2)')#game 2
    print('Or you can try to WIN 2 TIMES in a row before your enemy does it')#game3
    i=input('what du you want to play?  ')
    if i=='1':#########################################################################################################################game1
        while True:
            print('Welcome to Rock Paper Scissor.')
            i=input('Please write 1(Scissor),2(Paper) or 3(Rock).If you want to stop write(stop).  ')#Rock(3)<Paper(2)<Scissor(1)
            if i=='1'and x==2:
                print('Congratulations your enemy has paper!')###YOU WIN
                pointoneyou=pointoneyou+1
                print('you have  '+str(pointoneyou)+'  points')
                print('the computer has  '+str(pointonecomputer)+'  points')
                rounds=rounds+1
                print('It is Round:  '+str(rounds))
                if pointoneyou==3:
                    print('Congratulations you have a lot of luck')
                    print('')
                    break
                if rounds==5:#Its Round 5 and nobody has 3 points
                    if pointoneyou<pointonecomputer:#Computer has more points
                        print('Haha close but whatever...LOSER')
                        print('')
                        break
                    elif pointoneyou>pointonecomputer:#You have more points
                        print('Uh lala that was close, but Win is Win')
                        print('')
                        break
            elif i=='1'and x==1:
                print('Draw your enemy has scissor!')###DRAW
                print('you have  '+str(pointoneyou)+'  points')
                print('the computer has  '+str(pointonecomputer)+'  points')
                rounds=rounds+1
                print('It is Round:  '+str(rounds))
            elif i=='1'and x==3:
                print('Sorry you lost your enemy has stone!')##YOU LOSE
                pointonecomputer=pointonecomputer+1
                print('you have  '+str(pointoneyou)+'   points')
                print('the computer has  '+str(pointonecomputer)+'  points')
                rounds=rounds+1
                print('It is Round:  '+str(rounds))
                if pointonecomputer==3:
                    print('You really dont know the word LUCK!')
                    print('')
                    break
                if rounds==5:#Its Round 5 and nobody has 3 points
                    if pointoneyou<pointonecomputer:#Computer has more points
                        print('Haha close but whatever...LOSER')
                        print('')
                        break
                    elif pointoneyou>pointonecomputer:#You have more points
                        print('Uh lala that was close, but Win is Win')
                        print('')
                        break
            elif i=='2'and x==1:
                print('Sorry you lost your enemy has paper!')###YOU LOSE
                pointonecomputer=pointonecomputer+1
                print('you have  '+str(pointoneyou)+'  points')
                print('the computer has  '+str(pointonecomputer)+'  points')
                rounds=rounds+1
                print('It is Round:  '+str(rounds))
                if pointonecomputer==3:
                    print('You really dont know the word LUCK!')
                    print('')
                    break
                if rounds==5:#Its Round 5 and nobody has 3 points
                    if pointoneyou<pointonecomputer:#Computer has more points
                        print('Haha close but whatever...LOSER')
                        print('')
                        break
                    elif pointoneyou>pointonecomputer:#You have more points
                        print('Uh lala that was close, but Win is Win')
                        print('')
                        break
            elif i=='2'and x==2:
                print('Draw your enemy has paper!')###DRAW
                print('you have  '+str(pointoneyou)+'  points')
                print('the computer has  '+str(pointonecomputer)+'  points')
                rounds=rounds+1
                print('It is Round:  '+str(rounds))
                if rounds==5:#Its Round 5 and nobody has 3 points
                    if pointoneyou<pointonecomputer:#Computer has more points
                        print('Haha close but whatever...LOSER')
                        print('')
                        break
                    elif pointoneyou>pointonecomputer:#You have more points
                        print('Uh lala that was close, but Win is Win')
                        print('')
                        break
            elif i=='2'and x==3:
                print('Congratulations your enemy has stone!')###YOU WIN
                pointoneyou=pointoneyou+1
                print('you have  '+str(pointoneyou)+'  points')
                print('the computer has  '+str(pointonecomputer)+'  points')
                rounds=rounds+1
                print('It is Round:  '+str(rounds))
                if pointoneyou==3:
                    print('Congratulations you have a lot of luck')
                    print('')
                    break
                if rounds==5:#Its Round 5 and nobody has 3 points
                    if pointoneyou<pointonecomputer:#Computer has more points
                        print('Haha close but whatever...LOSER')
                        print('')
                        break
                    elif pointoneyou>pointonecomputer:#You have more points
                        print('Uh lala that was close, but Win is Win')
                        print('')
                        break
            elif i=='3'and x==1:
                print('Congratulations your enemy has scissor!')###YOU WIN
                pointoneyou=pointoneyou+1
                print('you have  '+str(pointoneyou)+'  points')
                print('the computer has  '+str(pointonecomputer)+'  points')
                rounds=rounds+1
                print('It is Round:  '+str(rounds))
                if pointoneyou==3:
                    print('Congratulations you have a lot of luck')
                    print('')
                    break
                if rounds==5:#Its Round 5 and nobody has 3 points
                    if pointoneyou<pointonecomputer:#Computer has more points
                        print('Haha close but whatever...LOSER')
                        print('')
                        break
                    elif pointoneyou>pointonecomputer:#You have more points
                        print('Uh lala that was close, but Win is Win')
                        print('')
                        break
            elif i=='3'and x==2:
                print('Sorry you lost your enemy has paper!')###YOU LOSE
                pointonecomputer=pointonecomputer+1
                print('you have  '+str(pointoneyou)+'  points')
                print('the computer has  '+str(pointonecomputer)+'  points')
                rounds=rounds+1
                print('It is Round:  '+str(rounds))
                if pointonecomputer==3:
                    print('You really dont know the word LUCK!')
                    print('')
                    break
                if rounds==5:#Its Round 5 and nobody has 3 points
                    if pointoneyou<pointonecomputer:#Computer has more points
                        print('Haha close but whatever...LOSER')
                        print('')
                        break
                    elif pointoneyou>pointonecomputer:#You have more points
                        print('Uh lala that was close, but Win is Win')
                        print('')
                        break
            elif i=='3'and x==3:
                print('Draw your enemy has stone!')###DRAW
                print('you have  '+str(pointoneyou)+'  points')
                print('the computer has  '+str(pointonecomputer)+'  points')
                rounds=rounds+1
                print('It is Round:  '+str(rounds))
                if rounds==5:#Its Round 5 and nobody has 3 points
                    if pointoneyou<pointonecomputer:#Computer has more points
                        print('Haha close but whatever...LOSER')
                        print('')
                        break
                    elif pointoneyou>pointonecomputer:#You have more points
                        print('Uh lala that was close, but Win is Win')
                        print('')
                        break
            else:
                print('Write a right number or write stop:')
                print('')
    elif i=='2':#####################################################################################################################GAME2
        print('Welcome to Rock Paper Scissor.')
        i=input('Please write 1(Scissor),2(Paper) or 3(Rock).If you want to stop write(stop).  ')#Rock(3)<Paper(2)<Scissor(1)
        if i=='1'and x==2:
            print('')
            print('Congratulations your enemy has paper!')
            print('')
        elif i=='1'and x==1:
            print('')
            print('Draw your enemy has scissor!')
            print('')
        elif i=='1'and x==3:
            print('')
            print('Sorry you lost your enemy has stone!')
            print('')
        elif i=='2'and x==1:
            print('')
            print('Sorry you lost your enemy has paper!')
            print('')
        elif i=='2'and x==2:
            print('')
            print('Draw your enemy has paper!')
            print('')
        elif i=='2'and x==3:
            print('')
            print('Congratulations your enemy has stone!')
            print('')
        elif i=='3'and x==1:
            print('')
            print('Congratulations your enemy has scissor!')
            print('')
        elif i=='3'and x==2:
            print('')
            print('Sorry you lost your enemy has paper!')
            print('')
        elif i=='3'and x==3:
            print('')
            print('Draw your enemy has stone!')
            print('')
        else:
            print('')
            print('Write a right number or write stop:')
            print('')
    elif i=='stop':
        break
    elif i=='3':###########################################################################################################GAME3
        while True:
            print('Welcome to Rock Paper Scissor.')
            i=input('Please write 1(Scissor),2(Paper) or 3(Rock).If you want to stop write(stop).  ')#Rock(3)<Paper(2)<Scissor(1)
            if i=='1'and x==2:
                print('Congratulations your enemy has paper!')
                pointthreeyou=pointthreeyou+1
                if pointthreeyou==2:#you won
                    break
                if pointthreecomputer==1:
                    pointthreecomputer=pointthreecomputer-1
                print('you won  '+ str(pointthreeyou) +'  times in a row')    
            elif i=='1'and x==1:
                print('Draw your enemy has scissor!')
                print('you won  '+ str(pointthreeyou) +'  times in a row')
            elif i=='1'and x==3:
                print('Sorry you lost your enemy has stone!')
                pointthreecomputer=pointthreecomputer+1
                if pointthreecomputer==2:#you lose
                    print('you lost really hard,LOSER')
                    break
                if pointthreeyou==1:
                    pointthreeyou=pointthreeyou-1
                print('you won  '+ str(pointthreeyou) +'  times in a row')    
            elif i=='2'and x==1:
                print('Sorry you lost your enemy has paper!')
                pointthreecomputer=pointthreecomputer+1
                if pointthreecomputer==2:#you lose
                    print('you lost really hard,LOSER')
                    break
                if pointthreeyou==1:
                    pointthreeyou=pointthreeyou-1
                print('you won  '+ str(pointthreeyou) +'  times in a row')    
            elif i=='2'and x==2:
                print('Draw your enemy has paper!')
                print('you won  '+ str(pointthreeyou) +'  times in a row')
            elif i=='2'and x==3:
                print('Congratulations your enemy has stone!')
                pointthreeyou=pointthreeyou+1
                if pointthreeyou==2:#you won
                    break
                if pointthreecomputer==1:
                    pointthreecomputer=pointthreecomputer-1
                print('you won  '+ str(pointthreeyou) +'  times in a row')    
            elif i=='3'and x==1:
                print('Congratulations your enemy has scissor!')
                pointthreeyou=pointthreeyou+1
                if pointthreeyou==2:#you won
                    break
                if pointthreecomputer==1:
                    pointthreecomputer=pointthreecomputer-1
                print('you won  '+ str(pointthreeyou) +'  times in a row')    
            elif i=='3'and x==2:
                print('Sorry you lost your enemy has paper!')
                pointthreecomputer=pointthreecomputer+1
                if pointthreecomputer==2:#you lose
                    print('you lost really hard,LOSER')
                    break
                if pointthreeyou==1:
                    pointthreeyou=pointthreeyou-1
                print('you won  '+ str(pointthreeyou) +'  times in a row')    
            elif i=='3'and x==3:
                print('Draw your enemy has stone!')
                print('you won  '+ str(pointthreeyou) +'  times in a row')
            else:#if you want to stop playing
                print('Write a right number or write stop:')
                print('')
            
    else:#if you write something wrong
        print('Please write one of the following options:')
        print('')
        



