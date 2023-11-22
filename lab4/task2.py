
import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:


    array = []
    with open(INPUT_FILENAME) as input_csv:
        reader = csv.DictReader(input_csv)
        for i in reader:
            array.append(i)

    with open(OUTPUT_FILENAME, "w") as output_json:
        json.dump(array, output_json, indent=4, ensure_ascii=True)
    # print(type(reader))



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
