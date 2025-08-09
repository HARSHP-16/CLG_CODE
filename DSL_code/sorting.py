salary = []

value = int(input("Enter the number of employees: "))

for i in range(value):
    s = float(input(f"Enter the salary for employee {i + 1}: "))
    salary.append(s)

#Selection sort
selection_sorted = salary.copy()
for i in range(len(selection_sorted)):
    min = i
    for j in range(i + 1, len(selection_sorted)):
        if selection_sorted[j] < selection_sorted[min]:
            min  = j
    selection_sorted[i], selection_sorted[min] = selection_sorted[min], selection_sorted[i]

print("\nSalaries after selection Sort in Ascending order:", selection_sorted)
print("Top 5 Salaries for Selection :", selection_sorted[-5:][::-1])  


#bubble sort
bubble_sorted = salary.copy()
n = len(bubble_sorted)
for i in range(n - 1):
    for j in range(n - i - 1):
        if bubble_sorted[j] > bubble_sorted[j + 1]:
            bubble_sorted[j], bubble_sorted[j + 1] = bubble_sorted[j + 1], bubble_sorted[j]

print("\nSalaries after Bubble Sort in Ascending order:", bubble_sorted)
print("Top 5 Salaries for Bubble :", bubble_sorted[-5:][::-1])  
