class Wing(object):
    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1.0:
            print("Weee, this is fun")
        elif self.ratio == 1.0:
            print("This is hard work but I'm flying")
        else:
            print("I think I'll just walk")

class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("waddle waddle waddle")

    def swim(self):
        print("splash splash splash")

    def quack(self):
        print("quack quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def walk(self):
        print("waddle, waddle, I waddle too")

    def swim(self):
        print("splash, splash, I swim too")

    def quack(self):
        print("Are you having a laugh? I don't swim")


# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()


if __name__ == "__main__":
    donald = Duck()
    donald.fly()

    # percy = Penguin()
    # test_duck(percy)