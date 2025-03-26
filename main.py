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

if __name__ == "__main__":
    data = read_product_data("data.txt")
    print("Прочитані дані:", data)
