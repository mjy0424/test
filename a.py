list = []
while True:
    list.append(input())
    judge = input("Anything else?(y/n)")
    if judge == "y":
        continue
    if judge == "n":
        break
    else:
        raise ValueError("Not an option.")
for str in list:
    print(str, end='')
