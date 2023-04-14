# Object Relations Code Challenge - Restaurants

For this assignment, we'll be working with a Yelp-style domain.

We have three models: `Restaurant`, `Customer`, and `Review`.

For our purposes, a `Restaurant` has many `Reviews`, a `Customer` has many
`Review`s, and a `Review` belongs to a `Customer` and to a `Restaurant`.

`Restaurant` - `Customer` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you
start coding_. Remember to identify a single source of truth for your data.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

## Instructions

To get started, run `pipenv install` while inside of this directory.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge has tests to help you check your work. You
can run `pytest` to make sure your code is functional before submitting.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session
with your classes defined. You can test out the methods that you write here. You
can add code to the `debug.py` file to define variables and create sample
instances of your objects.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

### Initializers, Readers, and Writers

For any invalid inputs raise an `Exception`. In your future work, you should
raise specific types of exceptions for specific error cases. You can do that
here and the tests will pass, but you don't have to this time around!

#### Customer

- `Customer __init__(self, first_name, last_name)`
  - Customer should be initialized with a given name and family name, (i.e.,
    first and last name,
    like George Washington)"
- `Customer property first_name()` and `Customer property last_name()`
  - Return first and last name, respectively
  - Names must be of type `str`
  - Names must be between 1 and 25 characters, inclusive
  - `raise Exception` if setter validation fails

#### Restaurant

- `Restaurant __init__(self, name)`
  - Restaurants should be initialized with a name, as a string
- `Restaurant property name()`
  - Returns the restaurant's name
  - Must be 1 or more characters
  - Should not be able to change after the restaurant is created
  - `raise Exception` if setter validation fails
- `Restaurant class attribute all`
  - Returns a list of all restaurants

#### Review

- `Review __init__(self, customer, restaurant, rating)`
  - Reviews should be initialized with a customer, restaurant, and a rating (a number)
- `Review property rating()`
  - Returns the rating for a restaurant
  - Rating must be a number between 1 and 5, inclusive
  - `raise Exception` if setter validation fails

### Object Relationships

#### Review

- `Review customer`
  - Returns the customer object for that review
  - Must be of type `Customer`
  - `raise Exception` if validation fails
  
- `Review restaurant`
  - Returns the restaurant object for that given review
  - Must be of type `Restaurant`
  - `raise Exception` if validation fails

#### Restaurant

- `Restaurant reviews(self, new_review=None)`
  - Creates a new review if called with new review
  - Returns a list of all reviews for that restaurant
  - Reviews must be of type `Review`
  - _Should be called from `Review.__init__`_
- `Restaurant customers(self, new_customer=None)`
  - Creates a new customer if called with new customer
  - Returns a **unique** list of all customers who have reviewed a particular restaurant.
  - Customers must be of type `Customer`
  - _Should be called from `Review.__init__`_

#### Customer

- `Customer restaurants(self, new_restaurant=None)`
  - Creates a new restaurant if called with new restaurant
  - Returns a **unique** list of all restaurants a customer has reviewed
  - Restaurants must be of type `Restaurant`
  - _Should be called from `Review.__init__`_
- `Customer reviews(self, new_review=None)`
  - Creates a new review if called with new review
  - Returns a list of all reviews a customer has written
  - _Should be called from `Review.__init__`_

### Aggregate and Association Methods

#### Customer

- `Customer num_reviews()`
  - Returns the total number of reviews that a customer has authored

#### Restaurant

- `Restaurant average_star_rating(self)`
  - Returns the average star rating for a restaurant based on its reviews
  - Reminder: you can calculate the average by adding up all the ratings and
    dividing by the number of ratings
