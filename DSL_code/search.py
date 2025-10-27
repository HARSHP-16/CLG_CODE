# Linear Search function
def linear_search(customer_ids, target_id):
    for i in range(len(customer_ids)):
        if customer_ids[i] == target_id:
            return i  
    return -1  


# Binary Search function
def binary_search(customer_ids, target_id):
    left = 0
    right = len(customer_ids) - 1

    while left <= right:
        mid = (left + right) // 2
        if customer_ids[mid] == target_id:
            return mid
        elif customer_ids[mid] < target_id:
            left = mid + 1
        else:
            right = mid - 1

    return -1

print("E-Commerce Customer Account Search System\n")

customer_ids = [105, 204, 302, 101, 250, 190]

print("Customer Account IDs:", customer_ids)

target_id = int(input("Enter Customer Account ID to search: "))

# Linear Search
index_linear = linear_search(customer_ids, target_id)
if index_linear != -1:
    print(f"[Linear Search] Customer ID {target_id} found at position {index_linear + 1}.")
else:
    print(f"[Linear Search] Customer ID {target_id} not found.")

# Binary Search 
sorted_ids = sorted(customer_ids)
index_binary = binary_search(sorted_ids, target_id)
if index_binary != -1:
    print(f"[Binary Search] Customer ID {target_id} found at position {index_binary + 1} in sorted list.")
else:
    print(f"[Binary Search] Customer ID {target_id} not found in sorted list.")
