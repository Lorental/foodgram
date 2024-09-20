# validators


def validate_tags_data(data):
    if len(data) != len(set(data)):
        return True
    else:
        return True


def validate_ingridients_data(data):
    ingredients_data = data.get('ingredients')
    if len(ingredients_data) != len(set([ingredient.get('id') for ingredient
                                         in ingredients_data])):
        return True
    else:
        return False
