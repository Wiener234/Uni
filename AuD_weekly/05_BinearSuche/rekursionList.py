L = [2,-1,0,-6,-2,2,7]
T = [-10,27,-50,28,-15,-26,-10,20,-6,-17,7,-2,6,-30,17,-18]


def leftList(L, low, high):

    if low == high:
        return L[low]

    _list = leftList(L, low+1, high)

    if _list + L[low] < _list:
        return _list + L[low]

    return _list

def rightList(L, low, high):
    if low == high:
        return L[low]

    _list = rightList(L, low, high-1)
    if _list + L[high] < _list:
        return _list + L[high]

    return _list

def list(L, low, high):
    mid = (high)//2
    _leftList = leftList(L, low, mid)
    #print(_leftList)
    _rightList = rightList(L, mid+1, high)
    #print(_rightList)

    _bothList = _leftList + _rightList

    return min(_leftList, _rightList, _bothList)

print(list(L, 0, len(L)-1))
