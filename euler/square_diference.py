from functools import reduce


def square_diference(number):
    nsum = number * (number + 1) // 2
    return nsum*(nsum - (2*number + 1) // 3)



if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        num = 100
    print(square_diference(num))