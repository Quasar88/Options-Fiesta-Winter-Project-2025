def main():
    a = input("enter any string:- ")
    n = len(a)
    flag=0
    for i in range(0, (n//2)):
        if(a[i] != a[n-1-i]):
            flag=1
            break
    if(flag==1):
        print("Not a pallindrome")
    else:
        print("Pallindrome")
main()