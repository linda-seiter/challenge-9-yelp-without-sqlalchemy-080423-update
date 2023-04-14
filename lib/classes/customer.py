class Customer:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def reviews(self, new_review=None):
        from classes.review import Review
        pass
    
    def restaurants(self, new_restaurant=None):
        from classes.restaurant import Restaurant
        pass

    def num_reviews(self):
        pass
