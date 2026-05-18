def banner_text(text: str = " ", banner_width: int = 80) -> None:
    """ Print a string centred, with ** either side.

    :param text: The string to print.
        An asterisk (*) will result in a row of asterisks.
        The default will print a blank line, with a ** border at
        the left and right edges.
    :param banner_width: The overall width to print within
        (including the 4 spaces for the ** either side).
    :raises ValueError: if the supplied string is too long to fit.
    """
    text = str(text).rstrip("\n")

    if len(text) > banner_width - 4:
        raise ValueError(f"String {text} is larger than specified width {banner_width - 4}")

    if text == "*":
        print("*" * banner_width)
        return

    output_string = f"**{text.center(banner_width - 4)}**"
    print(output_string)


banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,")
banner_text(banner_width=79)
banner_text("When you're feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And... always look on the bright side of life...")
banner_text("*")
