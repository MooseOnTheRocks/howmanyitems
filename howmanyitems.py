import os
import json
import pprint


class Recipe:
    def __init__(self):
        pass

    @staticmethod
    def from_json(recipe_json):
        print("from_json:")
        print(recipe_json)
        return Recipe()


def load_recipes_json():
    root = "recipes"
    paths = (os.path.join(root, file_name) for file_name in os.listdir(root))
    all_recipes = []
    for path in paths:
        with open(path) as file:
            obj = json.load(file)
            all_recipes.append(obj)
    return all_recipes


def main():
    recipes = load_recipes_json()
    # first = recipes[0]
    # rec = Recipe.from_json(first)
    # print(rec)
    all_types = (recipe["type"] for recipe in recipes)
    unique_types = set(all_types)
    print(unique_types)
    print("all recipes:", len(recipes))
    print("minecraft:crafting_shaped")
    num_shaped = sum(r["type"] == "minecraft:crafting_shaped" for r in recipes)
    print(num_shaped)
    print("minecraft:crafting_shapeless")
    num_shapeless = sum(r["type"] == "minecraft:crafting_shapeless" for r in recipes)
    print(num_shapeless)


if __name__ == "__main__":
    main()
