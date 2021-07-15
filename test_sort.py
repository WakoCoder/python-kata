A = [1, 2, 2, 3.5, 4, 5, 1.0, 3]
B = [0.1, -0.1, 0.2, -0.2, 0.3]
C = [1, 2, 3, 4, 3, 4, 3, 2, 1]
D = [2, 1, 1, 1, 1]

def unique_sort_f(x):
    d = {}
    for i in x:
        d[i] = i

    us = []
    for k in d:
        us.append(k)

    S_us = sorted(us)    

   


    print(S_us)
    return S_us

def test_unique_sort():
    assert unique_sort_f(C) == [1, 2, 3, 4]
    assert unique_sort_f(D) == [1, 2]
 
