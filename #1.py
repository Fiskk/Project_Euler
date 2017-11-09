#Steffan Sampson
#11-8-2017
#Project Euler Problem 1


def sum_of_multiples():
    print("This function finds the sums of multiples of integers below an upper bound")
    print("This function takes in an upper bound")
    print("As well as the numbers to be used to find the multiples")

    #low_end = int(input("Please input your lower bound: "))
    high_end = int(input("Please input your upper bound: "))

    stop = False
    ints = []
    print("Please input values > 0 to be used to find multiples below the bound, to stop inputting input '-1'")
    while stop is False:

        value = int(input("Value: "))

        if value > 0 and value % 1 == 0:
            ints.append(value)

        elif value == -1:
            stop = True

        else:
            print("Input either an integer > 0 or -1")

    print(ints)
    print(str(high_end) + "\n")

    num_of_values = len(ints) - 1

    list_of_multiples = []
    n = 0
    z = 1
    while n <= num_of_values:

        multiple = ints[n] * z

        #print(multiple)
        if multiple < high_end:
            list_of_multiples.append(multiple)
            z += 1
        else:
            n += 1
            z = 1

    print(list_of_multiples)

    num_of_multiples = len(list_of_multiples) - 1

    #set_of_multiples = set(list_of_multiples)
    #unique_list_of_multiples = [set_of_multiples]
    total = 0
    n = 0
    while n <= num_of_multiples:

        total += list_of_multiples[n]

        n += 1

    print(total)


sum_of_multiples()


