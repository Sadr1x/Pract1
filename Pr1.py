import math


def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


def area_circle(r):
    return math.pi * r * r


def area_rectangle(w, h):
    return w * h


def area_triangle(b, h):
    return 0.5 * b * h


def structures_demo():
    nums = [1, 2, 3, 4, 5]
    nums.append(6)
    evens = [x for x in nums if x % 2 == 0]

    point = (3, 4)
    dist = math.sqrt(point[0] ** 2 + point[1] ** 2)

    grades = {"Олег": 90, "Анна": 85, "Ігор": 78}
    grades["Марія"] = 95

    print("Список:", nums)
    print("Парні зі списку:", evens)
    print("Кортеж:", point, "Відстань:", round(dist, 2))
    print("Словник:", grades)


class Countdown:
    def __init__(self, start):
        self.num = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < 0:
            raise StopIteration
        cur = self.num
        self.num -= 1
        return cur


def gen_squares(n):
    for i in range(1, n + 1):
        yield i * i


def iter_gen_demo():
    print("Ітератор:", list(Countdown(5)))
    print("Генератор квадратів:", list(gen_squares(5)))


def main():
    while True:
        print("\n1 - Факторіал")
        print("2 - Площа фігури")
        print("3 - Список, кортеж, словник")
        print("4 - Ітератор і генератор")
        print("0 - Вихід")

        cmd = input("Вибір: ")

        if cmd == "1":
            n = int(input("n: "))
            print("Результат:", factorial(n))
        elif cmd == "2":
            fig = input("Фігура (circle / rectangle / triangle): ")
            if fig == "circle":
                r = float(input("Радіус: "))
                print("Площа:", round(area_circle(r), 2))
            elif fig == "rectangle":
                w = float(input("Ширина: "))
                h = float(input("Висота: "))
                print("Площа:", round(area_rectangle(w, h), 2))
            elif fig == "triangle":
                b = float(input("Основа: "))
                h = float(input("Висота: "))
                print("Площа:", round(area_triangle(b, h), 2))
            else:
                print("Невідома фігура")
        elif cmd == "3":
            structures_demo()
        elif cmd == "4":
            iter_gen_demo()
        elif cmd == "0":
            break
        else:
            print("Невірний вибір")


main()
