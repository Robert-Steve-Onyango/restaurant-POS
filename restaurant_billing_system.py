from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.simpledialog import askstring
from datetime import datetime
import os


# import pandas as pd

class ViewBillsWindow:
    def __init__(self, parent, saved_bills):
        self.parent = parent
        self.saved_bills = saved_bills

        self.window = Toplevel(parent)
        self.window.title("View All Bills")
        self.window.geometry("400x300")

        self.bills_textbox = Text(self.window, font=("arial", 12))
        self.bills_textbox.pack(fill=BOTH, expand=1)

        self.populate_bills()

    def populate_bills(self):
        self.bills_textbox.delete("1.0", END)
        self.bills_textbox.insert(END, "View All Bills\n")
        self.bills_textbox.insert(END, "-----------------------\n")

        for code, info in self.saved_bills.items():
            self.bills_textbox.insert(END, f"Code: {code}\n")
            self.bills_textbox.insert(END, f"File Name: {info['file_name']}\n")
            self.bills_textbox.insert(END, f"Timestamp: {info['timestamp']}\n")
            self.bills_textbox.insert(END, "-----------------------\n")

def view_all_bills(saved_bills):
    root = Tk()
    root.title("View All Bills")
    root.geometry("400x300")

    ViewBillsWindow(root, saved_bills)

    root.mainloop()



