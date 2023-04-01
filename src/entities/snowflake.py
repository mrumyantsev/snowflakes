import simple_draw as sd


class Snowflake:
    def __init__(self, x=0.0, y=0.0,
                 speed_x=1.0, speed_y=10.0, accel_x=1.5,
                 size=100, color=sd.COLOR_WHITE, trail_color=sd.COLOR_BLACK,
                 factor_a=0.6, factor_b=0.35, factor_c=60.0) -> None:
        self.__x = x
        self.__y = y
        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.__accel_x = accel_x
        self.__size = size
        self.__color = color
        self.__trail_color = trail_color
        self.__factor_a = factor_a
        self.__factor_b = factor_b
        self.__factor_c = factor_c

    def __draw(self, color) -> None:
        point = sd.Point(self.__x, self.__y)

        sd.snowflake(center=point, length=self.__size, color=color,
                     factor_a=self.__factor_a, factor_b=self.__factor_b, factor_c=self.__factor_c)

    def draw(self) -> None:
        self.__draw(self.__color)
    
    def draw_trail(self) -> None:
        self.__draw(self.__trail_color)
    
    def move(self) -> None:
        self.__x += self.__speed_x*self.__accel_x
        self.__y -= self.__speed_y

    @property
    def accel_x(self) -> float:
        return self.accel_x

    @accel_x.setter
    def accel_x(self, value: float) -> None:
        self.__accel_x = value

    @property
    def y(self) -> float:
        return self.__y
