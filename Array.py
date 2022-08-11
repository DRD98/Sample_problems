import array as arr

def result (a, n, length):
    print ("Pairs are: ")
    for i, j in ((a,b) for a in range(length) for b in range(length)):
        if (i == j):
            flag = 0
        if ((a[i] + a[j] == n) and a[i] != 0 and a[j] != 0 and i != j):
            flag = 1
        else:
            flag = 0
        if (flag == 1):
            print ("(" + str(a[i]) +", " + str(a[j]) + ")")
            a[i] = 0
            a[j] = 0

arr = input("Enter the elements in the array (with a space between them): ")
try:
    num = int(input("Enter the sum to be checked for: "))
    a = list(map(int, arr.split(' ')))
except ValueError:
    print ("Incorrect input. Exited from program.")
    quit()
l = len(a)
result(a, num, l)