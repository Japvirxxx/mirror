r=int(input("Enter the numbers of rows: "))

for i in range(r):
    for j in range(i+1):
        print("*", end=" ")
    print()
len = r * 3
dl = "-" * len
print(dl)
for i in range(r):
    for j in range(i,r):
        print("*", end=" ")
    print()