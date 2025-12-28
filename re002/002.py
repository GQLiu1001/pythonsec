# 数据容器
# 列表 list 
# 字符串 str
# 元组 tuple
# 集合 set
# 字典 dict

# region 列表 list
# 简单创建
num_list = []
a = [1,3,"str"]
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