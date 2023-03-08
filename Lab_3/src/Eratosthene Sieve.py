from math import sqrt
from matplotlib import pyplot as plot
from time import time


def alg1(n, sieve_list):
    sieve_list[1] = False
    i = 2

    while i <= n:
        if sieve_list[i]:
            j = 2 * i

            while j <= n:
                sieve_list[j] = False
                j += i   
        i += 1


def alg2(n, sieve_list):
    sieve_list[1] = False
    i = 2

    while i <= n:
        j = 2 * i

        while j <= n:
            sieve_list[j] = False
            j += i
        
        i += 1


def alg3(n, sieve_list):
    sieve_list[1] = False
    i = 2

    while i <= n:
        if sieve_list[i]:
            j = i + 1

            while j <= n:
                if j % i == 0:
                    sieve_list[j] = False
                j += 1
        i += 1


def alg4(n, sieve_list):
    sieve_list[1] = False
    i = 2

    while i <= n:
        j = 2

        while j < i:
            if i % j == 0:
                sieve_list[i] = False
            j += 1
        i += 1


def alg5(n, sieve_list):
    sieve_list[1] = False
    i = 2

    while i <= n:
        j = 2

        while j <= sqrt(i):
            if i % j == 0:
                sieve_list[i] = False
            j += 1
        i += 1


# testing all the algorithms
def current_time_millis():
    return time() * 1000

iteration_list = list()
num = 1000
for index in range(1, 6):
    iteration_list.append(num)
    num *= 2

alg1_list = list()
alg2_list = list()
alg3_list = list()
alg4_list = list()
alg5_list = list()

for index in range(0, len(iteration_list)):
    s = [True] * (iteration_list[index] + 1)

    start_time = current_time_millis()
    alg1(iteration_list[index], s)
    end_time = current_time_millis()
    alg1_list.append(round(end_time - start_time, 4))

    s = [True] * (iteration_list[index] + 1)

    start_time = current_time_millis()
    alg2(iteration_list[index], s)
    end_time = current_time_millis()
    alg2_list.append(round(end_time - start_time, 4))

    s = [True] * (iteration_list[index] + 1)

    start_time = current_time_millis()
    alg3(iteration_list[index], s)
    end_time = current_time_millis()
    alg3_list.append(round(end_time - start_time, 4))

    s = [True] * (iteration_list[index] + 1)

    start_time = current_time_millis()
    alg4(iteration_list[index], s)
    end_time = current_time_millis()
    alg4_list.append(round(end_time - start_time, 4))

    s = [True] * (iteration_list[index] + 1)

    start_time = current_time_millis()
    alg5(iteration_list[index], s)
    end_time = current_time_millis()
    alg5_list.append(round(end_time - start_time, 4))
    

# plotting the obtained results
plot.figure()

plot.plot(iteration_list, alg1_list, color="red", label="Alg 1")
plot.plot(iteration_list, alg2_list, color="blue", label="Alg 2")
plot.plot(iteration_list, alg3_list, color="green", label="Alg 3")
plot.plot(iteration_list, alg4_list, color="black", label="Alg 4")
plot.plot(iteration_list, alg5_list, color="yellow", label="Alg 5")
plot.title("Eratosphene sieve", color="violet", fontsize=16)

plot.legend(loc='upper left')

plot.xlabel("n", color="violet", fontsize=14)
plot.ylabel("T(millis)", color="violet", fontsize=14)

plot.grid()
plot.show()
