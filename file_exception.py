path = "C:/Users/Fatoom/Documents/text_files/numbers1.txt"
try:
    with open(path) as f:
        lines = f.readlines()
        print(lines)
        numbers = [line.strip() for line in lines]
        sum = 0
        for number in numbers:
            try:
                sum += int(number)
            except ValueError as e:
                print(f"{number} is not an integer")
        print(sum)
        f.close()
except FileNotFoundError as e:
    print(f"File not found {e}")
except ValueError as e:
    print(f"It should be number {e}")