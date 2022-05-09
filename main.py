# This is a sample Python script.
from phonenumbers import TelFormatter


def print_num(tel):

    print(TelFormatter.format(tel))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_num("0729999999")
    print_num("0422991111")
    print_num("0312345678")
    print_num("０３．１２３５．５６７８")
    print_num("０３−００００−００００")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
