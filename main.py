import requests
import json

api_key = "7e9c35d9d78f7e34567e6e4eef3ce6c1"
base_url = "https://api.elsevier.com/content/search/sciencedirect"

query = "(KEY artificial intelligence)"
url = f"{base_url}?apiKey={api_key}&query={query}&date=2023&count=100"

response = requests.get(url)

doi_list = []

if response.status_code == 200:
    data = response.json()
    entries = data["search-results"]["entry"]
    for entry in entries:
        doi_list.append(entry["prism:doi"])
else:
    print(f"Error: {response.status_code}")

articles = dict()

for doi in doi_list:
    article_retrieval_url = f"https://api.elsevier.com/content/article/doi/{doi}?apiKey={api_key}&httpAccept=application%2Fjson"

    article_retrieval_response = requests.get(article_retrieval_url)
    if article_retrieval_response.status_code == 200:
        data = article_retrieval_response.json()
        article = data["full-text-retrieval-response"]
        article_core_data = article["coredata"]

        articleOAFlag = article_core_data["openaccess"]
        if articleOAFlag == "1":
            imageCount = 0

            articleObjects = article["objects"]["object"]
            for object in articleObjects:
                if (
                    object["@category"] == "standard"
                    and object["@mimetype"] == "image/jpeg"
                ):
                    imageCount += 1

            valid_article = {
                "Title": article_core_data["dc:title"],
                "Date": article_core_data["prism:coverDisplayDate"],
                # "Text": article["originalText"],
                "Images": imageCount,
            }

            articles[doi] = valid_article

            if len(articles) == 30:
                break

    else:
        print(f"Error", {article_retrieval_response.status_code})

articles_json = json.dumps(articles, indent=4)

print(articles_json)

"""
art2013 = "articles_2013.json"
art2023 = "articles_2023.json"
"""

art_img_2023 = "articles_img_2023.json"

with open(f"files/{art_img_2023}", "w") as file:
    file.write(articles_json)
