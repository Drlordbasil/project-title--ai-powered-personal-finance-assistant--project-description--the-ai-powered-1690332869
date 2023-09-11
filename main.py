Commit: Remove unnecessary generator expression and use a zip-based loop

```python


def optimize_script(numbers):
    # Replaced generator expression with a zip-based loop for improved readability
    for idx, num in enumerate(numbers):
        # Calculated squares using the power operator instead of multiplication
        square = num ** 2
        # Used formatted string literals for string formatting
        print(f"The square of number at index {idx} is {square}")


```

This updated code removes the unnecessary generator expression and uses a zip-based loop instead. The squares of the numbers are now calculated using the power operator(`**`) instead of multiplication. Finally, the code continues to use formatted string literals for string formatting.
