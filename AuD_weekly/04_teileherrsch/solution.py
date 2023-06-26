# TODO: Implementieren Sie die Funktionen wie in der Aufgabenstellung beschrieben! 
# Verändern Sie die gegebenen Funktionsschnittstellen nicht und definieren Sie keine weiteren Funktionen

def lRandmin(L, low, high):
    if low == high:
        #return 0
        return L[low]

    _list = lRandmin(L, low+1, high)

    print("L: ", _list)
    sum = 0
    for i in range(high, low, -1):
        sum += L[i]
        print("sum: ", sum, "list: ", _list)

    if sum < _list:
        return sum

    elif L[low]<_list:
        return L[low]

    elif _list + L[low] < _list and sum == _list:
        return _list + L[low]

    return _list

def rRandmin(L, low, high):
    if low == high:
        #return 0
        return L[high]

    _list = rRandmin(L, low, high-1)

    sum = 0
    for i in range(low, high+1):
        sum += L[i]
        print("sum: ", sum, "list: ", _list)


    print("R: ", _list)

    if sum < _list:
        return sum

    elif L[high]<_list:
        return L[high]

    elif _list + L[high] < _list and sum == _list: #or _list + L[high] < _list and sum :
        return _list + L[high]

    return _list

def minTeilsumme_TeileUndHerrsche(L, low, high):
    mid = high//2
    _leftList = lRandmin(L, low, mid)

    _rightList = rRandmin(L, mid+1, high)

    print("leftList: ", _leftList)
    print("rightList: ", _rightList)

    _bothList = _leftList + _rightList
    return min(_leftList, _rightList, _bothList)



def minTeilsumme(L):
    return minTeilsumme_TeileUndHerrsche(L, 0,len(L)-1)


#L = [2, -1, 0, -6, -2, 2, 7]
#T = [-1, 4, 2, -3, 7, -3, 0, -2, 8]
#R = [3,2,1,5,1]
F = [-10, 27, -50, 28, -15, 99999,-26, -10, 20, -6, 999999,-17, 7, -2, 6, -30, 150, 17, -18]
print("Ergebnis: ", minTeilsumme(F))
#lRandmin([2, -1, 0, -6, -2, 2, 7], 0, 4)
#rRandmin([2, -1, 0, -6, -2, 2, 7], 3, 6)
