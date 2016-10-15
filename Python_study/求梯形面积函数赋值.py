def trapezoid_area(base_up,base_down,height):#创建名为trapezoid_area的新函数
    return 1/2 * (base_up + base_down) * height #梯形面积公式
#print(trapezoid_area(1,2,3)) #传递参数方法一、位置参数
#print(trapezoid_area(base_up=1,base_down=2,height=3)) #传递参数方法二、关键词参数
print("输入上底：")
base_up = float(input())#传递参数方法三，参数转换为变量，浮点数输入
print("输入下底：")
base_down = float(input())
print("输入高：")
height = float(input())
print(trapezoid_area(base_up,base_down,height))#方法三，参数调用输入的浮点数
#创建的函数的参数只是形式上的占位符，可用其他变量替代