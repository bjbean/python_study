tip ="""
python字符串示例

1.python语言，可以使用多种引号来引用。
双引号    "this is a string"
单引号    'this is a string'

2.多行文本，使用三个单引号或双引号引用。
var = '''this is a line
         but have multi lines'''

3.文本中含有引号，可在前面使用转义符(\)
var_str='He said:"Are\\'t can\\'t shouldn\\'t would\'t"'

4.字符串嵌入值(%s)
myscore=100
message="I scored %s points"
print(message % myscore)

5.字符串乘法
'A'*5 = 'AAAAA'

"""

print(tip)
print()


print("*"*10,"字符串定义","*"*10)
var_str="this is a string"
print('var_str="this is a string" ')
print("print(var_str)=>",var_str)
print("变量var_str的类型:type(var_str)=",type(var_str))
print()

print("*"*10,"多种引号用法","*"*10)
print("<<<双引号>>>")
var_str="this is a string"
print('var_str="this is a string" ')
print("print(var_str)=>",var_str)
print()

print("<<<单引号>>>")
var_str='this is a string'
print("var_str='this is a string' ")
print("print(var_str)=>",var_str)
print()

print("*"*10,"字符串用法","*"*10)
print("<<<多行文本>>>")
var_str="""this is a string
           but have multi lines"""
print("var_str=",'''"""this is a string
           but have multi lines""" ''')
print("print(var_str)=>",var_str)
print()

print("<<<包含单引号>>>")
var_str="this'is a string"
print('''var_str="this'is a string" ''')
print("print(var_str)=>",var_str)
print()

print("<<<包含双引号>>>")
var_str='this"is a string'
print("""var_str='this"is a string'""")
print("print(var_str)=>",var_str)
print()

print("<<<使用转义符>>>")
var_str='He said:"Are\'t can\'t shouldn\'t would\'t"'
print("""var_str='He said:"Are\\'t can\\'t shouldn\\'t would\\'t"'""")
print("print(var_str)=>",var_str)
print()

print("<<<字符串占位符>>>")
myscore=100
print("myscore=100")
message="I scored %s points"
print('message="I scored %s points"')
print("print(message % myscore)=>",message % myscore)
print()

print("<<<字符串乘法>>>")
var_str = 'A'
print("var_str = 'A'")
print("print(var_str*10)=>",var_str*10)
print()
