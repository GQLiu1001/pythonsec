PI = 3.14

def sum(a:int,b:int) -> int:
    return a+b

def max(a:int,b:int) -> int:
    return a if a>b else b


# region all name
# 1. 定义 __all__：控制 from mymath import * 时可导入的成员
# 列表内填写需要对外暴露的变量、函数名（字符串格式）
# __all__ = ["PI", "sum", "max"]
__all__ = ["sum", "max"]

# 2. 定义 __name__ 相关逻辑：判断模块是直接运行还是被导入
# __name__ 是Python模块的内置属性，有两种取值场景
if __name__ == "__main__":
    # 当模块被直接运行时（如直接双击运行 mymath.py 或 python mymath.py），执行以下测试代码
    print("mymath 模块被直接运行了！")
    # 内部测试函数功能
    print(f"sum(1,2) = {sum(1,2)}")
    print(f"max(1,3) = {max(1,3)}")
    print(f"PI = {PI}")
else:
    # 当模块被其他文件导入时（如 import mymath），执行以下提示（可选，可删除）
    print("mymath 模块被成功导入！")

# endregion