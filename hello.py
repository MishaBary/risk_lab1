import typer

def main(
    name: str,
    lastname: str = typer.Option(
        "",
        help="Фамилия пользователя."
    ),
    formal: bool = typer.Option(
        False,
        "--formal",
        "-f",
        help="Использовать формальное приветствие."
    ),
) -> None:

    if formal:
        message = f"Добрый день, {name} {lastname}!"
    else:
        message = f"Привет, {name}!"

    print(message)


if __name__ == "__main__":
    typer.run(main)
