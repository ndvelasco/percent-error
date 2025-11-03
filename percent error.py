def percent_error(experimental, theoretical):
    if theoretical == 0:
        raise ValueError("Theoretical value cannot be zero.")
    return abs(experimental - theoretical) / theoretical * 100

experimental_values = [1.60, 2.80, 0.70, 1.40, 0.30, 0.60, 0.10, 0.20, 1.50, 2.90, 0.70, 1.30, 0.20, 0.40, 0.10, 0.20]
theoretical_values = [1.63, 3.25, 0.81, 1.63, 0.26, 0.52, 0.13, 0.26, 1.29, 2.58, 0.64, 1.29, 0.21, 0.41, 0.10, 0.21]

if len(experimental_values) != len(theoretical_values):
    raise ValueError("Arrays of experimental and theoretical values must have the same length.")

percent_errors = []
for exp, theo in zip(experimental_values, theoretical_values):
    error = percent_error(exp, theo)
    percent_errors.append(error)

print("Percent errors:")
for i, error in enumerate(percent_errors):
    print(f"Pair {i + 1}: {error:.2f}%")
