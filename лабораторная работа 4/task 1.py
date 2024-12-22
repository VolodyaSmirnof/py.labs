import json

def calculate_sum_of_products(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    total_sum = 0
    for item in data:
        score = float(item['score'])
        weight = float(item['weight'])
        total_sum += score * weight
    return round(total_sum, 3)

if __name__ == "__main__":
    try:
        with open("test_data.json", "r") as outfile:
              pass # If file exists, do nothing
    except FileNotFoundError:
          with open("test_data.json", "w") as outfile:
             json.dump(test_data, outfile)

    input_file_path = "input.json"
    test_file_path = "test_data.json"
    sum_of_products_input = calculate_sum_of_products(input_file_path)
    if sum_of_products_input is not None:
        print(f"{sum_of_products_input}")

