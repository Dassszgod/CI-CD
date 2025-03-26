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

def get_last_two_prices(products, product_name):
    filtered = [p for p in products if p[0] == product_name]
    if len(filtered) < 2:
        print(f"Недостатньо даних для {product_name}")
        return None

    filtered.sort(key=lambda x: x[1]) 
    return filtered[-2:]  



def price_change(products, product_name):
    filtered = [p for p in products if p[0] == product_name]
    if len(filtered) < 2:
        return None

    filtered.sort(key=lambda x: x[1])
    return filtered[-1][2] - filtered[0][2]


if __name__ == "__main__":
    data = read_product_data("data.txt")
    print("Прочитані дані:", data)

    last_two_prices = get_last_two_prices(data, "Apple")
    print("Останні два записи про Apple:", last_two_prices)

    if last_two_prices:
        price_diff = last_two_prices[1][2] - last_two_prices[0][2]
        print("Зміна ціни:", price_diff)

