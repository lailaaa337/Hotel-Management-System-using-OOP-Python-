
#  Hotel Management System (OOP in Python)

##  Overview
This project is a **console-based Hotel Management System** implemented using **Object-Oriented Programming (OOP) in Python**.

The system simulates real-world hotel operations by managing:
- Guests   
- Rooms   
- Staff   
- Bookings  

It demonstrates core OOP principles such as **encapsulation, inheritance, polymorphism, and modular design**.

---

##  Features

###  Hotel Management
- Store and display hotel information  
- Update hotel details dynamically  

---

###  Guest Management
- Add new guests  
- Store guest ID and name  
- Display all guests  

---

###  Room Management
- Add new rooms  
- Display available rooms  
- Search for rooms by ID  
- Delete rooms  
- Sort rooms by ID  

---

###  Staff Management
- Store staff details (name, position, hours, rate)  
- Calculate **monthly salary**  

---

###  Booking System
- Book rooms with check-in and check-out dates  
- Calculate stay duration  
- Display booking details  

---

##  OOP Concepts Used

###  Encapsulation
Each entity (Hotel, Guest, Room, Staff, Booking) is represented as a class with its own attributes and methods.

---

###  Inheritance
All classes inherit from a base `Hotel` class:

```python
class Guest(Hotel)
class Room(Hotel)
class Staff(Hotel)
class Booking(Hotel)
````

---

###  Polymorphism

The `displayDetails()` method is implemented differently across classes.

---

###  Abstraction

Complex operations (e.g., booking, salary calculation, sorting) are encapsulated inside methods.

---

##  System Architecture

###  Main Classes

* **Hotel**

  * Base class with common attributes
* **Guest**

  * Stores guest information
* **Room**

  * Manages room operations
* **Staff**

  * Handles employee details and salary
* **Booking**

  * Manages reservations and dates

---

##  How It Works

1. Program starts with a **menu-driven interface**
2. User selects an option
3. Corresponding class method is executed
4. Data is stored in lists (guests, rooms, bookings)

---

##  Program Menu

```
1. Display hotel details
2. Update hotel details
3. Add a new guest
4. Display guests
5. Add a new room
6. Display rooms
7. Sort rooms by ID
8. Search for a room
9. Delete a room
10. Staff salary calculation
11. Book a room
12. Exit
```

---

##  Technologies Used

* **Python**
* Standard Library (`datetime`)

---

##  Project Structure

```
project/
│── main.py     # Main program file
│── README.md
```

---

##  How to Run

1. Make sure Python is installed
2. Navigate to the project folder

```bash
python main.py
```

3. Follow the on-screen menu

---

##  Example Use Cases

* Manage hotel guests and bookings
* Track room availability
* Calculate staff salaries
* Organize and sort rooms
* Simulate real hotel operations

---

##  What I Learned

* Applying **OOP principles in real systems**
* Designing multi-class applications
* Managing relationships between objects
* Building menu-driven applications in Python
* Working with dates (`datetime`)

---

##  Limitations

* Data is not persistent (no database)
* Console-based interface only
* Limited validation for user input
* Fixed hotel data (hardcoded values)

---

##  Future Improvements

* Add database (SQLite / MySQL)
* Build GUI or web interface
* Add authentication system
* Improve validation and error handling
* Support multiple hotels

---

##  Author

**Laila Tarek**

```

