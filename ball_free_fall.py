# 导入数学库，用于计算平方根
import math

# 定义重力加速度，单位为 m/s^2
g = 9.8

# 定义初始高度，单位为米
h0 = 100

# 定义函数，用于计算第 n 次反弹的高度
def bounce_height(n):
    """
    此函数计算第 n 次反弹的高度
    :param n: 反弹的次数
    :return: 第 n 次反弹的高度
    """
    return h0 / (2 ** n)

# 定义函数，用于计算球在第 n 次反弹时经过的总路程
def total_distance(n):
    """
    此函数计算球在第 n 次反弹时经过的总路程
    :param n: 反弹的次数
    :return: 球在第 n 次反弹时经过的总路程
    """
    if n == 0:
        return h0
    # 初始高度
    distance = h0
    # 后续每次反弹的路程是反弹高度的 2 倍
    for i in range(1, n + 1):
        distance += 2 * bounce_height(i)
    return distance

# 定义函数，用于计算球在第 n 次反弹时运动的总时间
def total_time(n):
    """
    此函数计算球在第 n 次反弹时运动的总时间
    :param n: 反弹的次数
    :return: 球在第 n 次反弹时运动的总时间
    """
    # 第一次下落的时间
    time = math.sqrt(2 * h0 / g)
    # 后续每次反弹和下落的时间
    for i in range(1, n + 1):
        h = bounce_height(i)
        # 每次反弹和下落的时间是相同的
        time += 2 * math.sqrt(2 * h / g)
    return time

# 计算第 10 次反弹的相关信息
n1 = 10
height1 = bounce_height(n1)
distance1 = total_distance(n1)
time1 = total_time(n1)

print(f"第 {n1} 次掉下并反弹到最高点时，反弹高度为 {height1:.2f} 米，一共经过 {distance1:.2f} 米，运动了 {time1:.2f} 秒。")

# 计算第 n 次反弹的相关信息
n = int(input("请输入要计算的反弹次数 n: "))
height = bounce_height(n)
distance = total_distance(n)
time = total_time(n)

print(f"第 {n} 次掉下并反弹到最高点时，反弹高度为 {height:.2f} 米，一共经过 {distance:.2f} 米，运动了 {time:.2f} 秒。")    