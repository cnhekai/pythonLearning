# 这是一个“元组”，类似于list，但是元组不能赋值，相当于只读列表
tuple = ('python','is','very','cool')
tuple2 = ('javascript','is','also')
print(tuple) # 输出完整元组
print(tuple[2]) # 输出tuple的第三个元素
print(tuple[1:]) # 输出tuple的第二个元素之后的所有元素
print(tuple[-3:]) # 输出tuple倒数第三个元素及之后的所有元素
print(tuple * 2) # 输出两次tuple
print(tuple + tuple2) # 输出tuple和tuple2合并之后的元组

list = ['python','is','very','cool']

list[-1] = 'strong'
print(list[-1]) # 修改list的值并输出，这样是合法的
# 不能修改元组里面的值
# tuple[-1] = 'strong'
# print(tuple[-1])