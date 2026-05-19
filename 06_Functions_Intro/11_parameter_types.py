def func(p1, p2, *args, k, **kwargs):
    print(f"Positional-or-keyword:...{p1}, {p2}")
    print(f"var-positional (*args):...{args}")
    print(f"keyword-only (k):...{k}")
    print(f"var-keyword (**kwargs):...{kwargs}")


func(1, 2, 3, 4, 5, k=6, key1 = 7, key2=8)