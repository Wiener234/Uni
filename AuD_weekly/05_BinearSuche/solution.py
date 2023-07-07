def lRandmin(L,i,j):
    # pre: 0 <= i <= j < len(L)
    # post: maximale Summe einer linken Randfolge
    # der Teilfolge von i bis j (einschließlich i,j)
    min = L[i]
    sum = 0
    for k in range(i,j+1): # k = i, i+1, ..., j
        sum += L[k]
        if (sum < min):
            min = sum
    return min

def rRandmin(L,i,j):
    # pre: 0 <= i <= j < len(L)
    # post: maximale Summe einer rechten Randfolge
    # der Teilfolge von i bis j (einschließlich i,j)
    min = L[j]
    sum = 0
    for k in range(j,i-1,-1): # k = j, j-1, ..., i
        sum += L[k]
        if (sum < min):
            min = sum
    return min

def minTeilsumme_TeileUndHerrsche(L,i,j):
    # pre: 0 <= i <= j < len(L)
    # post: maximale Teilsumme der Teilfolge
    # von i bis j (einschließlich i,j)
    if (i == j): # nur ein Element
        return L[i]
    else:
        m = (i + j)//2 # Mitte von L
        maxLinks = minTeilsumme_TeileUndHerrsche(L,i,m)
        maxRechts = minTeilsumme_TeileUndHerrsche(L,m+1,j)
        maxMisch = rRandmin(L,i,m) + lRandmin(L,m+1,j)
    return min(maxLinks, maxRechts, maxMisch)

def minTeilsumme(L):
    # pre: L ist nicht leer
    # post: maximale Teilsumme von L
    return minTeilsumme_TeileUndHerrsche(L,0,len(L)-1)

#print(maxTeilsumme_rek([1,3,4,-6,5,-7]))
