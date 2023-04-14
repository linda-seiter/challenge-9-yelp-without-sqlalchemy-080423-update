#!/usr/bin/env python3

from random import randint, choice as rc

from faker import Faker
import ipdb

from classes.customer import Customer
from classes.restaurant import Restaurant
from classes.review import Review

if __name__ == '__main__':
    fake = Faker()

    customers = [Customer(fake.first_name(), fake.last_name()) for i in range(50)]
    restaurants = [Restaurant(f"{fake.first_name()}'s") for i in range(25)]
    reviews = [Review(rc(customers), rc(restaurants), randint(1, 5)) for i in range(200)]

    ipdb.set_trace()
