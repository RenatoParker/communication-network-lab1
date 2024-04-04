import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcol

color_dict = mcol.TABLEAU_COLORS


def lin2db(x):
    return 10*np.log10(x)


def db2lin(x):
    return 10**(x/10)


class ADC:
    fs_step = 2.75625e3
    
    def __init__(self):
        pass

    
class BSC:
    
    def __init__(self):
        pass


class PCM:

    def __init__(self):
        pass

    
def exercise_1():
    pass


def exercise_2():
    pass


def exercise_3():
    pass



if __name__ == "__main__":
    print("Laboratory 3 - ADC-BSC")
    
    exercise_1()
    exercise_2()
    exercise_3()


    
    
    
    