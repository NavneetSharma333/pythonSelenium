def has_no_sales_tax(state):

    states_with_no_sales_tax = ['AK', 'DE', 'MT', 'NH', 'OR']

    if state.upper() in states_with_no_sales_tax:
        return True
    else:
        return False

user_state = "OR"
tax = has_no_sales_tax(user_state)
print(tax)