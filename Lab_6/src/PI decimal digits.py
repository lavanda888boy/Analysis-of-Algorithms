import decimal
from time import time
import matplotlib.pyplot as plot


# method implementing Gauss-Legendre algorithm 
# for a given context precision 
def Gauss_Legendre():
    D = decimal.Decimal

    with decimal.localcontext() as ctx:
        ctx.prec += 2                
        a, b, t, p = 1, 1/D(2).sqrt(), 1/D(4), 1                
        pi = None

        while 1:
            an = (a + b) / 2
            b = (a * b).sqrt()
            t -= p * (a - an) * (a - an)
            a, p = an, 2*p
            piold = pi
            pi = (a + b) * (a + b) / (4 * t)
            
            if pi == piold:
                break
    return +pi


# Bailey-Borwein-Plouffe algorithm with summing helper function
def S(j, n):
    # Left sum
    s = 0.0
    k = 0

    while k <= n:
        r = 8*k + j
        s = (s + float(pow(16, n-k, r)) / r) % 1.0
        k += 1

    # Right sum
    t = 0.0
    k = n + 1

    while 1:
        newt = t + pow(16, n-k) / (8*k+j)
        # Iterate until t no longer changes
        if t == newt:
            break
        else:
            t = newt
        k += 1
    return s + t


def BBP_formula(n):
    n -= 1
    x = (4 * S(1, n) - 2 * S(4, n) - S(5, n) - S(6, n)) % 1.0
    return "%014x" % int(x * 16**14)


# implementation of the simplified Chudnovsky algorithm
def Chudnovsky(n):
    decimal.getcontext().prec = n + 1
    C = 426880 * decimal.Decimal(10005).sqrt()
    K = 6.
    M = 1.
    X = 1
    L = 13591409
    S = L

    for i in range(1, n):
        M = M * (K ** 3 - 16 * K) / ((i + 1) ** 3)
        L += 545140134
        X *= -262537412640768000
        S += decimal.Decimal(M * L) / X

    pi = C / S
    return pi


# time counter in milliseconds
def current_time_millis():
    return time() * 1000


# testing the algorithms against the input data
input_digit = 10
r = 10
input_list = list()
start_time, end_time = 0, 0

gauss_list = list()
bbp_list = list()
chudnovsky_list = list()

for i in range(r):
    input_list.append(input_digit)

    decimal.getcontext().prec = input_digit
    start_time = current_time_millis()
    Gauss_Legendre()
    end_time = current_time_millis()
    gauss_list.append(round(end_time - start_time, 4))

    start_time = current_time_millis()
    BBP_formula(input_digit)
    end_time = current_time_millis()
    bbp_list.append(round(end_time - start_time, 4))

    input_digit *= 2


input_chud_list = list()
input_digit = 2
for i in range(r):
    input_chud_list.append(input_digit)

    start_time = current_time_millis()
    Chudnovsky(input_digit)
    end_time = current_time_millis()
    chudnovsky_list.append(round(end_time - start_time, 4))

    input_digit *= 2


# visualizing the results obtained
plot.figure()

plot.plot(input_list, gauss_list, color="red", linewidth=3, label="Gauss-Legendre Algorithm")
plot.plot(input_list, bbp_list, color="blue", linewidth=3, label="BBP formula")

plot.title(f"PI n-th decimal digit", color="violet", fontsize=16)
plot.legend(loc='upper left')

plot.xlabel("n", color="violet", fontsize=14)
plot.ylabel("T(millis)", color="violet", fontsize=14)

plot.grid()
plot.show()


plot.figure()

plot.plot(input_chud_list, chudnovsky_list, color="green", linewidth=3, label="Chudnovsky Algorithm")

plot.title(f"PI n-th decimal digit", color="violet", fontsize=16)
plot.legend(loc='upper left')

plot.xlabel("n", color="violet", fontsize=14)
plot.ylabel("T(millis)", color="violet", fontsize=14)

plot.grid()
plot.show()
