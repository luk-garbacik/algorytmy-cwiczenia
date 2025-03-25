from datetime import datetime

zadana_data = datetime.strptime(input("Podaj datę w formacie rrrr-mm-dd: "), '%Y-%m-%d')

roznica = datetime.now() - zadana_data

print("Liczba dni od zadanej daty do daty aktualnej:", roznica.days)