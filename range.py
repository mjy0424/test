a_range = range(10)
'''
range函数返回一个range类型的整数序列，一般用在循环结构中。
range(start, stop, step)
range函数返回一个range对象实例。实例包含了计数的起始位置、终点位置和步长等信息。（类型为range）
所有参数都是整形。不能给出浮点数序列。
step不能小于1，也不能为0.
'''
a_list = [x * x for x in a_range]
print(a_list)
# 列表推导式，等价于
# for x in a_range:
#    a_list.append(x*x)
# 直接将循环中计算表达式得到的一系列值组成一个列表。
b_list = [x * x for x in a_range if x % 2 == 0]
print(b_list)
# 在列表推导式中添加 if 条件语句，这样列表推导式将只迭代那些符合条件的元素.
# 筛选结果中的偶数
a = (x for x in range(3))  # 元组推导式，类似于前者，生成的结果是生成器对象。
print(a.__next__())  # 遍历生成器
print(tuple(a))  # 将其转换成元组
