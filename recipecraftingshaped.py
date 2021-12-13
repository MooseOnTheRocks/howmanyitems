class RecipeCraftingShaped:
    TYPE = "minecraft:crafting_shaped"

    def __init__(self, pattern, key, result):
        # Resulting minecraft item.
        self.result = result
        # A map from characters in pattern to items in minecraft.
        self.key = key
        # An array of 0 to 3 strings each ranging from 0 to 3 chars.
        # This encodes the relative positioning, item type, and quantity of the recipe ingredients.
        self.pattern = pattern

    @staticmethod
    def from_json(obj):
        assert(obj["type"] == RecipeCraftingShaped.TYPE)
        result, key, pattern = map(lambda k: obj[k], ["result", "key", "pattern"])
        return RecipeCraftingShaped(result, key, pattern)

    def __repr__(self):
        return f"RecipeCraftingShaped({self.result}, {self.key}, {self.pattern})"
