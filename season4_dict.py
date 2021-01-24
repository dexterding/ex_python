"""第四课，讲述字典与集合"""

import timeit

# 创建字典
d1 = {"name":"victor","age":42,"sex":"man","box":12}
print(d1)

d2 = dict({"name":"victor","age":42,"sex":"man"})
print(d2)

d4 = dict([("name","nike"),("sex","women")])
print(d4)

d5 = dict(name="nike",sex="women")
print(d5)

print(d5.items())

d1_sorted_by_key = sorted(d1.items(),key = lambda x:x[0])
print(d1_sorted_by_key)

#value格式不一致时如何排序
# d1_sorted_by_value = sorted(d1.items(),key = lambda x:x[1])
# print(d1_sorted_by_value)