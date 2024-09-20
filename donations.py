import sqlite3
from db import connect, create_table

# Ensure table is created when module is imported
create_table()

def add_donation():
    conn = connect()
    cursor = conn.cursor()

    donor_name = input("Enter donor's name: ")
    donation_type = input("Enter donation type (funds, food, clothes): ")
    amount_or_quantity = input("Enter amount (if funds) or quantity (if food/clothes): ")
    
    cursor.execute('''
        INSERT INTO donations (donor_name, donation_type, amount_or_quantity)
        VALUES (?, ?, ?)
    ''', (donor_name, donation_type, amount_or_quantity))
    
    conn.commit()
    conn.close()
    print("Donation added successfully!\n")

def view_donations():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM donations')
    records = cursor.fetchall()
    
    if records:
        print("\nList of all donations:")
        for row in records:
            print(f"ID: {row[0]}, Donor: {row[1]}, Type: {row[2]}, Amount/Quantity: {row[3]}")
        print("\n")
    else:
        print("\nNo donations found.\n")

    conn.close()

def delete_donation():
    conn = connect()
    cursor = conn.cursor()

    donation_id = input("Enter the ID of the donation to delete: ")
    cursor.execute('DELETE FROM donations WHERE id = ?', (donation_id,))
    
    if cursor.rowcount > 0:
        conn.commit()
        print(f"Donation with ID {donation_id} deleted successfully!\n")
    else:
        print(f"No donation found with ID {donation_id}.\n")

    conn.close()

def update_donation():
    conn = connect()
    cursor = conn.cursor()

    donation_id = input("Enter the ID of the donation to update: ")
    donor_name = input("Enter new donor name: ")
    donation_type = input("Enter new donation type (funds, food, clothes): ")
    amount_or_quantity = input("Enter new amount (if funds) or quantity (if food/clothes): ")
    
    cursor.execute('''
        UPDATE donations
        SET donor_name = ?, donation_type = ?, amount_or_quantity = ?
        WHERE id = ?
    ''', (donor_name, donation_type, amount_or_quantity, donation_id))
    
    if cursor.rowcount > 0:
        conn.commit()
        print(f"Donation with ID {donation_id} updated successfully!\n")
    else:
        print(f"No donation found with ID {donation_id}.\n")

    conn.close()
