import time

def main(n: int = 1):
    if n == 1:
        print("1")
        time.sleep(1)
    else:
        print(f"{n} -> ", end="")
        if (n % 2) == 0:
            main(n // 2)
        else:
            main((n * 3) + 1)

if __name__ == "__main__":
    i = 1
    while True:
        try:
            print(f"=={i}==")
            main(i)
            i += 1
        except KeyboardInterrupt:
            exit(0)
