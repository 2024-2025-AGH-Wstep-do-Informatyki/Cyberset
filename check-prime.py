def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def main():
    print('Test pierwszości liczb\nSprawdzone zostaną liczby z zakresu 0-200, wypisane na ekran zostaną tylko te które zdały test pierwszości')
    for n in range(0, 201):
        if isPrime(n):
            print(n)

if __name__ == '__main__':
    main()
    