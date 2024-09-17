def fibonacci_sequence(num):
    fibonacci = [0, 1]
    while fibonacci[-1] < num:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if num in fibonacci:
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} não pertence à sequência de Fibonacci.")

num = int(input("Informe o número para calcular a sequência de Fibonacci: "))
fibonacci_sequence(num)