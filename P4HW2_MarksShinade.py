# Shinade Marks
# 10/26
# P4HW2
# Loops in Salary calculator


# request info
name = input("Enter Employee's or name 'done' to finish: ")

# variables for totals
overtimepay_total = 0
regularpay_total = 0
grosspay_total = 0
employee_count = 0

while name != 'done':
    employee_count += 1

    hours = float(input("How many hours did " +name+ " work this week? "))
    rate = float(input("What is " +name+ "'s hourly pay rate? "))
    
    # calculate pay
    if hours > 40:
        overtime_hours = hours - 40
        gross_pay = regular_pay + overtime_pay
        overtime_pay = overtime_hours * (rate * 1.5)
        regular_pay = 40 * rate
        
    else:
        overtime_pay = 0
        overtime_hours = 0
        regular_pay = hours * rate
        gross_pay = regular_pay
    
    grosspay_total += gross_pay
    overtimepay_total += overtime_pay
    regularpay_total += regular_pay

    
    # update totals
    overtimepay_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay

    
    # display results
    print("---------------------------------")
    print("Employee Name: ", name)
    print(f'{"Hours Worked: ":<15}{"Pay Rate: ":<12}{"Regular Pay: ":<15}{"Overtime Pay: ":<15}{"Gross Pay: ":<12}')
    print("------------------------------------------------------------------")
    print(f'{hours:<15.2f}{rate:<12.2f}{regular_pay:<15.2f}{overtime_pay:<15.2f}{gross_pay:<12.2f}')


    # request next employee info
    name = input("Enter Employee's or name 'done' to finish: ")

print("Total number of employees entered: ", employee_count)
print("Total amount paid for overtime: $", format(overtimepay_total, '.2f'))
print("Total amaount paid for regular pay: $", format(regularpay_total, '.2f'))
print("Total amount paid in gross pay: $", format(grosspay_total, '.2f'))