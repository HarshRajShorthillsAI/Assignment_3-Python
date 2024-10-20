import sqlite3
from storage.storage import Storage

class SQLStorage(Storage):
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS extracted_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT,
                content BLOB
            )
        ''') #content set to blob in order to support binary data like image
        conn.commit()
        conn.close()

    def save(self, data, data_type: str):
        """Save extracted data based on its type."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        if data_type == 'table':
            row_accumulator = []  # To collect cells into rows
            row_length = 3  # Assume tables have 3 columns, adjust this based on your table structure

            for table in data:
                table_content_list = []

            for idx, cell in enumerate(table):
                row_accumulator.append(str(cell))  # Accumulate cells as strings
                if (idx + 1) % row_length == 0:  # Once we have enough cells for a row
                    table_content_list.append("\t".join(row_accumulator))  # Join the row
                    row_accumulator = []  # Reset for the next row

            # If there are any leftover cells, add them as a row
            if row_accumulator:
                table_content_list.append("\t".join(row_accumulator))

            # Combine all rows into a single string with newline separation
            table_content = "\n".join(table_content_list)
            cursor.execute('INSERT INTO extracted_data (type, content) VALUES (?, ?)', (data_type, table_content))

        elif data_type == 'image':
            # Save images as BLOB
            if isinstance(data, list):
                for item in data:
                    if isinstance(item, dict) and 'image_data' in item:
                        image_data = item['image_data']
                        cursor.execute('INSERT INTO extracted_data (type, content) VALUES (?, ?)', (data_type, image_data))
        else:
            # Save text or other types normally
            chunks = self._chunk_text(data, 1000)
            for chunk in chunks:
                cursor.execute('INSERT INTO extracted_data (type, content) VALUES (?, ?)', (data_type, chunk))

        conn.commit()
        conn.close()

    def _chunk_text(self, text, chunk_size):
        """Split the text into chunks of specified size."""
        return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]