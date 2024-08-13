def fizzBuzz(n: int):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(i))
    return result


def main():
    try:
        n = int(input("Введите значение n: "))
        if n < 1:
            print("Пожалуйста, введите положительное целое число.")
            return
        fizz_buzz_result = fizzBuzz(n)
        print("Результат FizzBuzz:")
        for item in fizz_buzz_result:
            print(item)
    except ValueError:
        print("Пожалуйста, введите целое число.")


if __name__ == "__main__":
    main()