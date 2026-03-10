
import csv
from datetime import datetime, timedelta

file_name = "serum_data.csv"

def add_serum():
    name = input("Enter Serum Name: ")
    opened = input("Enter Opened Date (YYYY-MM-DD): ")
    months = int(input("Months usable after opening: "))
    notes = input("Notes: ")

    opened_date = datetime.strptime(opened, "%Y-%m-%d")
    expiry_date = opened_date + timedelta(days=months*30)

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, opened_date.date(), expiry_date.date(), notes])

    print("Serum saved successfully!")

def check_serums():
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            today = datetime.today().date()

            for row in reader:
                name, opened, expiry, notes = row
                expiry_date = datetime.strptime(expiry, "%Y-%m-%d").date()

                if today > expiry_date:
                    status = "Expired ❌"
                else:
                    status = "Safe to use ✅"

                print("\nSerum:", name)
                print("Opened Date:", opened)
                print("Expiry Date:", expiry)
                print("Status:", status)
                print("Notes:", notes)

    except FileNotFoundError:
        print("No serum data found.")

while True:
    print("\n--- Serum Expiry Tracker ---")
    print("1. Add Serum")
    print("2. Check Serums")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_serum()
    elif choice == "2":
        check_serums()
    elif choice == "3":
        print("Program closed")
        break
    else:
        print("Invalid choice")