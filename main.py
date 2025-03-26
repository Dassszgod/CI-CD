import datetime

def read_product_data(file_path):
    products = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line: 
                continue
            parts = line.split(", ")
            if len(parts) != 3:
                print(f"Некоректний формат рядка: {line}")
                continue
            name, date_str, price = parts
            try:
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                price = float(price)
                products.append((name, date, price))
            except ValueError:
                print(f"Помилка в даних: {line}")
                continue 
    return products

def filter_last_month(products):
    today = datetime.date.today()
    last_month = today - datetime.timedelta(days=30)
    return [p for p in products if p[1] >= last_month]

if __name__ == "__main__":
    data = read_product_data("data.txt")
    last_month_data = filter_last_month(data)
    print("Прочитані дані:", last_month_data)
