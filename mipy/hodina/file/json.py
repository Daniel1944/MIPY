import  json

path = "C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\bibliography.json"

with open(path, "r") as f:
    bib = json.load(f)
def print_bib_entry_nicely(entry):
    authors = entry["author"]
    for author in authors:
        print("{}, {}., ").format(author["family"], author["given"][0])

print_bib_entry_nicely(bib[0])