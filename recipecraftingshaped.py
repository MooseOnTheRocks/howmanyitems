class RecipeCraftingShaped:
    TYPE = "minecraft:crafting_shaped"

    def __init__(self, result_item_name, result_count, key, pattern):
        # Resulting minecraft item.
        self.result_item_name = result_item_name
        # Quantity received from crafting
        self.result_count = result_count
        # A map from characters in pattern to items in minecraft.
        self.key = key
        # An array of 0 to 3 strings each ranging from 0 to 3 chars.
        # This encodes the relative positioning, item type, and quantity of the recipe ingredients.
        self.pattern = pattern

    @staticmethod
    def from_json(obj):
        assert(obj["type"] == RecipeCraftingShaped.TYPE)
        result, key, pattern = map(lambda k: obj[k], ["result", "key", "pattern"])
        result_count = result["count"] if "count" in result else 1
        result_item_namespace, result_item_name = result["item"].split(":")

        return RecipeCraftingShaped(result_item_name, result_count, key, pattern)

    def __repr__(self):
        return f"RecipeCraftingShaped({self.result_item_name}, {self.result_count}, {self.key}, {self.pattern})"
