def calculate_product(num):
    product = 1
    for i in range(1, num + 1):
        product *= i
    return product

def main():
    try:
        num = int(input("Masukkan sebuah angka: "))
        if num < 0:
            print("Masukkan bilangan bulat non-negatif.")
        else:
            result = calculate_product(num)
            print("Hasil perkalian dari angka 1 -",num, "adalah:", result)
    except ValueError:
        print("Masukkan bilangan bulat yang valid.")

if __name__ == "__main__":
    main()
