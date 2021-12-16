n = int(input('Input number of strings: '))
lst = []
dc = {}
for i in range (0,n):
    x = input()
    # tu ar aris dictionaryshi elementi aseti gasagebit sheqmnas is
    if x not in dc: 
        dc[x] = 1
    else:
        dc[x] += 1
    #list-shi sheinaxos mxolod unikaluri sting-ebi
    if x not in lst[:i]: 
        lst += [x,]
print(len(dc))
#viyenebt string comprehensions pasuxis gamosatanad
print(' '.join([str(dc[i]) for i in lst]))
