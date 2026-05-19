import colorama

# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def colour_print(text: str, *effects: str) -> None:
    """Prints text in the terminal.
    :param text: The text to print.
    :param effects: The effect to be printed.
    """
    effect_string = "".join(effects)
    output_string = f"{effect_string}{text}{RESET}"
    print(output_string)


colorama.init()

print("This is the default terminal colour")
colour_print("Hello, Blue", BLUE, REVERSE)
colour_print("Hello, Blue", BLUE, REVERSE, UNDERLINE)
colour_print("Hello, Blue", BLUE)
colour_print("Hello, Green", GREEN)
colour_print("Hello, Yellow", YELLOW)
colour_print("Hello, Black", BLACK)
colour_print("Hello, Red in bold", RED, BOLD)
colour_print("Hello, Red in bold", RED)
colour_print("Hello, Magenta", MAGENTA)
colour_print("Hello, CYAN", CYAN)
colour_print("Hello, White", WHITE)
colour_print("Hello, Reset", RESET)
colour_print("Hello, BOLD", BOLD)
colour_print("Hello, UNDERLINE", UNDERLINE)
colour_print("Hello, REVERSE", REVERSE)

colorama.deinit()