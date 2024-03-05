import os

def main():
    nombre = os.getenv("USERNAME")
    print(f"hello {nombre} mundo desde GitHub")

if __name__ == "__main__":
    main()