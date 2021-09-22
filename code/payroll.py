#!/usr/local/bin/python3


def calc_pay(emp, rate, hours):
    pay = rate * hours

    return pay


def main():
    emp = "Callahan"
    net_pay = calc_pay(emp, 14.50, 30)
    print(f"Pay {emp} ${net_pay}")


if __name__ == "__main__":
    main()

