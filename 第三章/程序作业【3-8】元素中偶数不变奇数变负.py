numbers = [3, 8, 2, 5, 12]
processed = [n if n % 2 == 0 else -n for n in numbers]
print(processed)