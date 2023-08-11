class Restaurant:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 1:
            self._name = name
        else:
            return None
            # raise Exception("Names must be non-empty strings")

    def reviews(self):
        return [review for review in Review.all if review.restaurant is self]

    def customers(self):
        return list({review.customer for review in self.reviews()})

    def average_star_rating(self):
        return round(
            mean([review.rating for review in self.reviews()]),
            1
        ) if self.reviews() else 0.0

    @classmethod
    def top_two_restaurants(cls):
        sorted_list = sorted(
            cls.all,
            key=lambda restaurant: restaurant.average_star_rating(),
            reverse=True,
        ) if Review.all else []
        return (
            sorted_list[:2]
            if len(sorted_list) > 1
            else sorted_list[0]
            if sorted_list
            else None
        )


from classes.review import Review
from statistics import mean
