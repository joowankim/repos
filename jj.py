import json



URL = "myapp/item/fixtures/"
item_data = URL + "item-data.json"
ingredient_data = URL + "ingredient-data.json"

with open(ingredient_data, 'r', encoding='utf-8') as ingredients, open(item_data, 'r', encoding='utf-8') as items:
    ingredient_data = json.load(ingredients)
    item_data = json.load(items)

    ingredient_output = []
    item_output = []
    in_idcs = dict()

    for (i, fields) in enumerate(ingredient_data):
        in_idcs[fields["name"]] = i
        fs = []
        for t in [fields["oily"], fields["dry"], fields["sensitive"]]:
            if t == 'O':
                fs += [1]
            elif t == 'X':
                fs += [-1]
            else:
                fs += [0]
        fields = {
            "id": i,
            "name": fields["name"],
			"oily": fs[0],
			"dry": fs[1],
			"sensitive": fs[2]
        }
        ingredient_output += [{
            "pk": i,
            "model": "item.ingredient",
            "fields": fields
        }]
    with open(URL + "ingredient-data-refined.json", 'w', encoding='utf-8') as out:
        json.dump(ingredient_output, out, ensure_ascii=False, indent='\t')

    def name_to_idx(name):
        return in_idcs[name]

    for fields in item_data:
        fields["ingredients"] = list(map(name_to_idx, fields["ingredients"].split(',')))
        item_output += [{
            "model": "item.item",
            "fields": fields
        }]
    with open(URL + "item-data-refined.json", 'w', encoding='utf-8') as out:
        json.dump(item_output, out, ensure_ascii=False, indent='\t')