n = int(input())
for i in range (1,n+1):
        a = input()
        k=len(a)
        if (k<=10):
            print(a)
        else:
            print(a[0]+str(k-2)+a[k-1])
        