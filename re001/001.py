#  常见数据类型

# region int floate String boolean
# int a = 1;
a = 1
# floate b = 1.1;
b = 1.1
# String c = "hello"
c = "hello"
# boolean d = true;
# 注意 python 的布尔开头是大写 
#   运算会把布尔->int 本质也是整形
d = True
print(a+d)
# endregion

# region 变量 这就是 python
# 动态语言
num = 1
print(num)
num = "hello"
print(num)
# endregion

# region 标识符 蛇形命名
# 蛇形 _
user_name = "good"
new_password = "asdfgh"
# endregion
 
# region 一些方法
# type(变量) 查看变量类型
print(type(user_name))
# isinstance(变量,类型) -> boolean 是不是同个类型
print(isinstance(num,str))
# endregion

# region 字符串 + %s f""
s1 = "hello"
s2 = 'hello'
# 多行字符串
s3 = """hello
"""
print(s3)
# 字符串拼接 
print(s1+s2+"world")
print("第一个 %s 第二个 %s" %(s1,s2))
print(f"第一个 {num} 第二个 {s3}")
# endregion

# region 输入输出 input()
# name = input("输入姓名")
# age = input("输入年龄")
# print(f"欢迎{age}岁的{name}")
# sum = 1000
# number = input("输入一个数")
# 数据转换
# print(f"sum {sum} 变化为 {sum - int(number)}")
# endregion

# region 逻辑运算符
# and 与
# or 或 
# not 取反 
# python 方法的定义
# def isBigger(number: int):
#     # Python 三元运算符：真值 if 条件 else 假值
#     return "大于" if number >= 30 else "小于"
# result_str = f"输入的{number}，{("大于" if int(number) >= 30 else "小于")} 30"
# print(result_str)
# print(f"输入的{number}，{("大于" if int(number) >= 30 else "小于")} 30")
# endregion

# region if
a = 25
if a > 30 :
    print("good")
elif a < 20:
    print("bad")
else:
    print("....")
# endregion

# region match (switch)
a = 6
match a:
    case 3:
        print("3")
    case 4:
        print("4")
    case _:
        print("兜底")
# 注意：case _: default
# endregion

# region 循环
a = 1
while a<3:
    print("执行")
    a += 1
# for 元素 in 待处理数据集:
#  循环体
# else:
#  循环结束执行代码
for i in range(3):
    print(i)
else:
    print("over")
# 注意：range都不包含end 右开
# range(end)
# range(start,end)
# range(start,end,step)
# endregion

