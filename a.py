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
'''
2022年10月25日下午4时，武汉鸣响防空警报
'''
