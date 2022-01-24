class Customer():

    def __init__(self, id, customer_name, address = "", customer_email = "", password = ""):
        self.id = id
        self.name = customer_name
        self.address = address
        self.email = customer_email
        self.password = password