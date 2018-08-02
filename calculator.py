#!/usr/bin/env python3
import sys
noandsalary = {}
try:
    for i in sys.argv[1:]:
            no, salary = i.split(':')
            noandsalary[no] = int(salary)
except:
    print("Parameter Error")
def calculator(**noandsalary):
    for no,salary in noandsalary.items():
        if salary > 3500:
            taxableincome = salary - 3500 -(salary * 0.165)
        else:
            taxableincoem = 0
        if taxableincome <= 1500 and taxableincome > 0:
            taxamountpayable = taxableincome * 0.03 - 0
        elif taxableincome >1500 and taxableincome <= 4500:
            taxamountpayable = taxableincome * 0.1 - 105
        elif taxableincome >4500 or taxableincoem <= 9000:
            taxamountpayable = taxableincome * 0.2 - 555
        elif taxableincome >9000 or taxableincome <= 35000:
            taxamountpayable = taxableincome * 0.25 - 1005
        elif taxableincome >35000 or taxableincome <= 55000:
            taxamountpayable = taxableincome * 0.3 - 2755
        elif taxableincome >55000 or taxableincoem <= 80000:
            taxamountpayable = taxableincome * 0.35 - 5505
        elif taxableincome >80000:
            taxamountpayable = taxableincome * 0.45 - 13505
        final =  salary - (salary * 0.165) - taxamountpayable
        print(no,end='')
        print(":",end='')
        print("{:.2f}".format(final))
calculator(**noandsalary)

