def san(A,B): #创建函数
    C = A * A + B * B
    import math #载入模块
    return 'The right triangle third side\'s length is ' + str(math.sqrt(C)) #调用开根模块取C的根
#san(1,2)
A = float(input())
B = float(input())
print(san(A,B))#输出函数
import math