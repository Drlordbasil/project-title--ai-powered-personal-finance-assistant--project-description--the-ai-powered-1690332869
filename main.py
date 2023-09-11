Commit: Optimize Python script
```
# Renamed function to follow Python naming conventions


def optimize_script(numbers):
    # Calculated squares using a generator expression instead of a list comprehension to save memory
    squares = (num * num for num in numbers)

    # Replaced enumerate with a range-based loop for improved performance
    for idx in range(len(squares)):
        num = next(squares)
        # Used formatted string literals for string formatting
        print(f"The square of number at index {idx} is {num}")


```
