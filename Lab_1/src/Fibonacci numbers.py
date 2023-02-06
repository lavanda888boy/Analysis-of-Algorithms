from matplotlib import pyplot
from math import sqrt
from time import time

# recursive Fibonacci sequence
def recursive_fibonacci(n):
    if n <= 1:
        return n
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

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


# testing the efficinency of all algorithms
order_number = 10
order_list = list()
for i in range(1, 6):
    order_list.append(order_number)
    order_number *= 10

order_number = 5
small_order_list = list()
for i in range(1, 8):
    small_order_list.append(order_number)
    order_number += 10

order_number = 10

matrix_args = list()
dynamic_args = list()

for i in range(1, 6):
    initial_time = current_time_millis()
    dynamic_fibonacci(order_number)
    end_time = current_time_millis()
    dynamic_args.append(end_time - initial_time)
    order_number *= 10

order_number = 10
for i in range(1, 6):
    initial_time = current_time_millis()
    matrix_fibonacci(order_number)
    end_time = current_time_millis()
    matrix_args.append(end_time - initial_time)
    order_number *= 10


# plotting the results for milliseconds order
pyplot.figure()
pyplot.plot(order_list, dynamic_args, color="red", label="Dynamic method")
pyplot.plot(order_list, matrix_args, color="blue", label="Matrix multiplication method")
pyplot.title("Computing Fibonacci sequence", color="violet", fontsize=16)

pyplot.legend(loc='upper left')

pyplot.xlabel("n", color="violet", fontsize=14)
pyplot.ylabel("T(millis)", color="violet", fontsize=14)

pyplot.grid()
pyplot.show()


# recursion + dynamic programming
memory = [-1 for i in range(order_number + 1)]
 
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


# plotting the results for milliseconds order
# limited by the number of recursion calls
order_number = 5
recursiveDP_args = list()
for i in range(1, 8):
    initial_time = current_time_millis()
    recursiveDP_fibonacci(order_number)
    end_time = current_time_millis()
    recursiveDP_args.append(end_time - initial_time)
    order_number += 10

order_number = 5
binet_args = list()
for i in range(1, 8):
    initial_time = current_time_millis()
    Binet_formula(order_number)
    end_time = current_time_millis()
    binet_args.append(end_time - initial_time)
    order_number += 10

pyplot.figure()
pyplot.plot(small_order_list, recursiveDP_args, color="red", label="DP recursion method")
pyplot.plot(small_order_list, binet_args, color="blue", label="Binet's formula method")
pyplot.title("Computing Fibonacci sequence", color="violet", fontsize=16)

pyplot.legend(loc='upper right')

pyplot.xlabel("n", color="violet", fontsize=14)
pyplot.ylabel("T(millis)", color="violet", fontsize=14)

pyplot.grid()
pyplot.show()


# plotting the slowest recursive algorithm
order_number = 5
recursive_args = list()
for i in range(1, 6):
    initial_time = current_time_millis()
    recursive_fibonacci(order_number)
    end_time = current_time_millis()
    recursive_args.append(end_time - initial_time)
    order_number += 5

pyplot.figure()
pyplot.plot([5, 10, 15, 20, 25], recursive_args, color="green", label="Recursive method")
pyplot.title("Computing Fibonacci sequence", color="violet", fontsize=16)

pyplot.legend(loc='upper left')

pyplot.xlabel("n", color="violet", fontsize=14)
pyplot.ylabel("T(millis)", color="violet", fontsize=14)

pyplot.grid()
pyplot.show()


# plotting the fastest fast-doubling iterative algorithm
order_number = 100
fast_doubling_args = list()
for i in range(1, 6):
    initial_time = current_time_millis()
    fast_doubling_iterative(order_number)
    end_time = current_time_millis()
    fast_doubling_args.append(end_time - initial_time)
    order_number *= 10


# plotting the results for milliseconds order
pyplot.figure()
pyplot.plot([10**2, 10**3, 10**4, 10**5, 10**6], dynamic_args, color="blue", label="Fast-doubling iterative method")
pyplot.title("Computing Fibonacci sequence", color="violet", fontsize=16)

pyplot.legend(loc='upper left')

pyplot.xlabel("n", color="violet", fontsize=14)
pyplot.ylabel("T(millis)", color="violet", fontsize=14)

pyplot.grid()
pyplot.show()

