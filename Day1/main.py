from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, features="html.parser")
print(soup.title.string)

all_anchor_tags = soup.findAll(name="a")

for tag in all_anchor_tags:
    print(tag.get("href"))

company_url = soup.select_one(selector="p a")
print(company_url)
