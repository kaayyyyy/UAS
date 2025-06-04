import sqlite3

def init_db():
    conn = sqlite3.connect('image_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            processed_filename TEXT,
            plot_filename TEXT,
            upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def insert_image(filename, processed_filename, plot_filename):
    conn = sqlite3.connect('image_data.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO images (filename, processed_filename, plot_filename)
        VALUES (?, ?, ?)
    ''', (filename, processed_filename, plot_filename))
    conn.commit()
    conn.close()

def get_all_images():
    conn = sqlite3.connect('image_data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM images ORDER BY upload_time DESC')
    data = c.fetchall()
    conn.close()
    return data
