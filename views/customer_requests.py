CUSTOMERS = [
    {
      "id": 15,
      "name": "Ryan Tanay",
      "email": "ryan@tanay.com",
          },
    {
      "id": 16,
      "name": "Emma Beaton",
      "email": "emma@beaton.com",
          },
    {
      "id": 17,
      "name": "Dani Adkins",
      "email": "dani.adkins.com",
          },
    {
      "id": 18,
      "name": "Adam Oswalt",
      "email": "adam@oswalt.com",
          },
    {
      "id": 19,
      "name": "Fletcher Bangs",
      "email": "flangs@bangs.com",
          },
    {
      "id": 20,
      "name": "Angela Lee",
      "email": "lee@lee.com",
          },
    {
      "name": "mike mike",
      "email": "m@m.com",
      
      "id": 21
    }
]


def get_all_customers():
    return CUSTOMERS

# Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the CUSTOMERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):
    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the customer dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer