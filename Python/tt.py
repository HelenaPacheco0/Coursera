hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
pay = h * r

if h <= 40:
    print(pay)
else:
    pay = 40 * r
    pay2 = (h - 40) * 1.5 * r
    pay3 = pay + pay2
    print(pay3)
