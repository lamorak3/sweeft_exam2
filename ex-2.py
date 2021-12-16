def bigger_is_greater(w):
    w = list(w)
    n = len(w)
    i = n - 1
    j = n - 1
    while i>0 and w[i-1] >= w[i]:
        i-=1
    #vpoulobt tanrigis dargvevas
    if i <= 0:
        return "no answer"
    while w[j]<=w[i-1]:
        j-=1
    #vpoulobt shoreul asos romelic naklebia w[i-1]ze da vucvlit mnishvnelobebs
    w[i-1], w[j] = w[j], w[i-1]
    
    w[i:] = w[n-1:i-1:-1]
    """aqamde gagebuli klebadi nawili w[i:] shevartialot rata minimaluri
    leqsikografiuli mnishvneloba hqondes strings"""
    return ''.join(w)
    
    
x = int(input('Input number of strings: '))
for i in range (x):
    w = input()
    print(bigger_is_greater(w))