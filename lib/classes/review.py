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
            # raise Exception("Ratings must be integers between 1 and 5")

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

from classes.customer import Customer
from classes.restaurant import Restaurant