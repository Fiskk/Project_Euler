#Steffan Sampson
#11-13-2017
#Project Euler Problem 2


def iterative_even_fibonacci_sums(limit):
    n1 = 0
    n2 = 1
    n3 = 0
    total = 0

    while n3 < limit:
        n3 = n1 + n2
        #print(n3) #Checkpoint
        n1, n2 = n2, n3

        if n3 % 2 == 0:
            total += n3

    return total


print(iterative_even_fibonacci_sums(4000000))
