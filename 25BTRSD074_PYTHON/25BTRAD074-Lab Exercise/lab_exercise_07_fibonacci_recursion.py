# Lab Exercise 7: Fibonacci Series Using Recursion
# Student: Niranjan P G | USN: 25BTRAD074

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def main():
    print("=== Fibonacci Series Generator ===")
    try:
        n_terms = int(input("Enter the number of terms: "))
        if n_terms <= 0:
            print("Please enter a positive integer greater than 0.")
        else:
            print(f"Fibonacci Series ({n_terms} terms):")
            fib_series = [str(fibonacci_recursive(i)) for i in range(n_terms)]
            print(", ".join(fib_series))
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
