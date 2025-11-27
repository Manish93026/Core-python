def fibonacci_sum(n: int) -> int:
    a, b = 0, 1
    total = 0
    for _ in range(n):
        total += a
        a, b = b, a + b
    return total

# Example usage:
n = 10
print(f"Sum of first {n} Fibonacci numbers:", fibonacci_sum(n))
