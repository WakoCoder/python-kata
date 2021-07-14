A = [1, 2, 2, 3.5, 4, 5, 1.0, 3]
B = [0.1, -0.1, 0.2, -0.2, 0.3]
C = [1, 2, 3, 4, 3, 4, 3, 2, 1]
D = [1, 1, 1, 1, 2]

def mean_f(x):
    # need to write the code to calculate the mean
    return 0.0
    
def median_f(x):
    # need to write the code to calculate the median
    return 0.0
    
def mode_f(x):
    # need to write the code to calculate the mode
    return 0.0
    
def range_f(x):
    # need to write the code to calculate the range
    return 0.0

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
    