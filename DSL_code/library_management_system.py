#Write a Python program to manage the borrowing records of books in a library. Implement
#the following functionalities:
#• Compute the average number of books borrowed by all library members.
#• Find the book with the highest and lowest number of borrowings in the library.
#• Count the number of members who have not borrowed any books (denoted by a
#borrow count of 0).
#• Display the most frequently borrowed book (i.e., the mode of borrow counts).
#After performing, determine the time and Space complexity of each operation

students={
1:["dsa","deld","maths"],
2:["maths","deld"],
3:[],
4:["deld","dsa"],
5:["phy","maths"]
}


a= students.keys()
#• Compute the average number of books borrowed by all library members.
sum=0
for i in students:
	sum=sum+len(students[i])
avg = sum/len(a)

#• Count the number of members who have not borrowed any books
count_students=0
for i in students:
	if(len(students[i])==0):
		count_students+=1

#• Find the book with the highest and lowest number of borrowings in the library.
book_count={}
for i in students.values():
	for book in i:
		if book in book_count:
			book_count[book]+=1
		else:
			book_count[book]=1

maxbook=max(book_count,key=book_count.get)	
minbook=min(book_count,key=book_count.get)					


#MENU
while True:
    print("\n--- Library Menu ---")
    print("1. Compute average number of books borrowed")
    print("2. Count members who haven't borrowed any books")
    print("3. Find the book with highest and lowest borrowings")
    print("4. Exit")
   
   
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
       print("Average is",avg)
    elif choice == "2":
       print(count_students)
    elif choice == "3":
      print("highest borrowed",maxbook)
      print("lowest borrowed",minbook)
    elif choice == "4":
       print("\nExiting program. Goodbye!")
       break
	
    else:
       print("\nInvalid choice. Please enter a number from 1 to 4.")