import random
#Schere schlägt Papier
#Papier schlägt Stein
#Stein schlägt Schere
#Schere Stein Papier
#insgesamt 9 optionen
x=random.randint(1,3)
i=input('Bitte gebe für Schere 1 an,für Papier 2 und für Stein 3.Wenn du aufhören willst schreibe STOP.')

print('Wilkommen zu Schere Stein Papier.')

if i=='1'and x==2:
    print('Glückwunsch dein Gegner hatte Papier')
elif i=='1'and x==1:
    print('Unentschieden dein Gegner hatte Schere')    
elif i=='1'and x==3:
    print('Leider Verloren dein Gegner hatte Stein')
elif i=='2'and x==1:
    print('Leider Verloren dei Gegner hatte Schere')
elif i=='2'and x==2:
    print('Unentschieden dein Gegner hatte Papier')
elif i=='2'and x==3:
    print('Glückwunsch dein Gegner hatte Stein')
elif i=='3'and x==1:
    print('Glückwunsch dein Gegner hatte Schere')
elif i=='3'and x==2:
    print('Leider Verloren dein Gegner hatte Papier')
elif i=='3'and x==3:
    print('Unentschieden dein Gegner hatte Stein')  
else:
    print('gebe bitte eine richtige Zahl oder stop ein')
        
    