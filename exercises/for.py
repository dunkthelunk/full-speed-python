def hasDuplicates(list):
    for e1 in list:
        for e2 in list[list.index(e1)+1 : ]:
            if e1 == e2 : return True
    return False

def max(list):
    max = list[0]
    for i in range(len(list)):
        if list[i] > max : max = list[i]
    return max
def maxWithIndex(list):
    max = [list[0], 0]
    for i in range(len(list)):
        if list[i] > max[0] :
            max[0] = list[i]
            max[1] = i
    return max
