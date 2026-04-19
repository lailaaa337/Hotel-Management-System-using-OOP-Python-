from datetime import datetime     #library keda be t-convert from string to date

class Hotel:        #this class contains id, name, contact,address
    def __init__(self, H_ID, H_name, H_contactInfo, H_address):  #Encapsulation
        self.H_ID = H_ID
        self.H_name = H_name
        self.H_contactInfo = H_contactInfo
        self.H_address = H_address
        self.guests = []  # List of guests 3alashan lama 23ml append   }
        self.funcRoom = []  # List of rooms same as guests             } ->  why self?? 3alashan haya5od address el object for example: guest1.guests
        self.book = []  # List of bookings same as guests              }

    def displayDetails(self):                  #method to display w btw display dih polymorphism ?? hagaweb ta7t (;
        print(f"Hotel ID = {self.H_ID}")
        print(f"Name = {self.H_name}")
        print(f"Contact info = {self.H_contactInfo}")
        print(f"Address = {self.H_address}")

    def updateDetails(self):                       #this method to update anything according to el user 3ayez eh
        print("What would you like to update?")
        print("1. Hotel ID\n2. Hotel Name\n3. Hotel Contact info\n4. Hotel Address")
        choice = int(input())
        if choice == 1:
            self.H_ID = int(input("Enter the Hotel new ID: "))                 # }
            print("Hotel ID updated successfully")                             
        elif choice == 2:                                                       
            self.H_name = input("Enter the new Hotel name: ")                  # } 
            print("Hotel name updated successfully")                           #        ->    hena i will assign each instance bel value el gedida             
        elif choice == 3:
            self.H_contactInfo = input("Enter the new hotel contact: ")        # }
            print("Hotel contact updated successfully")
        elif choice == 4:
            self.H_address = input("Enter the new hotel address: ")            # }
            print("Hotel Address updated successfully")
        else:
            print("Error: Please enter a valid choice...")

class Guest(Hotel):                              #New class that inherits the base class
    def __init__(self, H_ID, H_name, H_contactInfo, H_address, Guest_Id, Guest_name): #lazem a7ot kol el instance bema fihom el fel base class
        super().__init__(H_ID, H_name, H_contactInfo, H_address)    #super dih 3alashan ma3odsh akteb (self. = ) -> bec dah already mawgod fel base class
        self.Guest_Id = Guest_Id
        self.Guest_name = Guest_name

    def displayDetails(self):      #aho el polymorphism as i said (; -> batsa5dem nafs esm el method fe kaza 7eta w kol wa7da gowaha hagat mo5talefa
        super().displayDetails()   #this will also display details in the base class
        print(f"Guest ID: {self.Guest_Id}")
        print(f"Guest Name: {self.Guest_name}")

    def updateGuestInfo(self):         #hena bardo method to update according to ra8bet el user
        print("What would you like to update?")
        print("1. Guest ID\n2. Guest name")
        choice = int(input())
        if choice == 1:
            self.Guest_Id = input("Enter the new ID: ")
            print("Guest ID updated successfully.")
        elif choice == 2:
            self.Guest_name = input("Enter the new guest name: ")
            print("Guest name updated successfully.")
        else:
            print("Error: Please enter a valid choice...")

