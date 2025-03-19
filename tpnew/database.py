import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect("documents.db")
cursor = conn.cursor()

# Create table to store documents
cursor.execute('''
    CREATE TABLE IF NOT EXISTS documents (
        roll_number TEXT PRIMARY KEY,
        document_type TEXT,
        file_path TEXT
    )
''')

# Insert sample documents
cursor.execute("INSERT INTO documents (roll_number, document_type, file_path) VALUES ('12345', 'bonafide', 'path/to/bonafide_12345.pdf')")
cursor.execute("INSERT INTO documents (roll_number, document_type, file_path) VALUES ('67890', 'noc', 'path/to/noc_67890.pdf')")
cursor.execute("INSERT INTO documents (roll_number, document_type, file_path) VALUES ('54321', 'certificate', 'path/to/certificate_54321.pdf')")

conn.commit()
conn.close()

print("✅ Database setup completed!")
