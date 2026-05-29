class Duck(object):

    def walk(self):
        print("waddle waddle waddle")

    def swim(self):
        print("splash splash splash")

    def quack(self):
        print("quack quack")


class Penguin(object):

    def walk(self):
        print("waddle, waddle, I waddle too")

    def swim(self):
        print("splash, splash, I swim too")

    def quack(self):
        print("Are you having a laugh? I don't swim")


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()


if __name__ == "__main__":
    donald = Duck()
    test_duck(donald)

    percy = Penguin()
    test_duck(percy)