class Room(Hotel):     #another entity that inherits from the base class
    def __init__(self, H_ID, H_name, H_contactInfo, H_address, Room_id, RoomType, PricePerNight, Availability):
        super().__init__(H_ID, H_name, H_contactInfo, H_address)
        self.Room_id = Room_id
        self.RoomType = RoomType
        self.PricePerNight = PricePerNight
        self.Availability = Availability      #hena ha5od men el user True aw False 

    def displayDetails(self):       #polymorphism 
        super().displayDetails()
        print(f"Room ID: {self.Room_id}")
        print(f"Room type: {self.RoomType}")
        print(f"Price per night: {self.PricePerNight}")
        print(f"Availability: {self.Availability}")

    def add_room(self, new_room):            #ba add new room w ba5od its address w el value beta3etha el heya it will be roomId, roomType ,etc...
        self.funcRoom.append(new_room)       #ba append fel list el ana 3amlaha fo2

    def display_new_rooms(self):
        for r in self.funcRoom:             #ha dislpay el rooms el 3andi now how??? just a normal loop that llops 3ala el list and will display all
            r.displayDetails()

    def search(self, number):
        for r in self.funcRoom:             #another method to search beta5od a number .. tab whic number?? howa roomId law mawgod ba2ol found law no ba2ol not found
            if r.Room_id == number:
                print(f"Room {number} is found")
                return
        print(f"Room {number} not found")

    def delete(self, number):
        for r in self.funcRoom:
            if r.Room_id == number:            #another method to delete beta5od bardo the roomId that i want to delete 
                self.funcRoom.remove(r)
                print(f"Room {number} has been removed")
                return
        print(f"Room {number} not found")

    def sortRooms(self):               #the worst function );  to sort rooms according to the ids
        self.funcRoom.sort(key=lambda room: room.Room_id)       #dih function malhash esm bet help python eno ye sort bel key , eh howa key? room_id
        print("Rooms have been sorted by their IDs:")
        for r in self.funcRoom:          #hena el mafrod bey display el rooms w homa sorted
            r.displayDetails()

class Staff(Hotel):
    def __init__(self, H_ID, H_name, H_contactInfo, H_address, staff_name, position, hr_worked, hr_rate, shift):
        super().__init__(H_ID, H_name, H_contactInfo, H_address)
        self.staff_name = staff_name
        self.position = position
        self.hr_worked = hr_worked
        self.hr_rate = hr_rate
        self.shift = shift

    def displayDetails(self):
        super().displayDetails()
        print(f"Staff name: {self.staff_name}")
        print(f"Staff position: {self.position}")
        print(f"Hours worked per week: {self.hr_worked}, Hourly rate: {self.hr_rate}")
        print(f"Shift: {self.shift}")

    def salaryPerMonth(self):                #ba7es el salary beta3o according to hr_worked w hr_rate
        salary = self.hr_rate * self.hr_worked * 4
        print(f"Staff salary is {salary}$")

class Booking(Hotel):
    def __init__(self, H_ID, H_name, H_contactInfo, H_address, RoomNum, CheckinDate, CheckoutDate):
        super().__init__(H_ID, H_name, H_contactInfo, H_address)
        self.RoomNum = RoomNum
        self.CheckinDate = datetime.strptime(CheckinDate, "%Y-%m-%d")  # -> strptime dih esmaha (string parse time) bet convert men string to date time
        self.CheckoutDate = datetime.strptime(CheckoutDate, "%Y-%m-%d")

    def add_booking(self,new_booking):       # ba add fel list beta3i new booking details
        self.book.append(new_booking)
        for b in self.book:
            b.displayDetails()


    def displayDetails(self):
        super().displayDetails()
        print(f"Room number: {self.RoomNum}")
        print(f"Check-in date: {self.CheckinDate.strftime('%Y-%m-%d')}")
        print(f"Check-out date: {self.CheckoutDate.strftime('%Y-%m-%d')}")

    def Stay_duration(self):
        duration = self.CheckoutDate - self.CheckinDate           #bashof el sha5s dah hayo3od ad eh
        print(f"The guest is staying for {duration.days} days.")

hotel = Hotel(101, "San Stefano", "0101223334", "Gleem, Alexandria")                                        #   }
guest1 = Guest(101, "San Stefano", "0101223334", "Gleem, Alexandria", "G001", "Alice Smith")                #   }
guest2 = Guest(101, "San Stefano", "0101223334", "Gleem, Alexandria", "G002", "Bob Brown")                  #   }        
room1 = Room(101, "San Stefano", "0101223334", "Gleem, Alexandria", "R101", "Single", 100, "True")          #   }
room2 = Room(101, "San Stefano", "0101223334", "Gleem, Alexandria", "R102", "Double", 150, "True")          #   } -> ba5od object en kol el classes w badi values
staff1 = Staff(101, "San Stefano", "0101223334", "Gleem, Alexandria", "John", "Manager", 40, 25, "Morning") #   }
staff2 = Staff(101, "San Stefano", "0101223334", "Gleem, Alexandria", "Jane", "Receptionist", 30, 20, "Night")# }
booking1 = Booking(101, "San Stefano", "0101223334", "Gleem, Alexandria", "R101", "2024-12-25", "2024-12-30")#  }
booking2 = Booking(101, "San Stefano", "0101223334", "Gleem, Alexandria", "R102", "2024-11-10", "2024-12-10")#  }

