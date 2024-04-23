import json


def gather_data(file_name):
    file = open(file_name)

    articles = json.load(file)

    data = list()

    for article in articles.items():
        text_split = article["Text"].split()

        data_entry = {
            "title": article["Title"],
            "date": article["Date"][0:4],
            "word_count": len(text_split),
            "char_count": 0,
            "char_count_no_space": 0,
        }
        data.append(data_entry)

    return data


data_2013 = gather_data("articles_2013.json")
data_2023 = gather_data("articles_2023.json")

print(data_2013, "\n")
print(data_2023)
