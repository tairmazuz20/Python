def foo(num):
    sum = 0
    for i in num:
        sum += int(i)
    print('The sum od digits is: ', sum)


def oppositeNumber(num):
    for i in range(4, 0, -1):
        print(i, end="")
    print()


def filndurm(num):
    i = 0
    j = len(num) - 1
    while i < j:
        if num[i] != num[j]:
            return
        i += 1
        j -= 1
    print("The number: ", num, " is filndurm")


num = ''
while len(num) != 4:
    num = input('Please enter number with four digits: ')
    print('erorr! Please enter again number, with two digits. ')

foo(num)
oppositeNumber(num)
filndurm(num)
