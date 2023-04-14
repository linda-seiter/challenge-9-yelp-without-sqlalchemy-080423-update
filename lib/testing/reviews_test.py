from classes.restaurant import Restaurant
from classes.customer import Customer
from classes.review import Review
import pytest

class TestReviews:
    '''Review in review.py'''

    def test_has_rating(self):
        '''has the rating passed into __init__'''
        restaurant = Restaurant("Mels")
        customer = Customer('Steve', 'Wayne')
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer, restaurant, 5)

        assert(review_1.rating == 2)
        assert(review_2.rating == 5)
        with pytest.raises(Exception):
            review_1.rating = 6
        with pytest.raises(Exception):
            review_1.rating = "6"
        with pytest.raises(Exception):
            review_1.rating = -3

    def test_has_a_customer(self):
        '''review has a customer .'''
        restaurant = Restaurant("Mels")
        customer = Customer('Steve', 'Wayne')
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer, restaurant, 5)

        assert(review_1.customer == customer)
        assert(review_2.customer == customer)

    def test_has_a_restaurant(self):
        '''Review has a restaurant.'''
        restaurant = Restaurant("Mels")
        customer = Customer('Steve', 'Wayne')
        customer_2 = Customer('Dima', 'Bay')
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer_2, restaurant, 5)

        assert(review_1.restaurant == restaurant)
        assert(review_2.restaurant == restaurant)
