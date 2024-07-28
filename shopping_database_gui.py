import tkinter as tk
from tkinter import messagebox
import sqlite3

class ShoppingDatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping Database")

        # Create UI
        self.create_widgets()

    def create_widgets(self):
        # Tabs
        self.tab_control = tk.ttk.Notebook(self.root)

        self.user_tab = tk.Frame(self.tab_control)
        self.product_tab = tk.Frame(self.tab_control)
        self.order_tab = tk.Frame(self.tab_control)

        self.tab_control.add(self.user_tab, text="Users")
        self.tab_control.add(self.product_tab, text="Products")
        self.tab_control.add(self.order_tab, text="Orders")

        self.tab_control.pack(expand=1, fill="both")

        # User Tab
        tk.Label(self.user_tab, text="Username").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.user_tab)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.user_tab, text="Password").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.user_tab, show="*")
        self.password_entry.grid(row=1, column=1)

        tk.Label(self.user_tab, text="Email").grid(row=2, column=0)
        self.email_entry = tk.Entry(self.user_tab)
        self.email_entry.grid(row=2, column=1)

        self.add_user_button = tk.Button(self.user_tab, text="Add User", command=self.add_user)
        self.add_user_button.grid(row=3, column=0, columnspan=2)

        self.view_users_button = tk.Button(self.user_tab, text="View Users", command=self.view_users)
        self.view_users_button.grid(row=4, column=0, columnspan=2)

        # Product Tab
        tk.Label(self.product_tab, text="Product Name").grid(row=0, column=0)
        self.product_name_entry = tk.Entry(self.product_tab)
        self.product_name_entry.grid(row=0, column=1)

        tk.Label(self.product_tab, text="Price").grid(row=1, column=0)
        self.price_entry = tk.Entry(self.product_tab)
        self.price_entry.grid(row=1, column=1)

        tk.Label(self.product_tab, text="Stock").grid(row=2, column=0)
        self.stock_entry = tk.Entry(self.product_tab)
        self.stock_entry.grid(row=2, column=1)

        self.add_product_button = tk.Button(self.product_tab, text="Add Product", command=self.add_product)
        self.add_product_button.grid(row=3, column=0, columnspan=2)

        self.view_products_button = tk.Button(self.product_tab, text="View Products", command=self.view_products)
        self.view_products_button.grid(row=4, column=0, columnspan=2)

        # Order Tab
        tk.Label(self.order_tab, text="User ID").grid(row=0, column=0)
        self.user_id_entry = tk.Entry(self.order_tab)
        self.user_id_entry.grid(row=0, column=1)

        tk.Label(self.order_tab, text="Order Date").grid(row=1, column=0)
        self.order_date_entry = tk.Entry(self.order_tab)
        self.order_date_entry.grid(row=1, column=1)

        tk.Label(self.order_tab, text="Total Amount").grid(row=2, column=0)
        self.total_amount_entry = tk.Entry(self.order_tab)
        self.total_amount_entry.grid(row=2, column=1)

        self.add_order_button = tk.Button(self.order_tab, text="Add Order", command=self.add_order)
        self.add_order_button.grid(row=3, column=0, columnspan=2)

        self.view_orders_button = tk.Button(self.order_tab, text="View Orders", command=self.view_orders)
        self.view_orders_button.grid(row=4, column=0, columnspan=2)

    def add_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()

        conn = sqlite3.connect('shopping.db')
        c = conn.cursor()
        c.execute("INSERT INTO Users (username, password, email) VALUES (?, ?, ?)", (username, password, email))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "User added successfully")
        self.clear_entries()

    def add_product(self):
        name = self.product_name_entry.get()
        price = float(self.price_entry.get())
        stock = int(self.stock_entry.get())

        conn = sqlite3.connect('shopping.db')
        c = conn.cursor()
        c.execute("INSERT INTO Products (name, price, stock) VALUES (?, ?, ?)", (name, price, stock))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Product added successfully")
        self.clear_entries()

    def add_order(self):
        user_id = int(self.user_id_entry.get())
        order_date = self.order_date_entry.get()
        total_amount = float(self.total_amount_entry.get())

        conn = sqlite3.connect('shopping.db')
        c = conn.cursor()
        c.execute("INSERT INTO Orders (user_id, order_date, total_amount) VALUES (?, ?, ?)", (user_id, order_date, total_amount))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Order added successfully")
        self.clear_entries()

    def view_users(self):
        conn = sqlite3.connect('shopping.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Users")
        users = c.fetchall()
        conn.close()

        users_window = tk.Toplevel(self.root)
        users_window.title("Users")

        for i, user in enumerate(users):
            tk.Label(users_window, text=user).grid(row=i, column=0)

    def view_products(self):
        conn = sqlite3.connect('shopping.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Products")
        products = c.fetchall()
        conn.close()

        products_window = tk.Toplevel(self.root)
        products_window.title("Products")

        for i, product in enumerate(products):
            tk.Label(products_window, text=product).grid(row=i, column=0)

    def view_orders(self):
        conn = sqlite3.connect('shopping.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Orders")
        orders = c.fetchall()
        conn.close()

        orders_window = tk.Toplevel(self.root)
        orders_window.title("Orders")

        for i, order in enumerate(orders):
            tk.Label(orders_window, text=order).grid(row=i, column=0)

    def clear_entries(self):
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.product_name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.stock_entry.delete(0, tk.END)
        self.user_id_entry.delete(0, tk.END)
        self.order_date_entry.delete(0, tk.END)
        self.total_amount_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingDatabaseApp(root)
    root.mainloop()
