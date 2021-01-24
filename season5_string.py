"""第五讲：操作字符串"""

l = []
print(type(l))

for i in range(1,3):
    l.append(str(i))
    print(l)
print(l)
print(type(l))

#列表通过join，把所有元素连接起来，变为string
l1= "".join(l)
print(l1)
print(type(l1))

#split，切割字符串
path = "F:\\Program Files (x86)\Youdao\\YoudaoNote\res\Group\\"
print(type(path))
path1 =path.split("\\")
print(path1)
print(path)

path2 =path.split("\\")[1].split("x86")[1]
print(path2)

#strip 消除2端的字符

strip1 = " www.baidu.com "
strip2 = strip1.strip(" ")
print(strip2)

#format 在log的使用
id ="id20389"
name = "jack"
print("find something id:{},and name is{}".format(id,name))