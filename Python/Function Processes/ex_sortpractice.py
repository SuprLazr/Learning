def ascendSort(list):
    smallest = None
    ascended = []
    verifyPos = []
    while len(ascended) < len(list):
        y = -1
        for i in list:
            y+=1
            if y not in verifyPos:
                if smallest is None:
                    smallest=i
                    z=y
                elif i <= smallest:  
                    smallest=i
                    z=y
        verifyPos.append(z)
        ascended.append(smallest)
        smallest = None
    return ascended

preSort = [-999,32,-42,-50,47,-2,-2]
print(ascendSort(preSort))