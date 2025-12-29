# 数据容器
# 列表 list 
# 字符串 str
# 元组 tuple
# 集合 set
# 字典 dict

# region 列表 list
# 简单创建
num_list = []

ccc:list[int] = [1,2,3]
a:list[int | str] = [1,3,"str"]

for i in a :
    print(i)
# 修改
a[2] = 1
print(a[2])
# 删除
del(a[2])
# print(a[2])
# 列表的切片 s[start:end:step] end默认-1(最后一个元素索引)
# 常用方法
# append(元素) 列表尾部增加元素
a.append(3)
# insert(index,元素) index前加一个元素
# pop(index) pop() 删除index位置元素 默认最后一个
# sort() 排序
# reverse() 反转
# len(xxx) 获取xxx长度
len(a)
# 两个不同列表合并可以 num_list1 + num_list2 也可以 [*num_list1 , *num_list2] 解包 
# 快速判断存不存在于列表中 in
# ("大于" if int(number) >= 30 else "小于")
print(f"3 {("在" if 3 in a else "不在")} 列表 a 中")
# 按一定规则快速生成一个列表
# 列表推导式 num_list = [ (i*2) for i in data ]
# 列表推导式 num_list = [ (i*2) for i in data if i > 3]
num_list = [i*2 for i in range(10)]
num_list2 = [i*2 for i in range(10) if i > 3]
print(num_list)
print(num_list2)
# endregion

# region 字符串 有序不可变
# 也有切片
# s[start:end:step] end默认-1(最后一个元素索引)
s = "hello"
print(s[3])
print(s.index("l"))
print(s.find("l"))
print(s.find("xx"))
# find(子串) 返回子串第一次出现的索引 没有 -1
# index(子串) 返回子串第一次出现的索引 没有 报错
# count(子串) 返回子串出现次数
# upper() 全大写
# lower() 全小写
# spilt(子串) 按子串分割
# strip() strip(子串) 去掉两端空白字符/字串
# repalce(目标子串,新串) 将目标子串换为新串
# startwith(子串)
# endwith(子串)
# endregion

# region 元组 tuple 一旦定义不能修改

t1:tuple[int] = (1,3,4,5,4)

# 定义空元组
t2 = ()
t3 = tuple()
t4 = ("s","s","ss","sss")
# count(子串) 返回子串出现次数
# index(子串) 返回子串第一次出现的索引 没有 报错
print(t4.count("s"))
# 也可以切片
# s[start:end:step] end默认-1(最后一个元素索引)
a,b,c,d,e = t1 # 解包
a,*b = t1 # 解包 b接受剩余所有元素
*a,b = t1 # 解包 a接受除了最后一个剩余所有元素
print(a)
# endregion

# region 集合 set 自动去重
# 无序 不支持索引访问
# 无序

s1:set[int] = {1,3,3,4,6,7,3,1,2,0} # 自动去重

# 不能空大括号 -> 是字典 dict
# 空集合
s2 = set()
# add(元素) 添加元素 无序
# remove(元素) 删除元素 没有则报错
# pop() 随机删除元素
# clear() 清空
# set1.difference(set2) 求俩集合差集(s1有 s2没有)
# set1.union(set2) 求俩集合并集
# set1.intersection(set2) 求俩集合交集
a = 3 in s1
print(a)
s1.add(100)
s1.add(200)
s1.add(300)
# {0, 1, 2, 3, 4, 6, 7, 200, 100, 300}
print(s1)
# endregion

# region 字典 Map 键值对
# key 不能重复可以修改

dict1:dict[str,int] = {"a":1 , "b":3}

dict2 = {}
dict3 = dict()
# 如果没有会报错
print(dict1["a"])
# 增加
dict1["d"] = 99
# 删除加获取v
deleted_value = dict1.pop("a")
print("deleted_value = %s" % deleted_value)
# 删除
del(dict1["b"])
print(dict1)

dict1["d"]
dict1.get("d")
dict1.keys
dict1.values
dict1.items
# 遍历 keys values items

