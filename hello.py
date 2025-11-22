#smth
import typer

def main(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Использовать формальное приветствие."),
):
    """
    Говорит "Привет" пользователю, опционально используя фамилию и формальный стиль.
    """
    if formal:
        print(f"Добрый день, {name} {lastname}!")
    else:
        print(f"Привет, {name}!")

if __name__ == "__main__":
    typer.run(main)


"""print ("Hello    appsec   world")

for i in [  "Hello" ,   "appsec", "world"   ]:
        print(i),

import sys
def run():
	name="appsec"
	sys.stdout.write("Hello "+ name +" world")
run()

#what does dirty code mean?
#does it mean that the code is not formatted correctly?

name = input("Enter your name: ")
print(f"Hello appsec world from @{name}")

"""
