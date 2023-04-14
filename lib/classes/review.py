from classes.customer import Customer
from classes.restaurant import Restaurant

class Review:
    
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
