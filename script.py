def calculate_estimation(O, N, P):
    u = (O + 4 * N + P) / 6
    d = (P - O) / 6
    return u, d

# Get user inputs
O = float(input("Enter the optimistic estimation (O) in days: "))
N = float(input("Enter the normal estimation (N) in days: "))
P = float(input("Enter the pessimistic estimation (P) in days: "))

expected_time, deviation = calculate_estimation(O, N, P)

print("Expected time to end the project:", expected_time, "days")
print("Deviation:", deviation, "days")
