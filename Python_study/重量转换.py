def g_kg(g): #创建新函数组
    kg = g / 1000 #克向千克转换关系式
    return str(kg) + 'kg' #循环输出
#k = g_kg(1200)#调用函数参数为1200
print("请输入你要转换的数字")
g = float(input())
print(g_kg(g))#输出
