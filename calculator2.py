#!/usr/bin/env python3
import sys
noandsalary = {}
try:
    for i in sys.argv[1:]:
            no, salary = i.split(':')
            noandsalary[no] = int(salary)
except:
    print("Parameter Error")
def calculator(noandsalary):
    for no,salary in noandsalary.items():
        salary2 = salary - salary * 0.165 - 3500
        if salary2 <= 0:
            taxamountpayable = 0
        elif salary2 <= 1500:
            taxamountpayable = salary2 * 0.03  
        elif salary2 <= 4500:
            taxamountpaybale = salary2 * 0.1 - 105
        elif salary2 <= 9000:
            taxamountpayable = salary2 * 0.2 - 555
        elif salary2 <= 35000:
            taxamountpayable = salary2 * 0.25 - 1005
        elif salary2 <= 55000:
            taxamountpayable = salary2 * 0.3 - 2755
        elif salary2 <= 80000:
            taxamountpayable = salary2 * 0.35 - 5505
        elif slaary2 > 80000:
            taxamountpayable = salary2 * 0.45 - 13505
        final =  salary - (salary * 0.165) - taxamountpayable
        print(no,end='')
        print(":",end='')
        print("{:.2f}".format(final))
calculator(noandsalary)

