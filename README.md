Moesha Fundraising Management
A simple command-line application to manage donations for fundraising efforts. This program allows users to add, view, delete, and update donations.

Features
Add a Donation: Input details of a new donation.
View Donations: Display all recorded donations.
Delete a Donation: Remove a specific donation from the records.
Update a Donation: Modify the details of an existing donation.
Exit: Exit the program safely.
Requirements
Python 3.x
donations module (contains functions for managing donations)
Installation
Clone the repository:

bash
Copy code
git clone <repository-url>
Navigate to the project directory:

bash
Copy code
cd <project-directory>
Ensure you have the required packages installed. You might need to set up a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Usage
Start the application by running:

bash
Copy code
python main.py
Follow the on-screen instructions to manage donations.

Functions in donations.py
This module should contain the following functions:
written by mutugi
add_donation(): Prompts the user for donation details and saves it.
view_donations(): Retrieves and displays all donations.
delete_donation(): Asks for a donation ID and removes it from the records.
update_donation(): Updates details of a specific donation based on user input.
