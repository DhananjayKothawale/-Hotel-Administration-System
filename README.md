# Hotel Administration System

#### Description:
The Hotel Administration System is a Python project designed for managing hotel room bookings through a command-line interface. Users can add, view, delete, and generate reports for bookings, as well as manage reviews for each booking. The system includes input validation to handle and report errors.

**Main Components:**
- **Hotel Class**: Manages bookings and provides methods for interacting with them.
  - `add_booking(name, room_number, check_in_date, check_out_date)`: Adds a new booking.
  - `get_bookings()`: Retrieves a list of all current bookings.
  - `generate_report()`: Generates a formatted report of all bookings.
  - `delete_booking(room_number)`: Deletes a booking based on the room number.
  - `add_review(room_number, review)`: Adds a review to an existing booking.
  - `delete_review(room_number)`: Deletes a review from an existing booking.

**Usage**:
1. **Add Booking**: Select option 1 and enter the guest details. Room number must be an integer.
2. **View Bookings**: Select option 2 to view all current bookings.
3. **Generate Report**: Select option 3 to generate and view a detailed booking report.
4. **Delete Booking**: Select option 4 and provide the room number to delete a booking. Room number must be an integer.
5. **Add Review**: Select option 5 and provide the room number and review text. Room number must be an integer.
6. **Delete Review**: Select option 6 and provide the room number to delete a review. Room number must be an integer.
7. **Exit**: Select option 7 to exit the program.

**Error Handling**:
- The system will notify you of invalid inputs, such as non-integer room numbers, and invalid menu choices.

**Testing**:
The project includes tests for its core functionalities:
- `test_add_booking()`: Verifies that new bookings are added correctly.
- `test_get_bookings()`: Checks that bookings can be retrieved.
- `test_generate_report()`: Ensures the booking report is generated correctly.
- `test_delete_booking()`: Confirms that bookings can be deleted.
- `test_add_review()`: Verifies that reviews can be added to bookings.
- `test_delete_review()`: Confirms that reviews can be deleted from bookings.

