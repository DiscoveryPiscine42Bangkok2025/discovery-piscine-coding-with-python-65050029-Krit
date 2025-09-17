original_array = [2, 8, 9, 48, 8, 22, -12, 2]
processed_array = [x + 2 for x in original_array if x > 5]
unique_array = []
for num in processed_array:
    if num not in unique_array:
        unique_array.append(num)

print(original_array)
print(unique_array)
