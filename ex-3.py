def bomber_man(x,b,c):
    test = [['O' for i in range(c)] for j in range(b)]
    """pirdapir x listze moqmedeba problematuria amitom damatebit lists 
    gamoviyenebt masshi saboloo states misagebad"""
    for i in range (b):
        for j in range (c):
            if x[i][j] == 'O':
                test[i][j] = '.'
                if i+1<b:
                    test[i+1][j] = '.'
                if j+1<c:
                    test[i][j+1] = '.'
                if i>0:
                    test[i-1][j] = '.'
                if j>0:
                    test[i][j-1] = '.'
    return test
 

x = []
y = []
n = int(input('Input the number of seconds: '))
while True:
    a = input()
    y = list(a) #
    if y:
        x.append(y)
        print(x)
    else:
        break
b=len(x)
c=len(x[0])        
if n%2==0:
    """ tu wamebis raodenoba oris namravlia teritoria sul bombebit iqneba savse"""
    result = [['O' for i in range(c)] for j in range(b)]
    for i in range(b):
            print(''.join(map(str,result[i])))#mapi outputis msgavsi shedegistvis
else:
    """bombebis sicocxlis ciklshi meordeba 2 mdgomareoba. intervali mat 
    ganmeorebas shoris aris 4 wami. shevinaxot sawyisi mdgomareoba da funqciis
    sashualebit gamoviyvanot meorec. shemdeg ciklis sashualebit davadgent romel
    mdgomareobas ekutvnis bombebi n wamze"""
    state1 = x
    state2 = bomber_man(x,b,c)
    while n-4>0:
        n-=4
    if n == 1:
        for i in range(b):
            print(''.join(map(str,state1[i])))
    elif n==3:
        for i in range(b):
            print(''.join(map(str,state2[i])))
    