class RestaurantBillingSystem():
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Billing System")
        self.root.geometry("1350x700+0+0")

        # Variables
        self.menu = {}
        self.orders = {}
        self.total_price = 0

        self.menu = {
            "A Cup of Tea": 30,
            "Lemon Tea": 20,
            "Black Tea": 20,
            "Black Coffee": 40,
            "White Coffee": 50,
            "Porridge": 30,
            "Mineral Water(500ml)": 40,
            "Mineral Water(1l)": 60,
            "Mineral Water(1.25l)": 80,
            "A Glass of Milk": 50,
            "Soda (500ml)": 60,
            "Soda (300ml)": 40,
            "A Packet of Mala": 100,
            "Chapatti": 20,
            "Ndazi": 20,
            "Sausage": 50,
            "Toast Bread": 30,
            "Nduma": 50,
            "Smokies": 40,
            "Chips": 120,
            "Matoke": 50,
            "Chicken Fry": 350,
            "Chicken Stew": 300,
            "Beef Fry": 220,
            "Beef Stew": 200,
            "Beef choma": 170,
            "Boil": 170,
            "Matumbo Fry": 170,
            "Matumbo Stew": 150,
            "Maini": 150,
            "Samaki Dry Fry": 300,
            "Samaki Stew": 220,
            "Rice Beans": 80,
            "Chapatti Beans": 50,
            "Mboga Mix": 130,
            "Mboga Ugali": 80,
            "Mbuzi Choma": 80,
            "Aaliyah": 300,
            "Kamongo": 300,
            "Dek Plain": 120,
            "Dek Mix": 150,
            "Rice Dengu": 80,
            "Managu Plain": 120,
            "Managu Mix": 150,
            "Chicken stew": 350,
            "Maini": 200,
            "Samaki fresh": 300,
            "Samaki fry stew": 350,
            "Samaki dry fry": 350,
            "Dasani 500ml": 50,
            "Dasani 1 ltr": 80,
            "M.water 500ml": 30,
        }

        # Create Menu
        self.menu_frame = LabelFrame(self.root, text="Menu", font=("arial", 15, "bold"), bd=2, relief=RIDGE)
        self.menu_frame.place(x=0, y=60, width=400, height=600)

        # Create Order Frame
        self.order_frame = LabelFrame(self.root, text="Order", font=("arial", 15, "bold"), bd=2, relief=RIDGE)
        self.order_frame.place(x=400, y=60, width=450, height=600)

        # Create Bill Frame
        self.bill_frame = LabelFrame(self.root, text="Bill", font=("arial", 15, "bold"), bd=2, relief=RIDGE)
        self.bill_frame.place(x=850, y=60, width=400, height=600)

        # Create Menu Table
        self.menu_table = ttk.Treeview(self.menu_frame, columns=("Item", "Price"))
        self.menu_table.heading("Item", text="Item")
        self.menu_table.heading("Price", text="Price")
        self.menu_table.pack(fill=BOTH, expand=1)

        # Create Order Table
        self.order_table = ttk.Treeview(self.order_frame, columns=("Item", "Quantity", "Price"))
        self.order_table.heading("Item", text="Item")
        self.order_table.heading("Quantity", text="Quantity")
        self.order_table.heading("Price", text="Price")
        self.order_table.pack(fill=BOTH, expand=1)

        # Create Bill Textbox
        self.bill_textbox = Text(self.bill_frame, font=("arial", 15))
        self.bill_textbox.pack(fill=BOTH, expand=1)

        # Create Buttons
        self.add_item_button = Button(self.menu_frame, text="Add Item", font=("arial", 14, "bold"),
                                      command=self.add_item)
        self.add_item_button.place(x=10, y=450)

        self.remove_item_button = Button(self.order_frame, text="Remove Item", font=("arial", 14, "bold"),
                                         command=self.remove_item)
        self.remove_item_button.place(x=10, y=450)

        self.calculate_bill_button = Button(self.order_frame, text="Calculate Bill", font=("arial", 14, "bold"),
                                            command=self.calculate_bill)
        self.calculate_bill_button.place(x=150, y=450)

        self.clear_order_button = Button(self.order_frame, text="Clear Order", font=("arial", 14, "bold"),
                                         command=self.clear_order)
        self.clear_order_button.place(x=300, y=450)

        self.clear_bill_button = Button(self.bill_frame, text="Clear Bill", font=("arial", 14, "bold"),
                                        command=self.clear_bill)
        self.clear_bill_button.place(x=10, y=500)

        self.exit_button = Button(self.root, text="Exit", font=("arial", 14, "bold"), command=self.exit_restaurant)
        self.exit_button.place(x=1200, y=650)

        self.view_all_bills_button = Button(self.bill_frame, text="View All Bills", font=("arial", 14, "bold"),
                                            command=lambda: view_all_bills(self.saved_bills))
        self.view_all_bills_button.place(x=200, y=500)

        # Populate Menu

        # (add other menu items)
        def add_item(self, item):
            price = self.menu[item]

            if item in self.orders:
                self.orders[item] += 1
            else:
                self.orders[item] = 1

            self.order_table.insert("", "end", values=(item, self.orders[item], price))

            self.total_price += price

        def on_menu_item_click(self, event):
            # Get the selected item from the menu_table
            selected_item = self.menu_table.item(self.menu_table.selection())["values"][0]

            # Add the selected item to the order
            self.add_item(selected_item)

        def populate_menu(self):
            # Display Menu
            for item, price in self.menu.items():
                self.menu_table.insert("", "end", values=(item, price))

            # Bind the on_menu_item_click method to the left mouse click event on menu_table
            self.menu_table.bind("<ButtonRelease-1>", self.on_menu_item_click)

        heading_label = Label(self.root, text="Nyathi Nyakach Hotel", font=("arial", 20, "bold"), fg="blue")
        heading_label.place(x=500, y=10)

        # Sub-heading
        sub_heading_label = Label(self.root, text="TILL NUMBER 8881308", font=("arial", 16, "italic"), fg="green")
        sub_heading_label.place(x=520, y=50)

        # Display Menu
        for item, price in self.menu.items():
            self.menu_table.insert("", "end", values=(item, price))

        # Create Save Bill Button
        self.save_bill_button = Button(self.bill_frame, text="Save Bill", font=("arial", 14, "bold"),
                                       command=self.save_and_print_bill)
        self.save_bill_button.place(x=10, y=450)

        self.saved_bills = {}

        # Add this button creation in your __init__ method
        self.view_saved_bills_button = Button(self.bill_frame, text="View All Bills", font=("arial", 14, "bold"),
                                              command=self.view_saved_bills)
        self.view_saved_bills_button.place(x=200, y=500)

    def add_item(self):
        item = self.menu_table.item(self.menu_table.selection())["values"][0]
        price = self.menu[item]

        if item in self.orders:
            self.orders[item] += 1
        else:
            self.orders[item] = 1

        self.order_table.insert("", "end", values=(item, self.orders[item], price))

        self.total_price += price

    def remove_item(self):
        item = self.order_table.item(self.order_table.selection())["values"][0]
        price = self.menu[item]

        if self.orders[item] > 1:
            self.orders[item] -= 1
        else:
            del self.orders[item]

        self.order_table.delete(self.order_table.selection())

        self.total_price -= price

    def clear_order(self):
        self.order_table.delete(*self.order_table.get_children())
        self.orders = {}
        self.total_price = 0

    def calculate_bill(self):

        self.bill_textbox.delete("1.0", END)
        self.bill_textbox.insert(END, "Nyathi Nyakach Hotel\n")
        self.bill_textbox.insert(END, "-----------------------\n")
        self.bill_textbox.insert(END, "Bill Details\n")
        self.bill_textbox.insert(END, "-----------------------\n")
        self.bill_textbox.insert(END, "Till NO: 8881308\n")
        self.bill_textbox.insert(END, "-----------------------\n")

        for item, quantity in self.orders.items():
            self.bill_textbox.insert(END, f"{item} x {quantity} = {self.menu[item] * quantity}\n")
        self.bill_textbox.insert(END, "-----------------------\n")
        self.bill_textbox.insert(END, f"Total Price: {self.total_price}")

    def clear_bill(self):
        self.bill_textbox.delete("1.0", END)



    def view_saved_bills(self):
        # Display a list of saved bills with their codes, file names, and timestamps
        for code, info in self.saved_bills.items():
            print(f"Code: {code}, File Name: {info['file_name']}, Timestamp: {info['timestamp']}")

    def exit_restaurant(self):
        self.root.destroy()

    def mainloop(self):
        self.root.mainloop()

    def save_and_print_bill(self):
        try:
            # Generate a unique code for the bill
            bill_code = f"NTNY{len(self.saved_bills) + 1:03}"

            # Ask user for the file name
            file_name = askstring("Served by:", "Enter the name of the waiter/waitress:", parent=self.root)

            if file_name:
                with open(file_name, "w") as file:
                    file.write(self.bill_textbox.get("1.0", END))

                # Store the bill in the dictionary with the generated code as the key
                self.saved_bills[bill_code] = {
                    'file_name': file_name,
                    'content': self.bill_textbox.get("1.0", END),
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

                messagebox.showinfo("Save Bill", f"Bill saved successfully with code: {bill_code}")

                # Print the bill
                self.print_bill(file_name)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def print_bill(self, file_name):
    # Print the content of the bill
        os.startfile(file_name, "print")




root = Tk()
app = RestaurantBillingSystem(root)
app.mainloop()