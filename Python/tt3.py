def computepay(h, r):
    if h <= 40:
        return (h * r)
    else:
        pay = 40 * r
        pay2 = (h - 40) * 1.5 * r
        pay3 = pay + pay2
        return pay3

    #return 42.37

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
p = computepay(h, r)
#p = computepay(10, 20)
print("Pay", p)
