def main():
    print("enter number of elements: ", end="")
    n = int(input())

    print("enter elements: ", end="")
    a = []
    for i in range(n):
        element = int(input())
        a.append(element)


    max = a[0]
    min = a[0]
    for i in range(n):
        if max < a[i]:
            max = a[i]
        if min > a[i]:
            min = a[i]
    print(f"maximum: {max} minimum: {min}")

main()