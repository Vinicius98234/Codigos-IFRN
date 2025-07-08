for n in range (1,10000):
    n2 = 0
    for div in range(1, n//2 + 1):
        if n % div == 0:
            n2 += div
    if n2 > n:
        n3 = 0
        for div in range(1, n2//2 + 1):
            if n2 % div == 0:
                n3 += div

        if (n == n3) and (n != n2):
            print(n,n2)