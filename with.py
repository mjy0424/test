class Master:
    def __enter__(self):
        print("enter")
        return 'master'

    def __exit__(self, type, value, trace):
        print("exit")


def get_master():
    return Master()


with get_master() as h:
    print(h)
# 如果你想要让你创建的对象能被 with 使用，那么你这个对象必须要有 __enter__ () 和 __exit__() 这两个方法。
# 当我们使用 with 去执行这个对象的时候，就会先去调用 __enter__ () ，最后再调用 __exit__() 。
# 在这里的 as 后面的变量名称，其实得到的就是 enter 方法返回的值。
'''
1.通过 with 语句可以得到一个上下文管理器
2.执行对象
3.加载 __enter__ 方法
4.加载 __exit__ 方法
5.执行 __enter__
6.as 可以得到 enter 的返回值
7.拿到对象执行相关操作
8.执行完了之后调用 __exit__ 方法
9.如果遇到异常，__exit__ 可以获取到异常信息
10.在 __exit__ 中处理异常，返回 True
11.继续执行 with 后面的语句。
'''
