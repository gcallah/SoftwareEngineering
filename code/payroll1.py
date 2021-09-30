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
PA_TAX_BRACKETS = [
    [501, 0],
    [1001, .005],
    [1501, .01],
    [2001, .02],
    [BIG_NUM, .03]
]
NY_TAX_BRACKETS = [
    [501, 0],
    [1001, .1],
    [1501, .15],
    [2001, .2],
    [BIG_NUM, .25]
]

STATE_TABLES = {
    "NY": NY_TAX_BRACKETS,
    "PA": PA_TAX_BRACKETS,
}


def calc_bracketed_deduct(gross_pay, bracket_table):
    """
    Calculate a deduction based on a bracket table.
    """
    for bracket in bracket_table:
        if bracket[BRACKET_MAX] > gross_pay:
            deduct = gross_pay * bracket[BRACKET_RATE]
            break
    return deduct


def calc_pay(emp, rate, hours, state):
    gross_pay = rate * hours
    net_pay = gross_pay
    fed_inc = calc_bracketed_deduct(gross_pay, FED_TAX_BRACKETS)
    net_pay -= fed_inc
    net_pay -= calc_bracketed_deduct(gross_pay, STATE_TABLES[state])
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

