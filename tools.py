import sqlite3

def get_supplier_metrics(supplier_name):
    conn = sqlite3.connect('procurement_erp.db')
    cursor = conn.cursor()
    cursor.execute("SELECT risk_level, total_spend FROM suppliers WHERE supplier_name = ?", (supplier_name,))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return f"Supplier: {supplier_name} | Risk: {result[0]} | Spend: ${result[1]}"
    return "Not found"
