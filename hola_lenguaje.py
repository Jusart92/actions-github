import os


def main():
    language = os.getenv("LANGUAGE")
    print(f"¡Mi lenguaje favorito es: {language}!")


if __name__ == "__main__":
    main()
