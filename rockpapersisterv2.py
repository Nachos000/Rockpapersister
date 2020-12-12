#random numbers/letters/choices
import random
#Rockpaperscissor: 9 options
#Rock<Paper<Scissor 
#< >

x=random.randint(1,3)#random number

pointthreeyou=0#pointthreeyou=2 you win  
pointthreecomputer=0#pointthreecomputer=2 computer wins

#welcome
print('Welcome to Ultimat Rock Paper Scissor')
print('Here you can choose between many diferent gamemodes')
while True:#flowchart
    print('You can play BEST OF 10 (Write 1)')#game 1
    print('Or you can play just 1 GAME (Write 2)')#game 2
    print('Or you can try to WIN 2 TIMES in a row before your enemy does it')#game3
    i=input('what du you want to play?')
    if i=='1':#game1
        print('This Game is not finished')
    elif i=='2':##############################################################################################GAME2
        print('Welcome to Rock Paper Scissor.')
        i=input('Please write 1 for scissor, 2 for paper and 3 for rock.If you want to stop write(stop).')#Rock(3)<Paper(2)<Scissor(1)
        if i=='1'and x==2:
            print('Congratulations your enemy has paper!')
        elif i=='1'and x==1:
            print('Draw your enemy has scissor!')    
        elif i=='1'and x==3:
            print('Sorry you lost your enemy has stone!')
        elif i=='2'and x==1:
            print('Sorry you lost your enemy has paper!')
        elif i=='2'and x==2:
            print('Draw your enemy has paper!')
        elif i=='2'and x==3:
            print('Congratulations your enemy has stone!')
        elif i=='3'and x==1:
            print('Congratulations your enemy has scissor!')
        elif i=='3'and x==2:
            print('Sorry you lost your enemy has paper!')
        elif i=='3'and x==3:
            print('Draw your enemy has stone!')  
        else:
            print('Write a right number or write stop:')
            print('')
    elif i=='stop':
        break
    elif i=='3':###########################################################################################################GAME3
        while True:
            print('Welcome to Rock Paper Scissor.')
            i=input('Please write 1 for scissor, 2 for paper and 3 for rock.If you want to stop write(stop).')#Rock(3)<Paper(2)<Scissor(1)
            if i=='1'and x==2:
                print('Congratulations your enemy has paper!')
                pointthreeyou=pointthreeyou+1
                if pointthreeyou==2:#you won
                    break
                if pointthreecomputer==1:
                    pointthreecomputer=pointthreecomputer-1
                print('you have'+ str(pointthreeyou) +'points')    
            elif i=='1'and x==1:
                print('Draw your enemy has scissor!')
                print('you have'+ str(pointthreeyou) +'points')
            elif i=='1'and x==3:
                print('Sorry you lost your enemy has stone!')
                pointthreecomputer=pointthreecomputer+1
                if pointthreecomputer==2:#you lose
                    print('you lost really hard,LOSER')
                    break
                if pointthreeyou==1:
                    pointthreeyou=pointthreeyou-1
                print('you have'+ str(pointthreeyou) +'points')    
            elif i=='2'and x==1:
                print('Sorry you lost your enemy has paper!')
                pointthreecomputer=pointthreecomputer+1
                if pointthreecomputer==2:#you lose
                    print('you lost really hard,LOSER')
                    break
                if pointthreeyou==1:
                    pointthreeyou=pointthreeyou-1
                print('you have'+ str(pointthreeyou) +'points')    
            elif i=='2'and x==2:
                print('Draw your enemy has paper!')
                print('you have'+ str(pointthreeyou) +'points')
            elif i=='2'and x==3:
                print('Congratulations your enemy has stone!')
                pointthreeyou=pointthreeyou+1
                if pointthreeyou==2:#you won
                    break
                if pointthreecomputer==1:
                    pointthreecomputer=pointthreecomputer-1
                print('you have'+ str(pointthreeyou) +'points')    
            elif i=='3'and x==1:
                print('Congratulations your enemy has scissor!')
                pointthreeyou=pointthreeyou+1
                if pointthreeyou==2:#you won
                    break
                if pointthreecomputer==1:
                    pointthreecomputer=pointthreecomputer-1
                print('you have'+ str(pointthreeyou) +'points')    
            elif i=='3'and x==2:
                print('Sorry you lost your enemy has paper!')
                pointthreecomputer=pointthreecomputer+1
                if pointthreecomputer==2:#you lose
                    print('you lost really hard,LOSER')
                    break
                if pointthreeyou==1:
                    pointthreeyou=pointthreeyou-1
                print('you have'+ str(pointthreeyou) +'points')    
            elif i=='3'and x==3:
                print('Draw your enemy has stone!')
                print('you have'+ str(pointthreeyou) +'points')
            else:#if you want to stop playing
                print('Write a right number or write stop:')
                print('')
            
    else:#if you write something wrong
        print('Please write one of the following options:')
        print('')
        



