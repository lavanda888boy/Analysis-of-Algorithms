#from matplotlib import pyplot
from math import sqrt
from time import time

order = int(input("Enter the order of the series you want to compute: "))

# recursive Fibonacci sequence
def recursive_fibonacci(n):
    if n <= 1:
        return n
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)


# recursion + dynamic programming
memory = [-1 for i in range(order + 1)]
 
def recursiveDP_fibonacci(n):
    if (n <= 1):
        return n

    global memory
     
    first = 0
    second = 0
 
    if (memory[n - 1] != -1):
        first = memory[n - 1]
    else:
        first = recursiveDP_fibonacci(n - 1)
    if (memory[n - 2] != -1):
        second = memory[n - 2]
    else:
        second = recursiveDP_fibonacci(n - 2)
    
    memory[n] = first + second
 
    return memory[n]


# dynamic calculation
def dynamic_fibonacci(n):
    f = [0, 1]
      
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])

    return f[n]

# Binet's formula application
# after n = 72 rounding is no more precise
def Binet_formula(n):
    phi = (1 + sqrt(5)) / 2
 
    return round(pow(phi, n) / sqrt(5))


# Fast Doubling algorithm in an iterative implementation
def fast_doubling_iterative(n):
    bin_of_n = bin(n)[2:]
    f = [0, 1]
 
    for b in bin_of_n:
        f2i1 = f[1]**2 + f[0]**2
        f2i = f[0]*(2*f[1]-f[0])
 
        if b == '0':
            f[0], f[1] = f2i, f2i1 
        else:
            f[0], f[1] = f2i1, f2i1+f2i
 
    return f[0]



# 2*2 matrix multiplication
def matrix_fibonacci(n):
    F = [[1, 1], [1, 0]]
    if (n == 0):
        return 0
    power(F, n - 1)
     
    return F[0][0]
 
# function which multiplies 2*2 matrices
def multiply(F, M):
 
    x = (F[0][0] * M[0][0] + F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] + F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] + F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] + F[1][1] * M[1][1])
     
    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w
 
# function for calculating n-th power of teh matrix
def power(F, n):
    M = [[1, 1], [1, 0]]

    for i in range(2, n + 1):
        multiply(F, M)


def current_time_millis():
    return time() * 1000


# testing the efficinency
order_number = 10
for i in range(1, 6):
    initial_time = current_time_millis()
    fast_doubling_iterative(order_number)
    end_time = current_time_millis()
    print(end_time-initial_time)
    print()
    order_number *= 10






