import datetime

days = int(input("Masukkan sebuah angka: "))

current_date = datetime.date.today()
future_date = current_date + datetime.timedelta(days=days)
formatted_date = future_date.strftime("%A on %d %B %Y")

print("{} hari dari sekarang akan berada di: \n{}".format(days, formatted_date))