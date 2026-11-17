# Mini Project Unit 1: Retail Store Bill Generator
# Student: Niranjan P G | USN: 25BTRAD074
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class BillGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SuperMarket Bill Generator - 25BTRAD074")
        self.root.geometry("450x550")
        self.cart = []

        tk.Label(root, text="SuperMarket Retail Billing System", font=("Helvetica", 14, "bold")).pack(pady=10)
        
        frame = tk.Frame(root)
        frame.pack(pady=5)
        tk.Label(frame, text="Item Name:").grid(row=0, column=0, sticky="w")
        self.item_entry = tk.Entry(frame)
        self.item_entry.grid(row=0, column=1, padx=5, pady=2)
        
        tk.Label(frame, text="Price (Rs.):").grid(row=1, column=0, sticky="w")
        self.price_entry = tk.Entry(frame)
        self.price_entry.grid(row=1, column=1, padx=5, pady=2)
        
        tk.Label(frame, text="Quantity:").grid(row=2, column=0, sticky="w")
        self.qty_entry = tk.Entry(frame)
        self.qty_entry.grid(row=2, column=1, padx=5, pady=2)

        tk.Button(root, text="Add to Cart", command=self.add_item, bg="#4CAF50", fg="white").pack(pady=5)
        
        self.bill_area = tk.Text(root, width=50, height=15)
        self.bill_area.pack(pady=10)

        tk.Button(root, text="Generate Bill", command=self.generate_bill, bg="#2196F3", fg="white").pack(pady=5)

    def add_item(self):
        item = self.item_entry.get().strip()
        try:
            price = float(self.price_entry.get())
            qty = int(self.qty_entry.get())
            if not item or price <= 0 or qty <= 0:
                raise ValueError()
            self.cart.append((item, price, qty, price * qty))
            messagebox.showinfo("Success", f"Added {item} to cart!")
            self.item_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
            self.qty_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Enter valid item, price, and quantity.")

    def generate_bill(self):
        if not self.cart:
            messagebox.showwarning("Warning", "Cart is empty!")
            return
        self.bill_area.delete(1.0, tk.END)
        self.bill_area.insert(tk.END, "=============================================\n")
        self.bill_area.insert(tk.END, "          SUPERMARKET RETAIL BILL\n")
        self.bill_area.insert(tk.END, f" Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        self.bill_area.insert(tk.END, " Student / Cashier: Niranjan P G (25BTRAD074)\n")
        self.bill_area.insert(tk.END, "=============================================\n")
        self.bill_area.insert(tk.END, f"{'Item':<15}{'Price':<10}{'Qty':<8}{'Total':<10}\n")
        self.bill_area.insert(tk.END, "---------------------------------------------\n")
        subtotal = 0.0
        for item, price, qty, total in self.cart:
            self.bill_area.insert(tk.END, f"{item:<15}{price:<10.2f}{qty:<8}{total:<10.2f}\n")
            subtotal += total
        tax = subtotal * 0.05
        grand_total = subtotal + tax
        self.bill_area.insert(tk.END, "---------------------------------------------\n")
        self.bill_area.insert(tk.END, f" Subtotal: Rs.{subtotal:.2f}\n")
        self.bill_area.insert(tk.END, f" GST (5%): Rs.{tax:.2f}\n")
        self.bill_area.insert(tk.END, f" Grand Total: Rs.{grand_total:.2f}\n")
        self.bill_area.insert(tk.END, "=============================================\n")

if __name__ == '__main__':
    root = tk.Tk()
    app = BillGeneratorApp(root)
    root.mainloop()
