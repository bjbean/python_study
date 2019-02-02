tip ="""
python列表学习笔记

1.列表是python语言中的一种数据类型，可用来保存多个变量。
var_list=["变量1","变量2","变量3"]
var_list=[1,2,3]
var_list=[1,"变量2"，3]  //甚至是不同的数据类型变量

2.索引位置。列表中的元素可通过索引位置访问，它是从0开始进行索引的。
var_list=[1,2,3,4,5]
var_list[0] => 1
var_list[1] => 2
var_list[2:4] => [3, 4]  //从索引位置2开始访问，访问到索引位置4(不含)
var_list[-1] => 5        //访问列表最后的元素

3.列表操作
var_list=[1,2,3]
(1).添加元素
  var_list.append(4)
(2).删除元素
  del var_list[4]
(3).查看列表元素个数
  len(list)

4.列表算术
(1).列表加法:相当于把两个列表合并
list1=[1,2]
list2=[3,4]
list1+list2 => [1,2,3,4]
(2).列表乘法:相当于重复列表元素
var_list=[1,2]
var_list*3 => [1,2,1,2,1,2]  //重复3次
(3).列表减法、除法:不支持，会报错

5.扩展知识
查看列表支持的其他函数或方法：dir(list)
"""

print(tip)
print()

print("*"*10,"列表定义","*"*10)
var_list=["变量1","变量2","变量3"]
print('var_list=["变量1","变量2","变量3"]')
print("print(var_list)返回",var_list)
print("变量var_list的类型:type(var_list)=",type(var_list))
print()

print("*"*10,"列表访问","*"*10)
var_list=[1,2,3,4,5]
print('var_list=[1,2,3,4,5]')
print("访问索引位置0的元素 var_list[0] =>",var_list[0])
print("访问索引位置1的元素 var_list[1] =>",var_list[1])
print("访问索引位置最后的元素 var_list[-1] =>",var_list[-1])
print("访问索引位置2-4的元素 var_list[2:4] =>",var_list[2:4])
print()

print("*"*10,"列表操作","*"*10)
var_list=[1,2,3]
print("var_list=[1,2,3]")
var_list.append(4)
print("添加元素:var_list.append(4)")
print("添加后的结果:",var_list,"元素个数len(var_list)=>",len(var_list))
del var_list[2]
print("删除元素:del var_list[2]")
print("添加后的结果:",var_list,"元素个数len(var_list)=>",len(var_list))
print()

print("*"*10,"列表算术","*"*10)
list1=[1,2]
print("list1=[1,2]")
list2=[3,4]
print("list2=[3,4]")
print("列表加法: list1+list2 =>",list1+list2)
print("列表乘法: list1*3 =>",list1*3)
print()

print("*"*10,"扩展知识","*"*10)
print("查看列表支持的属性、函数等:dir(list)或dir(var_list) =>")
print(dir(list))

