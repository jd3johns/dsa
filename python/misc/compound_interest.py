#
# Calculate compound interest anually given initial savings and savings added each year.
#
# Author: Jonathan Johnston
# Date: 2015/11/7
#
import sys
import argparse

#
# Calculate total savings compounded annually.
#
# @param: savings -- sum added at beginning of each year
# @param: interest -- annual interest (ex. 0.03 is 3%)
# @param: years -- number of years to compute for
# @param: compound -- as argument is initial savings, as recursive is
#                     total compounded savings
#
# @return: total compounded savings
#
def compound_savings(savings, interest, years, compound=0):
    if years == 0:
        return compound
    else:
        compound = (compound + savings)*(1 + interest)
        return compound_savings(savings, interest, years-1, compound)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--savings', required=True, type=int, help="Savings added at beginning of each year")
    parser.add_argument('-i', '--interest', required=True, type=float, help="Percent interest compounded annually")
    parser.add_argument('-y', '--years', required=True, type=int, help="Number of years to calculate")
    parser.add_argument('-n', '--initial', default=0, type=int, help="Amount of initial savings")
    args = parser.parse_args()

    # Echo arguments to user
    print(args)
    savings = args.savings
    interest = args.interest/100
    years = args.years
    initial = args.initial

    print(compound_savings(savings, interest, years, initial))


if __name__ == "__main__":
    sys.exit(main())
