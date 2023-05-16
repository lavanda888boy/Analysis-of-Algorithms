import decimal

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

decimal.getcontext().prec = 2
print(Gauss_Legendre())


