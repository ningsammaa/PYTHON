# List of integers
integers = [4, 5, 45, 6, 87, 50, 66, 90, 2, 7, 8]


integers.sort()


if any(num <= 0 for num in integers):
    print("Please enter positive integers only.")
else:

    even_numbers = [num for num in integers if num % 2 == 0]
    print(f"The even numbers are:{even_numbers}")

    
    odd_numbers = [num for num in integers if num % 2 != 0]
    print(f"The odd numbers are: {odd_numbers}")

    
    def is_prime(num):
        """
        Check if a number is prime.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_numbers = [num for num in integers if is_prime(num)]
    print(f"The prime numbers are: {prime_numbers}")
