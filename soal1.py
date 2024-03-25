import datetime

def main():
    current_year = datetime.datetime.now().year
    
    days_in_year = 366 if is_leap_year(current_year) else 365
    
    whole_number = int(input("Masukkan bilangan bulat: "))
    
    result = whole_number / days_in_year

    formatted_result = "{:.11f}".format(result)
    print("Hasil:", formatted_result)

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == "__main__":
    main()
