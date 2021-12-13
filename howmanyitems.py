import os
import json

from recipecraftingshaped import *


def load_recipes_json():
    root = "recipes"
    paths = (os.path.join(root, file_name) for file_name in os.listdir(root))
    all_recipes = []
    for path in paths:
        with open(path) as file:
            obj = json.load(file)
            all_recipes.append(obj)
    return all_recipes


def pred_key(key, value):
    return lambda obj: obj[key] == value


def pred_type(expected_type):
    return pred_key("type", expected_type)


def main():
    recipes_json = load_recipes_json()
    shaped_crafting_recipes_json = filter(pred_type("minecraft:crafting_shaped"), recipes_json)
    shaped_crafting_recipes = list(map(RecipeCraftingShaped.from_json, shaped_crafting_recipes_json))
    print(len(shaped_crafting_recipes))


if __name__ == "__main__":
    main()
