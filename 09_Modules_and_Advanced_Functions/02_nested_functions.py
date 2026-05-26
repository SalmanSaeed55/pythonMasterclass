def greet_python(items: list) -> None:
    # nonlocal greeting = "Hello" Causes error due to inner func being able to access both named vars
    def make_greeting(item: str) -> str:
        greeting = "Hi"
        return f'{greeting}, {item}!'

    for item in items:
        print(make_greeting(item))

    print(f"Inside greet_python, `greeting` is: {greeting}")


names = ["John", "Eric", "Graham", "Terry", "Terry", "Micheal"]

greet_python(names)
