import json


def char_count(text):
    count = 0
    for _ in text:
        count += 1
    return count


def char_count_no_space(text):
    count = 0
    for char in text:
        if char != " ":
            count += 1
    return count


def gather_data(file_name):
    file = open(file_name)

    articles = json.load(file)

    data = list()

    for key, article in articles.items():
        text_split = article["Text"].split()

        data_entry = {
            "title": article["Title"],
            "date": article["Date"],
            "word_count": len(text_split),
            "char_count": char_count(article["Text"]),
            "char_count_no_space": char_count_no_space(article["Text"]),
        }
        data.append(data_entry)

    return data


data_2013 = gather_data("articles_2013.json")
data_2023 = gather_data("articles_2023.json")

print(data_2013, "\n")
print(data_2023)
