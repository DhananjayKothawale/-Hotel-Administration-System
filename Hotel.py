
'''
    Project NAME :- Hotel Administration System

    Name : DHANANJAY MACHINDRA KOTHAWALE

    GIT-HUB Username : DhananjayKothawale
    Edx Username : Dhananjay_Kothawale
    City,State,Country : Chhatrapati Sambhajinagar(Aurangabad) , Maharashtra , India
    Date(YYYY-MM-DD) : 2004-07-27

'''

class Hotel:
    def __init__(self):
        self.bookings = []

    def add_booking(self, name, room_number, check_in_date, check_out_date):
        """Add a new booking to the hotel."""
        booking = {
            "name": name,
            "room_number": room_number,
            "check_in_date": check_in_date,
            "check_out_date": check_out_date,
            "review": None  # Initialize review as None
        }
        self.bookings.append(booking)
        print(f"Booking added for {name} in room {room_number}.")

    def get_bookings(self):
        """Retrieve all current bookings."""
        return self.bookings

    def generate_report(self):
        """Generate a report of all bookings."""
        if not self.bookings:
            return "No bookings found."
        report = "Hotel Booking Report\n"
        report += "-" * 30 + "\n"
        for booking in self.bookings:
            report += (f"Name: {booking['name']}, "
                       f"Room Number: {booking['room_number']}, "
                       f"Check-in Date: {booking['check_in_date']}, "
                       f"Check-out Date: {booking['check_out_date']}, "
                       f"Review: {booking['review']}\n")
        return report

    def delete_booking(self, room_number):
        """Delete a booking based on the room number."""
        original_count = len(self.bookings)
        self.bookings = [b for b in self.bookings if b["room_number"] != room_number]
        if len(self.bookings) < original_count:
            print(f"Booking for room {room_number} has been deleted.")
        else:
            print(f"No booking found for room {room_number}.")

    def add_review(self, room_number, review):
        """Add a review to an existing booking."""
        for booking in self.bookings:
            if booking["room_number"] == room_number:
                booking["review"] = review
                print(f"Review added for room {room_number}.")
                return
        print(f"No booking found for room {room_number}.")

    def delete_review(self, room_number):
        """Delete a review from an existing booking."""
        for booking in self.bookings:
            if booking["room_number"] == room_number:
                booking["review"] = None
                print(f"Review deleted for room {room_number}.")
                return
        print(f"No booking found for room {room_number}.")

def main():
    hotel = Hotel()

    while True:
        print("\nHotel Management System")
        print("1. Add Booking")
        print("2. View Bookings")
        print("3. Generate Report")
        print("4. Delete Booking")
        print("5. Add Review")
        print("6. Delete Review")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            try:
                name = input("Enter guest name: ").strip()
                room_number = int(input("Enter room number: ").strip())
                check_in_date = input("Enter check-in date (YYYY-MM-DD): ").strip()
                check_out_date = input("Enter check-out date (YYYY-MM-DD): ").strip()
                hotel.add_booking(name, room_number, check_in_date, check_out_date)
            except ValueError:
                print("Invalid input. Room number must be an integer.")

        elif choice == '2':
            bookings = hotel.get_bookings()
            if not bookings:
                print("No bookings found.")
            else:
                print("\nCurrent Bookings:")
                for booking in bookings:
                    print(f"Name: {booking['name']}, Room Number: {booking['room_number']}, "
                          f"Check-in Date: {booking['check_in_date']}, "
                          f"Check-out Date: {booking['check_out_date']}, "
                          f"Review: {booking['review']}")

        elif choice == '3':
            report = hotel.generate_report()
            print("\nBooking Report:")
            print(report)

        elif choice == '4':
            try:
                room_number = int(input("Enter room number to delete: ").strip())
                hotel.delete_booking(room_number)
            except ValueError:
                print("Invalid input. Room number must be an integer.")

        elif choice == '5':
            try:
                room_number = int(input("Enter room number to add review: ").strip())
                review = input("Enter the review: ").strip()
                hotel.add_review(room_number, review)
            except ValueError:
                print("Invalid input. Room number must be an integer.")

        elif choice == '6':
            try:
                room_number = int(input("Enter room number to delete review: ").strip())
                hotel.delete_review(room_number)
            except ValueError:
                print("Invalid input. Room number must be an integer.")

        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()