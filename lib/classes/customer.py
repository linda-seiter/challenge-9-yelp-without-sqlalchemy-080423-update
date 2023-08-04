class Customer:
    all = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        type(self).all.append(self)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if isinstance(first_name, str) and 1 <= len(first_name) <= 25:
            self._first_name = first_name
        else:
            return None

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if isinstance(last_name, str) and 1 <= len(last_name) <= 25:
            self._last_name = last_name
        else:
            return None

    def reviews(self):
        return [review for review in Review.all if review.customer is self]

    def restaurants(self):
        return list({review.restaurant for review in self.reviews()})

    def num_negative_reviews(self):
        return len([review for review in self.reviews() if review.rating < 3])

    def has_reviewed_restaurant(self, restaurant):
        return restaurant in self.restaurants()

    @classmethod
    def top_negative_reviewer(cls):
        return (
            max(cls.all, key=lambda customer: customer.num_negative_reviews())
            if cls.all
            else None
        )


from classes.review import Review
