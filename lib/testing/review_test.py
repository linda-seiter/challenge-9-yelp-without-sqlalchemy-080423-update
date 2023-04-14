import pytest

from classes.restaurant import Restaurant
from classes.customer import Customer
from classes.review import Review

class TestReviews:
    '''Review in review.py'''

    def test_has_customer_restaurant_rating(self):
        '''has the customer, restaurant, and rating passed into __init__'''
        customer = Customer('Steve', 'Wayne')
        restaurant = Restaurant("Mels")
        review = Review(customer, restaurant, 2)

        assert review.customer == customer
        assert review.restaurant == restaurant
        assert review.rating == 2

    def test_validates_customer(self):
        '''checks to ensure customer is of type Customer'''
        restaurant = Restaurant("Katz")
        
        with pytest.raises(Exception):
            Review(1, restaurant, 2)

    def test_validates_restaurant(self):
        '''checks to ensure restaurant is of type Restaurant'''
        customer = Customer('Prabhdip', 'Gill')
        
        with pytest.raises(Exception):
            Review(customer, 1, 2)

    def test_validates_rating(self):
        '''checks to ensure rating is integer between 1 and 5, inclusive'''
        customer = Customer('Steve', 'Wayne')
        restaurant = Restaurant("Mels")

        with pytest.raises(Exception):
            Review(customer, restaurant, 0)

        with pytest.raises(Exception):
            Review(customer, restaurant, 6)
