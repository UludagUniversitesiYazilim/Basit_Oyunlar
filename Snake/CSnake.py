from Snake import Apple
import time


class Snake(object):

    def __init__(self):
        self.__speed = 3
        self.__direction = (0, 0)
        self.__tail_coords = [[1, 0], [0, 0]]
        self.__apple = self.new_apple()
        self.__score = 0

        self.start_time = time.time()


    def set_score(self, point):
        self.__score += point

    @property
    def get_score(self):
        return self.__score

    @property
    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed += speed

    @property
    def get_direction(self):
        return self.__direction

    def set_direction(self, x, y):
        self.__direction = (x, y)

    @property
    def get_coordinates(self):
        return self.__tail_coords

    @property
    def get_apple(self):
        return self.__apple

    def move_snake(self):
        # [[2,3], [2,4], [2,5]]
        x = self.__direction[0]
        y = self.__direction[1]

        temp = self.__tail_coords[0][:]

        length = len(self.__tail_coords)

        self.__tail_coords[0][0] = (x + self.__tail_coords[0][0]) % 55
        self.__tail_coords[0][1] = (y + self.__tail_coords[0][1]) % 55

        if self.check_crash():
            return -1

        foo = 1
        while foo < length:
            temp2 = self.__tail_coords[foo][:]
            self.__tail_coords[foo] = temp
            temp = temp2
            foo += 1

        if self.find_apple():
            self.eat()
            self.__apple = self.new_apple()
            self.calculate_score()

    def calculate_score(self):
        eat_time = time.time()
        add_score = int(1/(eat_time - self.start_time) * 100)
        self.set_score(add_score)
        self.start_time = eat_time

    def eat(self):  # TODO: Duzelt
        t = self.__tail_coords
        self.set_speed(1)
        if self.get_direction == (1, 0):
            t.append([(t[-1][0] - 1), (t[-1][1])])
        elif self.get_direction == (-1, 0):
            t.append([(t[-1][0] + 1), (t[-1][1])])
        elif self.get_direction == (0, 1):
            t.append([(t[-1][0]), (t[-1][1] - 1)])
        elif self.get_direction == (0, -1):
            t.append([(t[-1][0]), (t[-1][1] + 1)])

    def find_apple(self):
        coords = self.get_apple.coords

        if self.__tail_coords[0] == list(coords):
            return True
        else:
            return False

    @staticmethod
    def new_apple():
        return Apple.Apple()

    def check_crash(self):
        head = self.__tail_coords[0]
        li = self.__tail_coords[1:]

        if head in li:
            return True
        else:
            return False
