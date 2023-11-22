import json


def task() -> float:
    summ = 0
    with open("input.json", "r") as reader:
        array_txt = json.load(reader)
        for i in range(len(array_txt)):
            summ += (array_txt[i]["weight"] * array_txt[i]["score"])


        return round(summ, 4)



print(task())
