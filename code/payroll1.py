#!/usr/local/bin/python3

BIG_NUM = 999999999999999999
BRACKET_MAX = 0
BRACKET_RATE = 1
FED_TAX_BRACKETS = [
    [501, 0],
    [1001, .1],
    [1501, .2],
    [2001, .3],
    [BIG_NUM, .4]
]


def calc_fed_inc(gross_pay):
    """
    Calculate federal income tax deduction.
    """
    for bracket in FED_TAX_BRACKETS:
        if bracket[BRACKET_MAX] > gross_pay:
            fed_inc = gross_pay * bracket[BRACKET_RATE]
            break
    return fed_inc


def calc_pay(emp, rate, hours, state):
    gross_pay = rate * hours
    net_pay = gross_pay
    fed_inc = calc_fed_inc(gross_pay)
    net_pay -= fed_inc
    state_inc = 0
    if state == "NY":
        if gross_pay <= 500:
            state_inc = 0
        elif gross_pay <= 1001:
            state_inc = gross_pay * .01
        elif gross_pay <= 1501:
            state_inc = gross_pay * .02
        elif gross_pay <= 2001:
            state_inc = gross_pay * .03
        else:
            state_inc = gross_pay * .04
    elif state == "PA":
        if gross_pay <= 500:
            state_inc = 0
        elif gross_pay <= 1001:
            state_inc = gross_pay * .005
        elif gross_pay <= 1501:
            state_inc = gross_pay * .01
        elif gross_pay <= 2001:
            state_inc = gross_pay * .02
        else:
            state_inc = gross_pay * .03
    elif state == "CT":
        if gross_pay <= 500:
            state_inc = 0
        elif gross_pay <= 1001:
            state_inc = gross_pay * .05
        elif gross_pay <= 1501:
            state_inc = gross_pay * .1
        elif gross_pay <= 2001:
            state_inc = gross_pay * .15
        else:
            state_inc = gross_pay * .2
    net_pay -= fed_inc
    ss_deduct = max(gross_pay, 2000) * .07
    net_pay -= ss_deduct
    ins_deduct = 12
    net_pay -= ins_deduct
    return (gross_pay, net_pay)


def main():
    emp = "Callahan"
    (gross_pay, net_pay) = calc_pay(emp, 14.50, 30, "PA")
    print(f"Pay {emp} net of ${net_pay} from gross of ${gross_pay}")


if __name__ == "__main__":
    main()

