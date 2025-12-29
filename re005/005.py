# 面向对象
# region 类
class Student:
    # 注意 用_xxx（单下划线）标识 “保护成员”，__xxx（双下划线）标识 “私有成员”

    # 类的属性 所有实例共享
    school = "小学" 
    # 全参构造+无参构造
    # 给 name 和 age 设置默认值（None 或其他默认值），支持无参实例化
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age  # 已有逻辑，删除多余 pass
    # 实例方法
    def check(self):
        """
        check 报告
        
        :param self: 实例
        """
        print(f"{self.name} check")
    # 魔法方法
    # 对应Java重写equals()：自定义“逻辑相等”规则
    def __eq__(self, other):
        # 先判断other是否是Student实例，避免类型错误
        if not isinstance(other, Student):
            return False
        # 业务逻辑：姓名和年龄都相同，即为“相等”
        return self.name == other.name and self.age == other.age

    # 对应Java重写toString()：自定义友好字符串输出
    def __str__(self):
        # 返回包含属性的可读字符串
        return f"Student(name={self.name}, age={self.age})"


# 1. 无参实例化 s1，后续手动设置属性（现在不报错）
s1 = Student()
s1.name = "s1"
s1.age = 18
# 按字典输出实例属性（__dict__ 正常生效）
print(s1.__dict__)  # 输出：{'name': 's1', 'age': 18}
s1.check()
# 2. 传参实例化 s2，直接通过构造方法初始化属性
s2 = Student("s2", 19)
print(s2.__dict__)  # 输出：{'name': 's2', 'age': 19}
s2.check()


# 测试__eq__
s1 = Student("张三", 18)
s2 = Student("张三", 18)
s3 = Student("李四", 19)
print(s1 == s2)  # True（逻辑相等，而非内存地址相等）
print(s1 == s3)  # False
print(s1.school)
print(s2.school)
print(s3.school)
# 测试__str__
print(s1)  # 输出：Student(name=张三, age=18)（而非默认的内存地址字符串）
# endregion
# region 规范类
class Student:
    def __init__(self, name, age, score):
        # 公开成员（对应 Java public）
        self.name = name
        # 保护成员（单下划线，对应 Java protected，约定外部不访问）
        # from 模块 import * 时不会导入
        self._age = age
        # 私有成员（双下划线，对应 Java private，自动名称改写）
        # Python 会自动进行 “名称改写”（name mangling），外部无法直接通过 __xxx 访问，仅类内部可访问
        self.__score = score

    # 类内部可访问所有成员（包括 __score）
    def print_info(self):
        print(f"姓名：{self.name}，年龄：{self._age}，成绩：{self.__score}")

# 实例化对象
s = Student("张三", 18, 95)

# 1. 访问公开成员（无限制）
print(s.name)  # 正常输出：张三

# 2. 访问保护成员（单下划线，可直接访问，但不推荐）
print(s._age)  # 正常输出：18（本质公开，仅约定私有）

# 3. 访问私有成员（双下划线，直接访问报错）

# print(s.__score)  # 报错：AttributeError: 'Student' object has no attribute '__score'

# 4. 私有成员的名称改写：外部可通过 _类名__xxx 访问（不推荐，破坏封装）
print(s._Student__score)  # 正常输出：95（Python 改写后的名称，非推荐用法）

# 5. 类内部访问私有成员（正常执行）
s.print_info()  # 输出：姓名：张三，年龄：18，成绩：95


# endregion




# region 异常
# 对应 Java try-catch-finally
a = 10
b = 0
result = 0

# try：监控可能抛出异常的代码（与 Java try 完全一致）
try:
    result = a / b  # 此处会抛出 ZeroDivisionError（对应 Java ArithmeticException）
    print(f"运算结果：{result}")
# except：捕获指定异常并处理（对应 Java catch）
except ZeroDivisionError as e:  # as e 捕获异常对象（对应 Java 的 Exception e）
    print(f"Python 捕获异常：{e}")
# finally：无论是否发生异常，必定执行（与 Java finally 完全一致）
finally:
    print("Python finally 块：无论异常与否，我都会执行")

# endregion