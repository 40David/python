cities = ['A', 'B', 'C', 'D']
distances = {
('A', 'B'): 4, ('A', 'C'): 2, ('A', 'D'): 7,
('B', 'C'): 5, ('B', 'D'): 3, ('C', 'D'): 1
}
visited = ['A']
remaining_cities = set(cities) - set(visited)
current_city = 'A'
total_cost = 0
# Find the next nearest city
while remaining_cities:
   next_city = min(remaining_cities, key=lambda city: distances.get((current_city, city), float('inf')))
   visited.append(next_city)
   remaining_cities.remove(next_city)
   total_cost += distances.get((current_city, next_city), distances.get((next_city, current_city)))
   current_city = next_city
print(f"Visited cities: {visited}")
print(f"Total cost: {total_cost}")