import random
def simulate_event(machine_id):
   event = random.choice(['Start', 'Breakdown', 'Maintenance'])
   print(f"Machine {machine_id}: {event}")
def run_simulation(num_machines, steps):
   for step in range(1,steps+1):
      print(f"\nTime Step {step}")
      for machine_id in range(1, num_machines + 1):
        simulate_event(machine_id)
run_simulation(5, 10)