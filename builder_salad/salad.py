class Salad:
    def __init__(self):
        self.ingredients = []

    def prepare_vegg(self, vegg):
        self.ingredients.append(vegg)

    def prepare_main(self, main):
        self.ingredients.append(main)

    def prepare_graving(self, graving):
        self.ingredients.append(graving)

    def prepare_price(self, price):
        self.ingredients.append(price)

    def __str__(self):
        return "Salad Ingredients: " + ", ".join(self.ingredients)
