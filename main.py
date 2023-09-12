import os


def main():
    
    username = os.getenv("USERNAME")
    greeting = f'Hola {username}'

    print(greeting)


if __name__ == "__main__":
    main()