funcRoom = [room1, room2]   # }
guests = [guest1, guest2]   # } ->  ba7ot el object beto3i el ana lessa 3amlahom fel list el 3amaltelhom creation 
book = [booking1, booking2] # }

while True:
    print("\nWelcome to the Hotel Management System")
    print("1. Display hotel details")
    print("2. Update hotel details")
    print("3. Add a new guest")                                       #MY MENU <3
    print("4. Display guests")
    print("5. Add a new room")
    print("6. Display rooms")
    print("7. Sort rooms by ID")
    print("8. Search for a room")
    print("9. Delete a room")
    print("10. Staff salary calculation")
    print("11. Book a room")
    print("12. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        hotel.displayDetails()                        #el self benesbali howa address el hotel so it will be hotel.displayDetails fo2 bossi

    elif choice == 2:
        hotel.updateDetails()                  #same thing as choice 1

    elif choice == 3:
        guest_id = input("Enter new guest ID: ")     #ha5od men el user new guestid w new name lel guest 
        guest_name = input("Enter new guest name: ") # ha3ml variable esmo new_guest hayb2a object fi haagt sabta zay el H_id , etc.. bass el haagt el gedida hazawedha
        new_guest = Guest(101, "San Stefano", "0101223334", "Gleem, Alexandria", guest_id, guest_name)   #el howa guestid w guestname
        guests.append(new_guest)    #ba3d kda ha append fel list el esmaha guests ha append el new_guest
        print("New guest added successfully.")

    elif choice == 4:
        for g in guests:              #ha display all guests bema fihom el new_guest
            g.displayDetails()

    elif choice == 5:
        Room_id = input("Enter new room ID: ")   #same thing
        RoomType = input("Enter room type: ")
        PricePerNight = input("Enter the price per night: ")
        Availability = input("Is it available? (True/False): ")
        new_room = Room(101, "San Stefano", "0101223334", "Gleem, Alexandria", Room_id, RoomType, PricePerNight, Availability)
        room1.add_room(new_room) #leh hena msh func_room.add_room? 3alashan add_room dah beya5od already (self,new_room) fa room1 dah yo3tabar el new_room
        print("Room added successfully.")   # w gowa el add_room hayb2a fih eny a append el room1 dah fell list beta3ti 

    elif choice == 6:
        room1.display_new_rooms()

    elif choice == 7:
        room1.sortRooms()

    elif choice == 8:
        room_id = input("Enter room ID to search: ")
        room1.search(room_id)

    elif choice == 9:
        room_id = input("Enter room ID to delete: ")
        room1.delete(room_id)

    elif choice == 10:
        print("1. Staff 1\n2. Staff 2")
        user_choice = int(input("Choose staff to calculate salary: "))
        if user_choice == 1:
            staff1.salaryPerMonth()
        elif user_choice == 2:
            staff2.salaryPerMonth()
        else:
            print("Invalid choice.")

    elif choice == 11:
        RoomNum = input("Enter room number to book: ")
        CheckinDate = input("Enter check-in date (YYYY-MM-DD): ")
        CheckoutDate = input("Enter check-out date (YYYY-MM-DD): ")
        new_booking = Booking(101, "San Stefano", "0101223334", "Gleem, Alexandria", RoomNum, CheckinDate, CheckoutDate)
        booking1.add_booking(new_booking)
        new_booking.displayDetails()
        new_booking.Stay_duration()

    elif choice == 12:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")
 