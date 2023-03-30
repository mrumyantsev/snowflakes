import pygame, simple_draw, random


class Snowflake:
    counter = -1

    def __init__(self, x, y, length, color, factor_a, factor_b, factor_c, speed, wind):
        self.x = x
        self.y = y
        self.past_x = self.past_y = None
        self.length = length
        self.color = color
        self.factor_a = factor_a
        self.factor_b = factor_b
        self.factor_c = factor_c
        self.speed = speed
        self.wind = wind
        self.id = Snowflake.counter
        Snowflake.counter += 1

    def draw(self):
        self.past_x, self.past_y = self.x, self.y
        center = simple_draw.Point(self.past_x, self.past_y)
        simple_draw.snowflake(center=center, length=self.length, color=simple_draw.background_color, factor_a=self.factor_a,
                     factor_b=self.factor_b, factor_c=self.factor_c)
        self.x *= self.wind
        self.y -= self.speed
        center = simple_draw.Point(self.x, self.y)
        simple_draw.snowflake(center=center, length=self.length, color=self.color, factor_a=self.factor_a,
                     factor_b=self.factor_b, factor_c=self.factor_c)


class SnowflakesEngine:
    def __init__(self, resolution=(640, 480), snowflakes_number=10) -> None:
        simple_draw.resolution = resolution
        simple_draw.background_color = (0, 0, 0)

        pygame.init()
        pygame.mouse.set_visible(False)

        self.snowflakes_number = snowflakes_number
        self.snowflakes = []

        for _ in range(self.snowflakes_number):
            self.make_snowflake()
    
    def run(self):
        mouse_moves = 0
        while True:
            i = 0
            while i < self.snowflakes_number:
                self.snowflakes[i].draw()
                if self.snowflakes[i].y < -170:
                    self.snowflakes.pop(i)
                    self.make_snowflake()
                i += 1
            simple_draw.sleep(0.005)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    mouse_moves += 1
                    if mouse_moves > 3:
                        pygame.quit()
                        return
    
    def make_snowflake(self):
        white_bright = random.randint(242, 254)
        snowflake = Snowflake(x=random.randint(-120, simple_draw.resolution[0] + 20),
                            y=simple_draw.resolution[1] + 70 + random.randint(-50, 720),
                            length=random.randint(30, 95),
                            color=(white_bright, white_bright, white_bright),
                            factor_a=random.random(),
                            factor_b=random.random(),
                            factor_c=random.randint(1, 179),
                            speed=random.randint(4, 12),
                            wind=float("1.00" + str(random.randint(1, 3))))
        self.snowflakes.append(snowflake)
