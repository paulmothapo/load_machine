def calculate_total_cost(base_cost, interest_rate, admin_cost, num_years):
    principal_amount = base_cost + admin_cost
    interest = principal_amount * interest_rate * num_years
    total_cost = principal_amount + interest
    return total_cost