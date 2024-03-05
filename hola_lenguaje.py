import os

def main():
    lenguaje= os.getenv("LENGUAJE")
    print(f"Hola {lenguaje} desde GitHub")

if __name__ == "__main__":
    main()