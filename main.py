# This is a sample Python script.
from phonenumbers import TelFormatter


def print_num(tel):
    try:
        print(TelFormatter.format(tel))
    except Exception as e:
        print(repr(e), tel)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_num(" ww 0729- 9 -9 9999")
    print_num("0422991111")
    print_num("0312 3456 78 ")
    print_num("０３．１２３５．５６７８")
    print_num("０３−００００−００００")
    print_num("0428991111")
    print_num("0300000000")
    print_num("0110000000")
    print_num("0123000000")
    print_num("0126700000")
    print_num("0120000000")
    print_num("08099999999")
    print_num("08000000000")
    print_num("0429991111")
    print_num("0428991111")
    print_num("0422991111")
    print_num("0709999999")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
