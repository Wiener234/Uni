# TODO: Implementieren Sie die beiden Funktionen wie in der Aufgabenstellung beschrieben!

def func(L, x):
    """Doc"""
    list = []
    for i in range(x+1, x+11):
        if i%2 != 0 and len(list) < 5:
            list.append(i)
    return list	
def main(n): 
    list = []
    return_list = []
    sum = 0

    for i in range(20, 2*n):
        list.append(i-5)

    list_func = func(list, n)

    return_list.append(list_func)

    for i in list_func:
        sum += i

    if sum > 200:
        return_list.append("True")
    else:
        return_list.append("False")

    return_list.append(hex(n))
    return(str(return_list[0]) + str(return_list[1]) + str(return_list[2]))




