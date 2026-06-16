def greet(name: str) -> str:
    return f"hello, {name}"


def main() -> None:
    name: str = input("enter your name: ")
    print(greet(name))


if __name__ == "__main__":
    main()
