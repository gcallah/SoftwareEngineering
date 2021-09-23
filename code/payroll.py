#!/usr/local/bin/python3


def calc_pay(emp, rate, hours, state):
    gross_pay = rate * hours
    net_pay = gross_pay
    # deduct federal income tax
    if gross_pay <= 500:
        fed_inc = 0
    elif pay <= 1001:
        fed_inc = gross_pay * .1
    elif pay <= 1501:
        fed_inc = gross_pay * .2
    elif pay <= 2001:
        fed_inc = gross_pay * .3
    else:
        fed_inc = gross_pay * .4
    net_pay -= fed_inc
    state_inc = 0
    if state == "NY":
        if gross_pay <= 500:
            state_inc = 0
        elif pay <= 1001:
            state_inc = gross_pay * .01
        elif pay <= 1501:
            state_inc = gross_pay * .02
        elif pay <= 2001:
            state_inc = gross_pay * .03
        else:
            state_inc = gross_pay * .04
    elif state == "PA":
        if gross_pay <= 500:
            state_inc = 0
        elif pay <= 1001:
            state_inc = gross_pay * .005
        elif pay <= 1501:
            state_inc = gross_pay * .01
        elif pay <= 2001:
            state_inc = gross_pay * .02
        else:
            state_inc = gross_pay * .03
    elif state == "CT":
        if gross_pay <= 500:
            state_inc = 0
        elif pay <= 1001:
            state_inc = gross_pay * .05
        elif pay <= 1501:
            state_inc = gross_pay * .1
        elif pay <= 2001:
            state_inc = gross_pay * .15
        else:
            state_inc = gross_pay * .2
    net_pay -= fed_inc
    ss_deduct = max(gross_pay, 2000) * .07
    net_pay -= ss_deduct
    ins_deduct = 12
    net_pay -= ss_deduct
    return (gross_pay, net_pay)


def main():
    emp = "Callahan"
    (gross_pay, net_pay) = calc_pay(emp, 14.50, 30, "PA")
    print(f"Pay {emp} net of ${net_pay} from gross of ${gross_pay}")


if __name__ == "__main__":
    main()

