# 函数
# region 函数
const_num = 99
def sum(a:int, b:int):
    """
    sum 两数之和
    
    :param a: int
    :type a: int
    :param b: int
    :type b: int
    """
    print("调用了sum(a:int, b:int)")
    return a+b

def sum(a,v):
    """
    sum 两数之和
    
    :param a: int
    :param v: int
    """
    print("调用了sum(a,v)")
    return a+v

def mult(c,d):
    """
    mult 返回了一个 sum
    
    :param c: int
    :param d: int
    """
    # 声明用全局变量
    global const_num

    return sum(const_num+c,d)

def default_def(a="good",b='3'):
    print(a)
    print(b)
    print(type(b))

def func(*args):
    # 习惯不定长参数 *args
    # 会变成一个元组 一旦定义不能修改
    print(*args)

def func1(**kwargs):
    # 习惯不定长参数 **kwargs
    # 会变成一个字典 键值对
    print(kwargs)

# 同时支持 *args（位置参数）和 **kwargs（关键字参数）
def func_all(*args, **kwargs):
    print("位置参数元组：", args)
    print("关键字参数字典：", kwargs)

# Python 不支持像 Java/C++ 那样的 
# “函数重载”，同名函数会发生 
# “后定义覆盖先定义” 的行为
# 嵌套调用 先进后出 先运行最里层的
print(sum(1,2))
print(mult(3,4))
default_def()
func(1,3,4,4,5,"good")
func1(gppd=3)
func_all(1,2,3, name="Python", age=30)
# 输出：
# 位置参数元组： (1, 2, 3)
# 关键字参数字典： {'name': 'Python', 'age': 30}

# 1. 自定义运算函数（满足：接收两个参数，返回运算结果）
# 求和函数
def sum_func(x, y):
    return x + y

# 可选：扩展其他运算（如求积），验证灵活性
def mult_func(x, y):
    return x * y

# 2. 正确定义函数：带函数名 + 参数a,b,oper
def calc(a, b, oper):
    # 调用oper参数（本质是传入的函数），传入a和b执行运算
    result = oper(a, b)
    print(f"{a} 和 {b} 执行{oper.__name__}运算的结果：{result}")
    return result

# 3. 正确调用：函数名(1, 2, 自定义运算函数)
# 传入求和逻辑 sum_func
calc(1, 2, sum_func)
# 可选：传入求积逻辑 mult_func，验证灵活性
calc(1, 2, mult_func)
# endregion
# region 匿名函数

lambda a,vb: a+vb

# 定义计算函数（同上）
def calc(a, b, oper):
    result = oper(a, b)
    print(f"{a} 和 {b} 执行运算的结果：{result}")
    return result

# 调用时直接传递 lambda 求和函数（无需提前定义sum_func）
calc(1, 2, lambda x, y: x + y)
# 同理，传递 lambda 求积函数
calc(1, 2, lambda x, y: x * y)