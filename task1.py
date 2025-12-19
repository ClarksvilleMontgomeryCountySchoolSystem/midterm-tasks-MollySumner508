slices = party_pizza_mini + large + medium
print(f'Total number of slices {total_slices}')

people += 1
leftover = slices % people
share = slices // people
print(f"Each person gets: {share}")
print(f"Leftover slices: {leftover}")

people += 2 #Eric and Brandon are coming too.
leftover = slices % people
share = slices// people
print(f"Each person gets: {share}")
print(f"Leftover slices: {leftover}")


slices = (party_pizza_mini*2) + large + medium
leftover = slices % people
share = slices // people
print(f"Each person gets: {share}")
print(f"Leftover slices: {leftover}")
print("...for Mr. Hollow Leg")
