# 模块
# region 模块 同一个包直接导
# 1. 测试 import mymath 方式（不受 __all__ 影响）
import mymath
print("通过 import mymath 访问 PI：", mymath.PI)  # 正常输出 3.14
print("通过 import mymath 访问 max：", mymath.max(1,3))  # 正常输出 3

# 2. 测试 from mymath import * 方式（受 __all__ 影响）
from mymath import *
# 从使用效果上看，几乎等同于将模块内符合条件的成员 变成当前文件的本地成员
print("通过 from mymath import * 访问 max：", max(1,3))  # 正常输出 3（__all__ 包含 max）
# print("通过 from mymath import * 直接访问 PI：", PI)  # 报错！NameError: name 'PI' is not defined
# 但仍可通过 模块名.成员名 访问 PI
print("通过 from mymath import * 后，用 mymath.PI 访问：", mymath.PI)  # 正常输出 3.14