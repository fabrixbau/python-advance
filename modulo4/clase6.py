def fibonacci(n):
    fib_series = [0, 1]

    while len(fib_series) < n:
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)

    return fib_series


if __name__ == '__main__':
    prompt = "Ingrese el número de dígitos de la serie Fibonacci a calcular: "
    n = int(input(prompt))
    serie = fibonacci(n)
    print("SERIE FIBONACCI DE LOS ", n, " NÚMEROS : ")
    for s in serie:
        print(s)
