# howmanyitems.py
# by MooseOnTheRocks
#
# Simple Python interface for Minecraft recipes.
# Capabilities:
#   -- Currently, focus on crafting table recipes (shaped and shapeless).
#   -- Search for recipes with resulting item name.
#   -- Display total base materials required.
#   -- Decompose and display item into tree(s) of recipes.
#       -- Each tree represents a unique way to craft that item.
#
# Requirements:
#   // Load recipes from JSON data
#   // Filter craftable recipes
#   -- Search recipe by resulting item name
#   -- Compute recipe paths for items
#   -- Compute summary of base materials required

import os
import json
import pprint
import re

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


def recipes_by_name(recipes, item_name):
    return [r for r in recipes if r.result_item_name == item_name]


def recipes_by_re(recipes, regex):
    return [r for r in recipes if re.search(regex, r.result_item_name) is not None]


def main():
    recipes_json = load_recipes_json()
    shaped_crafting_recipes_json = filter(pred_type("minecraft:crafting_shaped"), recipes_json)
    shaped_crafting_recipes = list(map(RecipeCraftingShaped.from_json, shaped_crafting_recipes_json))
    print("Search recipes by name:")
    name_query = input(">>> ")
    by_re = recipes_by_re(shaped_crafting_recipes, name_query)
    pprint.pprint(by_re)


if __name__ == "__main__":
    main()
