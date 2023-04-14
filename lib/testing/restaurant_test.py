import pytest

from classes.restaurant import Restaurant
from classes.customer import Customer
from classes.review import Review

class TestRestaurant:
    '''Restaurant in restaurant.py'''

    def test_has_name(self):
        '''has the name passed into __init__'''
        restaurant = Restaurant("Mel's")

        assert restaurant.name == "Mel's"

    def test_validates_name(self):
        '''has name as unchangeable string'''
        with pytest.raises(Exception):
            Restaurant('')

        with pytest.raises(Exception):
            Restaurant(1)

        with pytest.raises(Exception):
            restaurant = Restaurant("Rudy's")
            restaurant.name = "Rudolph's"

    def test_has_many_reviews(self):
        '''restaurant has many reviews'''
        restaurant = Restaurant("Mels")
        customer = Customer('Steve', 'Wayne')
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer, restaurant, 5)

        assert len(restaurant.reviews()) == 2
        assert review_1 in restaurant.reviews()
        assert review_2 in restaurant.reviews()

    def test_restaurant_reviews_type_review(self):
        '''restaurant reviews are of type Review'''
        restaurant = Restaurant("Truluck's")
        restaurant.reviews(1)
        assert not restaurant.reviews()
        customer = Customer('Bruce', 'Miller')
        review = Review(customer, restaurant, 2)
        assert review in restaurant.reviews()

    def test_has_many_customers(self):
        '''restaurant has many customers'''
        restaurant = Restaurant("Mels")
        customer = Customer('Steve', 'Wayne')
        customer_2 = Customer('Dima', 'Bay')
        Review(customer, restaurant, 2)
        Review(customer_2, restaurant, 5)

        assert len(restaurant.customers()) == 2
        assert customer in restaurant.customers()
        assert customer_2 in restaurant.customers()

    def test_restaurant_customers_type_customer(self):
        '''restaurant customers are of type Customer'''
        restaurant = Restaurant("Franklin's")
        restaurant.customers(1)
        assert not restaurant.customers()
        customer = Customer('Bruce', 'Miller')
        restaurant.customers(customer)
        assert customer in restaurant.customers()

    def test_average(self):
        '''average_star_rating() gets average of restaurant's review ratings'''
        restaurant = Restaurant("Mels")
        customer = Customer('Steve', 'Wayne')
        customer_2 = Customer('Dima', 'Bay')
        Review(customer, restaurant, 2)
        Review(customer_2, restaurant, 5)

        assert(restaurant.average_star_rating() == 3.5)

    def test_get_all_restaurants(self):
        '''test has class attribute all'''
        Restaurant.all = []
        restaurant = Restaurant("Mel's")
        restaurant_2 = Restaurant("Franklin's")
        
        assert len(Restaurant.all) == 2
        assert restaurant in Restaurant.all
        assert restaurant_2 in Restaurant.all
