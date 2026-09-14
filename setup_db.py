import sqlite3

def setup_database():
    conn = sqlite3.connect('procurement_erp.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY,
            supplier_name TEXT,
            risk_level TEXT,
            total_spend REAL
        )
    ''')
    
    cursor.execute("INSERT OR IGNORE INTO suppliers (id, supplier_name, risk_level, total_spend) VALUES (1, 'GlobalTech Solutions', 'Low', 125000.00)")
    cursor.execute("INSERT OR IGNORE INTO suppliers (id, supplier_name, risk_level, total_spend) VALUES (2, 'Nexus Systems', 'High', 34000.00)")
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
