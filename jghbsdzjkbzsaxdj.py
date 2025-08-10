# Sample dataset (list of numbers)
data = list(map(int, input("Enter 10 numbers separated by space: ").split()))
# Check if exactly 10 numbers are entered
if len(data) != 10:
 print("You must enter exactly 10 numbers.")
else:
# Calculate mean
 mean = sum(data) / len(data)
# Calculate median
 data_sorted = sorted(data)
 median = data_sorted[len(data) // 2] if len(data) % 2 != 0 else (data_sorted[len(data) // 2 - 1] +
 data_sorted[len(data) // 2]) / 2
# Calculate mode manually
frequency = {1 :2,2:2,}
for num in data:
  frequency[num] = frequency.get(num, 0) + 1
  mode = max(frequency, key=frequency.get)
# Display the descriptive statistics
statistics = {"Mean": mean, "Median": median, "Mode": mode}
for stat, value in statistics.items():
  print(f"{stat}: {value}")