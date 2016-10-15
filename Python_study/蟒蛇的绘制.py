import turtle
def drawSnake(rad,angle,len,neckrad):
    for i in  range(len):
        turtle.circle(rad,angle)#描述rad描述圆形轨迹半径的位置，爬行弧度值
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rad)#直线爬行
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300,800,0,0)#1300宽度800高度，左上角坐标位置
    pythonsize = 30#乌龟运行轨迹的宽度
    turtle.pensize(pythonsize)#变量参数
    turtle.pencolor("blue")#小乌龟的颜色，使用RGB配色
    turtle.seth(-40)#运动方向，角度值0东，90北，180西，270南 复数为相反方向
    drawSnake(40,80,5,pythonsize/2)#开始绘制，绘制参数
main ()