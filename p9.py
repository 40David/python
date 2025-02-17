import random
max_customer=20
avg_cost_per_customer=25
simulation=1000
days=30
def monte_carlosimulation():
    total_revenue=0
    for day in range(days):
        customer_today=random.randint(0,max_customer)
        daily_revenue=customer_today*avg_cost_per_customer
        total_revenue+=daily_revenue
    return total_revenue
def run_simulation():
    total_simulation_revenue=0
    revenues= [] 
    for _ in range(simulation):
     simulations_revenue = monte_carlosimulation()
     revenues.append(simulations_revenue)
     total_simulation_revenue += simulations_revenue
    avg_revenue=total_simulation_revenue/simulation
    min_revenue=min(revenues)
    max_revenue=max(revenues)
     
    print(f"monte carlo simulation results")
    print(f"average revenue:${avg_revenue:,.2f}")
    print(f"minimum revenue:${min_revenue:,.2f}")
    print(f"max revenue:${max_revenue:,.2f}")

run_simulation()