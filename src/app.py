import random

from pyfiglet import Figlet, FigletFont


def main():
    fonts = FigletFont.getFonts()
    f = Figlet(font=random.choice(fonts))
    print(f.renderText("Hello World"))


if __name__ == "__main__":
    main()
