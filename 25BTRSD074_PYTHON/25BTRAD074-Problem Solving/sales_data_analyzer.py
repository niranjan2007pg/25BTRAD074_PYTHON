"""
Mini Project - Unit 3: Sales Data Analyzer
Problem Solving Component - Python Programming Laboratory
Student Name: Niranjan P G
USN: 25BTRAD074
Branch: B.Tech CSE (AI & DE) | Sem: 3rd Sem | Class: CSE-AIDE (B)
Academic Year: 2026 - 2027
"""

def initialize_sales_catalog():
    """Initializes and returns an empty sales catalog dictionary."""
    return {}

def add_product(catalog, product_id, name, unit_price, quantity_sold=0):
    """Adds a new product to the catalog using nested dictionary structures."""
    if product_id not in catalog:
        catalog[product_id] = {
            "name": name,
            "price": float(unit_price),
            "quantity": int(quantity_sold)
        }

def record_sale(catalog, product_id, additional_quantity):
    """Updates product sales record by adding sold quantity."""
    if product_id in catalog:
        catalog[product_id]["quantity"] += int(additional_quantity)

def update_price(catalog, product_id, new_price):
    """Updates the unit price of an existing product."""
    if product_id in catalog:
        catalog[product_id]["price"] = float(new_price)

def calculate_product_revenue(unit_price, quantity):
    """Calculates revenue for a given product."""
    return round(unit_price * quantity, 2)

def calculate_totals(catalog):
    """Computes total units sold and grand total revenue."""
    total_qty = sum(p["quantity"] for p in catalog.values())
    grand_rev = sum(calculate_product_revenue(p["price"], p["quantity"]) for p in catalog.values())
    return total_qty, grand_rev

def identify_highest_selling(catalog):
    """Identifies top products by volume and by revenue."""
    top_volume = max(catalog.items(), key=lambda x: x[1]["quantity"])
    top_revenue = max(catalog.items(), key=lambda x: calculate_product_revenue(x[1]["price"], x[1]["quantity"]))
    return top_volume, top_revenue

def display_summary(catalog, title="SALES REVENUE & PRODUCT PERFORMANCE REPORT"):
    """Displays comprehensive tabular sales summary and performance metrics."""
    total_qty, grand_rev = calculate_totals(catalog)
    top_vol, top_rev = identify_highest_selling(catalog)

    print("=" * 80)
    print(f"{title:^80}")
    print("=" * 80)
    print(f"{'ID':<8} | {'Product Name':<22} | {'Price (₹)':<11} | {'Qty Sold':<9} | {'Revenue (₹)':<14} | {'Share'}")
    print("-" * 80)

    # Sort products by revenue descending
    sorted_prods = sorted(catalog.items(), key=lambda x: calculate_product_revenue(x[1]["price"], x[1]["quantity"]), reverse=True)
    for pid, data in sorted_prods:
        rev = calculate_product_revenue(data["price"], data["quantity"])
        share = (rev / grand_rev * 100) if grand_rev > 0 else 0.0
        print(f"{pid:<8} | {data['name']:<22} | {data['price']:<11,.2f} | {data['quantity']:<9} | {rev:<14,.2f} | {share:<5.1f}%")

    print("-" * 80)
    print(f"Total Products: {len(catalog):<8} | Total Units Sold: {total_qty:<8} | Grand Total Revenue: ₹{grand_rev:,.2f}")
    print("=" * 80)
    
    vol_p = top_vol[1]
    rev_p = top_rev[1]
    print(f"★ Top Volume Seller   : {vol_p['name']} ({vol_p['quantity']} units sold)")
    print(f"★ Top Revenue Earner  : {rev_p['name']} (₹{calculate_product_revenue(rev_p['price'], rev_p['quantity']):,.2f} generated)")
    print("=" * 80)

def main():
    print("=== Sales Data Analytics & Reporting System (Unit 3) ===")
    print("Student: Niranjan P G | USN: 25BTRAD074 | Branch: CSE (AI & DE)\n")

    catalog = initialize_sales_catalog()
    products = [
        ("P101", "Wireless Mouse",      750.00,  45),
        ("P102", "Mechanical Keyboard", 3200.00, 20),
        ("P103", "27-inch 4K Monitor", 24500.00,  6),
        ("P104", "USB-C Multiport Hub", 1499.00, 35),
        ("P105", "Noise-Cancelling Mic", 4800.00, 12),
        ("P106", "HDMI 2.1 Cable (2m)",  450.00, 80)
    ]
    for pid, name, price, qty in products:
        add_product(catalog, pid, name, price, qty)
    print(f"[+] Loaded inventory catalog with {len(products)} products.")

    # Record real-time sales transactions & price promotion
    record_sale(catalog, "P101", 15)  # Mouse +15
    record_sale(catalog, "P103", 2)   # Monitor +2
    record_sale(catalog, "P106", 25)  # Cable +25
    print("[+] Processed afternoon transaction batch across active SKUs.")

    print("[Promo Event] Applying flash promotional discount on Mechanical Keyboard (P102):")
    update_price(catalog, "P102", 2800.00)
    record_sale(catalog, "P102", 15)
    print(f"[✓] Price updated to ₹2,800.00. Recorded 15 promo units sold (Total: {catalog['P102']['quantity']} units).\n")

    # Display Comprehensive Analytics Report
    display_summary(catalog, "ELECTRONICS & ACCESSORIES SALES PERFORMANCE REPORT")

if __name__ == "__main__":
    main()
