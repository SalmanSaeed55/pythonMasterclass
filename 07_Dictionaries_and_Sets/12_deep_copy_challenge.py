from contents import recipes


def my_deepcopy(d: dict) -> dict:
    """Copy a dictionary and return a deep copy of it

    :param d: The dictionary to copy
    :return: a deep copy of d
    """
    deep_copy = {}
    for key, value in d.items():
        new_value = value.copy()
        deep_copy[key] = new_value
    return deep_copy


recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
