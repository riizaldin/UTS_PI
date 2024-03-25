def read_numbers_from_file(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            try:
                number = int(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Non-integer: {line.strip()}")
    return numbers

def format_number_with_commas(number):
    return "{:,.3f}".format(number)

def main():
    filename = 'uts/input.txt'
    numbers = read_numbers_from_file(filename)
    if numbers:
        total_sum = sum(numbers)
        formatted_sum = format_number_with_commas(total_sum)
        print("Hasil penjumlahan dari angka yang ada di file input.txt adalah:", formatted_sum)

if __name__ == "__main__":
    main()
