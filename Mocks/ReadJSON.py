import json
with open("hello_frieda.json", mode="r", encoding="utf-8") as read_file:
    frie_data = json.load(read_file)

print(type(frie_data))
print(frie_data["name"])