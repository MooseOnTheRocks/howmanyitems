import os
import json
import pprint
from builtins import all

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


def reduce_predicates(reduce, *predicates):
    return lambda elem: reduce(map(lambda pred: pred(elem), predicates))


def filter_crafting_recipes(recipes):
    predicate = reduce_predicates(
        any,
        pred_type("minecraft:crafting_shaped"),
        pred_type("minecraft:crafting_shapeless"),
    )
    return list(filter(predicate, recipes))


def main():
    recipes = load_recipes_json()
    crafting_recipes = filter_crafting_recipes(recipes)
    print(f"There are {len(crafting_recipes)} craftable items in Minecraft 1.18")


if __name__ == "__main__":
    main()
