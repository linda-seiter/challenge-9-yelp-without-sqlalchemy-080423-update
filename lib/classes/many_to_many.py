from statistics import mean

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
            # raise Exception("First name must be a string between 1 and 25 characters")

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if isinstance(last_name, str) and 1 <= len(last_name) <= 25:
            self._last_name = last_name
        else:
            return None
            # raise Exception("First name must be a string between 1 and 25 characters")

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
        if cls.all:
            top = max(cls.all, key=lambda customer: customer.num_negative_reviews())
            if top.num_negative_reviews() > 0:
                return top
        return None
    
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
            # raise Exception("Name must be non-empty string")

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


    
class Review:
    all = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        type(self).all.append(self)

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        if isinstance(rating, int) and 1 <= rating <= 5 and not hasattr(self, "rating"):
            self._rating = rating
        else:
            return None
            # raise Exception("Rating must be integer between 1 and 5 that can't be changed")

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            return None
            # raise Exception("customer must be of type Customer")

    @property
    def restaurant(self):
        return self._restaurant

    @restaurant.setter
    def restaurant(self, restaurant):
        if isinstance(restaurant, Restaurant):
            self._restaurant = restaurant
        else:
            return None
            # raise Exception("restaurant must be of type Restaurant")
