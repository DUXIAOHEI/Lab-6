class Figure:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def volume(self):
        """方法1：计算体积 V = a * b * c"""
        return self.a * self.b * self.c
    
    def __add__(self, other):
        """重载加法运算符"""
        if type(self) != type(other):
            raise TypeError("对象类型不同，不能相加")
        return Figure(self.a+other.a, self.b+other.b, self.c+other.c)
    
    def __str__(self):
        return f"图形: 尺寸={self.a}x{self.b}x{self.c}, 体积={self.volume()}"


class HollowBody(Figure):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.d = d  # 壁厚
    
    def solid_volume(self):
        """方法2：计算减去内腔后的实体体积"""
        a_inner = max(0, self.a - self.d)
        b_inner = max(0, self.b - self.d)
        c_inner = max(0, self.c - self.d)
        return self.volume() - (a_inner * b_inner * c_inner)
    
    def __str__(self):
        return f"带内腔实体: 外尺寸={self.a}x{self.b}x{self.c}, 壁厚={self.d}, 实体体积={self.solid_volume()}"


class FigureArray(Figure):
    def __init__(self, a, b, c, count):
        super().__init__(a, b, c)
        self.count = count  # 图形数量
    
    def total_volume(self):
        """方法2：计算多个相同图形的总体积"""
        return self.volume() * self.count
    
    def __str__(self):
        return f"图形数组: 单个尺寸={self.a}x{self.b}x{self.c}, 数量={self.count}, 总体积={self.total_volume()}"


# 简单的演示代码
if __name__ == "__main__":
    # 创建并显示Figure对象
    fig = Figure(2, 3, 4)
    print(fig)
    
    # 创建并显示HollowBody对象
    hollow = HollowBody(10, 8, 6, 1)
    print(hollow)
    
    # 创建并显示FigureArray对象
    array = FigureArray(2, 3, 4, 5)
    print(array)
    
    # 测试运算符重载
    print("\n测试运算符重载:")
    
    fig1 = Figure(1, 2, 3)
    fig2 = Figure(1, 2, 3)
    
    try:
        result = fig1 + fig2
        print(f"fig1 + fig2 = {result}")
    except TypeError as e:
        print(f"错误: {e}")
    
    # 测试不同类型相加
    try:
        invalid = fig + hollow
    except TypeError as e:
        print(f"Figure + HollowBody 错误: {e}")