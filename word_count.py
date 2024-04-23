import json
import matplotlib.pyplot as plt


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

    for _, article in articles.items():
        text_split = article["Text"].split()

        date_split = article["Date"].split()
        date = date_split[len(date_split) - 1]

        data_entry = {
            "title": article["Title"],
            "date": date,
            "word_count": len(text_split),
            "char_count": char_count(article["Text"]),
            "char_count_no_space": char_count_no_space(article["Text"]),
        }
        data.append(data_entry)

        if len(data) == 15:
            break

    return data


def map_word_count(data):
    word_counts = list()
    for entry in data:
        word_counts.append(entry["word_count"])
    return word_counts


def map_char_count(data):
    char_counts = list()
    for entry in data:
        char_counts.append(entry["char_count"])
    return char_counts


def map_char_count_no_space(data):
    char_counts_no_space = list()
    for entry in data:
        char_counts_no_space.append(entry["char_count_no_space"])
    return char_counts_no_space


data_2013 = gather_data("articles_2013.json")  # 18
data_2023 = gather_data("articles_2023.json")  # 30

word_count_hist_2013 = map_word_count(data_2013)
char_count_hist_2013 = map_char_count(data_2013)
char_count_no_space_hist_2013 = map_char_count_no_space(data_2013)

word_count_hist_2023 = map_word_count(data_2023)
char_count_hist_2023 = map_char_count(data_2023)
char_count_no_space_hist_2023 = map_char_count_no_space(data_2023)

plt.hist(char_count_no_space_hist_2013)
plt.title("Liczba znaków bez spacji - Elsevier 2013")
plt.show()

plt.hist(char_count_hist_2013)
plt.title("Liczba znaków ze spacjami - Elsevier 2013")
plt.show()

plt.hist(word_count_hist_2013)
plt.title("Liczba wyrazów - Elsevier 2013")
plt.show()

plt.hist(char_count_no_space_hist_2013)
plt.title("Liczba znaków bez spacji - Elsevier 2023")
plt.show()

plt.hist(char_count_hist_2023)
plt.title("Liczba znaków ze spacjami - Elsevier 2023")
plt.show()

plt.hist(word_count_hist_2023)
plt.title("Liczba wyrazów - Elsevier 2023")
plt.show()
