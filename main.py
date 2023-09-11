Commit: Optimize Python script
```
# Used meaningful variable names


def optimize_script(numbers):
    # Removed unnecessary comments
    squares = [num * num for num in numbers]  # Calculate squares of numbers

    # Used enumerate
    for idx, num in enumerate(squares):
        # Used f-strings for string formatting
        print(f"The square of number at index {idx} is {num}")


```
**Note**: This is a basic optimization example. Depending on the specific requirements and context of the script, further optimizations and improvements may be possible.
