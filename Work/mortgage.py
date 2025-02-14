# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000


while principal > 0:
    month += 1
    is_extra_pay_month = 0
    if (month >= extra_payment_start_month) and (month <= extra_payment_end_month):
        is_extra_pay_month = 1
    principal = principal * (1+rate/12) - payment - \
        (extra_payment*is_extra_pay_month)
    total_paid = total_paid + payment
    print(month, round(total_paid, 2), round(principal, 2))

if principal < 0:
    total_paid += principal

print('Total paid', total_paid)
print('Months', month)
