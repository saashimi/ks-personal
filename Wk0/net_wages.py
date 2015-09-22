def compute_pay(hours, rate):
    if hours <= 40:
        pay = hours * rate
        return pay
    elif hours > 40:
        pay = 40 * rate
        over_hours = hours - 40
        overtime = (rate * 1.5) * over_hours
        tot_pay = pay + overtime
        return tot_pay
    else:
        print("something strange happened")
    

print(compute_pay(45, 10))

