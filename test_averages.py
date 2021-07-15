A = [1, 2, 2, 3.5, 4, 5, 1.0, 3]
B = [0.1, -0.1, 0.2, -0.2, 0.3]
C = [1, 2, 3, 4, 3, 4, 3, 2, 1]
D = [1, 1, 1, 1, 2]

def mean_f(x):
    mean = sum(x)/len(x)
    print(mean)
    return mean
    
def median_f(x):
    sorted_x = sorted(x)
    leng_x = len(x)
    if leng_x%2==0:
        # even
        a = int((leng_x / 2)- 1)
        b = int(leng_x / 2)
        median = (sorted_x[a] + sorted_x[b]) / 2
        print(leng_x, a, b)
    else:
        # odd case
        a =int((leng_x -1) / 2)
        median = sorted_x[a] 
    
    
    return median
    
def mode_f(x):
    d = {}
    for i in x:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    mode = x[0]
    max_count = 1
    for k in d:
        count = d[k]

        if count > max_count:
            mode = k
            max_count = count


    print(d)
    return mode
    
def range_f(x):#
    sorted_x = sorted(x)
    range1 = sorted_x[-1] - sorted_x[0]
    print(range1)
    return range1

def test_mean():
    assert mean_f(A) == 2.6875
    assert mean_f(B) == 0.06
 
def test_median():
    assert median_f(A) == 2.5
    assert median_f(B) == 0.1
    
def test_mode():
    assert mode_f(C) == 3
    assert mode_f(D) == 1
    
def test_range():
    assert range_f(A) == 4
    assert range_f(B) == 0.5
    
