def sum_of_ints_until_single_digit():

    while True:

        try:
            print("Input:")
            num = int(input())

            if num < 0:
                num = num * -1

            num = str(num)

            if len(num) < 1000 and len(num) > 1:
                break

            else:
                print("That is not a valid input.")

        except:
            print("That is not a valid input.")

    digits = list(int(number) for number in num)

    while len(digits) != 1:

        newNum = sum(digits)
        newNum = str(newNum)

        digits = list(int(number) for number in newNum)

    print(f"\nThe output is: {''.join(str(y) for y in digits)}")

    return digits


if __name__ == "__main__":

    sum_of_ints_until_single_digit()
