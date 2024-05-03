from itertools import product
import numpy as np

# definition of the 5 wheels
wheel_1 = [(15, None, 8, None, 3, None, 6, None, 10, None, 7, None)]

wheel_2 = [(6,    17, 7,    3, None, 6, None, 11, 11, 6, 11, None),
           (12, None, 4, None, 7, 15, None, None, 14, None, 9, None)]

wheel_3 = [(  13, 9,   7,13,  21, 17,   4, 5,None, 7,   8, 9),
           (   6,15,   4, 9,  18, 11,  26,14,   1,12,None,21),
           (None,10,None, 8,None, 22,None,16,None, 9,None, 5)]

wheel_4 = [( 8,None,16,   2,7,None, 9,None, 7,  14,11,None),
           ( 3,   8, 9,None,9,  20,12,   3, 6,None,14,  12),
           (17,  19, 3,  12,3,  26, 6,None, 2,  13, 9,None),
           (10,None,10,None,1,None, 9,None,12,None, 6,None)]

wheel_5 = [(11,11,14,11,14,11,14,14,11,14,11,14),
           ( 4, 5, 6, 7, 8, 9,10,11,12,13,14,15),
           ( 4, 4, 6, 6, 3, 3,14,14,21,21, 9, 9),
           ( 8, 3, 4,12, 2, 5,10, 7,16, 8, 7, 8)]

# function to rotate a wheel. All levels turn at the same time
def rotate(wheel, n=1):
    temp = wheel.copy()
    for _ in range(n):
        temp = [w[-1:]+w[:-1] for w in temp]
    return temp

# compute the sum of the elements in the wheel for all 12 columns
def process(wheel_1, wheel_2, wheel_3, wheel_4, wheel_5, show=False):
    
    sums = []
    
    for col in range(0, 12):
        els = []
        
        # rank 1 - if element is None, we go to the next rank
        if wheel_1[0][col] is not None:
            els.append(wheel_1[0][col])
        elif wheel_2[0][col] is not None:
            els.append(wheel_2[0][col])
        elif wheel_3[0][col] is not None:
            els.append(wheel_3[0][col])
        elif wheel_4[0][col] is not None:
            els.append(wheel_4[0][col])
        else:
            els.append(wheel_5[0][col])
        
        # rank 2
        if wheel_2[1][col] is not None:
            els.append(wheel_2[1][col])
        elif wheel_3[1][col] is not None:
            els.append(wheel_3[1][col])
        elif wheel_4[1][col] is not None:
            els.append(wheel_4[1][col])
        else:
            els.append(wheel_5[1][col])
            
        # rank 3
        if wheel_3[2][col] is not None:
            els.append(wheel_3[2][col])
        elif wheel_4[2][col] is not None:
            els.append(wheel_4[2][col])
        else:
            els.append(wheel_5[2][col])    

        # rank 4
        if wheel_4[3][col] is not None:
            els.append(wheel_4[3][col])
        else:
            els.append(wheel_5[3][col])
        
        # useful for debugging
        if show:
            string_list = [f"{x:2}" for x in els]
            print(f"{string_list} -> {sum(els)}")
        sums.append(sum(els))
    
    return sums, all(x == 42 for x in sums)


def solve(wheel_1, wheel_2, wheel_3, wheel_4, wheel_5):
    results = []
    solutions = 0
    for options in product(range(12), range(12), range(12), range(12), range(12)):
        s, r = process(rotate(wheel_1, options[0]), rotate(wheel_2, options[1]), rotate(wheel_3, options[2]), rotate(wheel_4, options[3]), rotate(wheel_5, options[4]))
        results.append((s,r, options, np.sum([int(x==42) for x in s])))
        if r is True:
            print(s, options)
            process(rotate(wheel_1, options[0]), rotate(wheel_2, options[1]), rotate(wheel_3, options[2]), rotate(wheel_4, options[3]), rotate(wheel_5, options[4]), show=True)
            solutions += 1
    
    print(f"found {solutions} solutions")
            
solve(wheel_1, wheel_2, wheel_3, wheel_4, wheel_5)