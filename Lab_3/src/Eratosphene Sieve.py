from math import sqrt

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


# TODO: fix the alg4 
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



num = int(input("n = "))
s = [True] * (num + 1)
alg4(num, s)

for index in range(1, len(s) - 1):
    if s[index]:
        print(index)