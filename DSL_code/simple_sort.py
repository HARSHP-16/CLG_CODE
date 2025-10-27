# Employee Salaries
salaries = [45000.0, 52000.5, 31000.0, 60000.0, 72000.0, 49000.0, 38000.0]

# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# --- Using Selection Sort ---
sel_salaries = salaries.copy()
selection_sort(sel_salaries)
print("Salaries sorted using Selection Sort:", sel_salaries)
print("Top 5 highest salaries:", sel_salaries[-5:][::-1])

# --- Using Bubble Sort ---
bub_salaries = salaries.copy()
bubble_sort(bub_salaries)
print("\nSalaries sorted using Bubble Sort:", bub_salaries)
print("Top 5 highest salaries:", bub_salaries[-5:][::-1])
