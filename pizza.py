def make_pizza(*toppings):
    """Summarize the pizza we are about to make"""
    print(f"\nThe following are the ingredient used in making a pizza:")
    for topping in toppings:
        print(f" -{topping}")
