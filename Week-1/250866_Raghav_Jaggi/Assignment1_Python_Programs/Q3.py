def main():
    print("enter number of elements: ", end="")
    n = int(input())

    print("enter elements: ", end="")
    a = []
    for i in range(n):
        element = int(input())
        a.append(element)
    
    print("enter x: ", end="")
    x = int(input())
    for i in range(0, n, 1):
        for j in range(i+1, n, 1):
            if abs(a[i]-a[j])==x:
                print(f"the pair of elements is {a[i]} and {a[j]}")
                flag=1
                break
        if flag==1:
            break



main()