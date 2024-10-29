import sqlite3
from storage.storage import Storage
import pandas as pd

class SQLStorage(Storage):
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS extracted_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT,
                content BLOB
            )
        ''')  # Content is set to BLOB to support binary data like images
        self.conn.commit()

    def save(self, data, data_type: str):
        """Save extracted data based on its type."""

        if data_type == 'table':
            # Save tables as text
            self._save_table_data(self.cursor, data)
        elif data_type == 'image':
            # Save images as BLOB
            self._save_image_data(self.cursor, data)
        elif data_type == 'url':
            # Save URLs as text
            self._save_url_data(self.cursor, data)
        else:
            # Save text or other types normally
            self._save_text_data(self.cursor, data, data_type)

        self.conn.commit()

    def _save_table_data(self, cursor, tables):
        for table in tables:
            # If the table is a DataFrame, check if it's empty
            if isinstance(table, pd.DataFrame):
                if table.empty:  # Skip empty DataFrames
                    continue
            elif not table:  # Skip empty lists or non-DataFrame tables
                continue

            """
            Convert the table to a string format
            If it's a DataFrame, use its values; otherwise, assume it's a list of lists
            """
            if isinstance(table, pd.DataFrame):
                table_content = "\n".join(
                    ["\t".join(str(cell) for cell in row) for row in table.values]
                )
            else:
                table_content = "\n".join(
                    ["\t".join(str(cell) for cell in row) for row in table]
                )

            try:
                cursor.execute('INSERT INTO extracted_data (type, content) VALUES (?, ?)', ('table', table_content))
            except Exception as e:
                print(f"Error inserting table data into database: {e}")


    def _save_image_data(self, cursor, images):
        """Store images as BLOBs."""
        if isinstance(images, list):
            for item in images:
                if isinstance(item, dict) and 'image_data' in item:
                    image_data = item['image_data']
                    cursor.execute('INSERT INTO extracted_data (type, content) VALUES (?, ?)', ('image', image_data))

    def _save_url_data(self, cursor, urls):
        """Store URLs as text."""
        if isinstance(urls, list):
            for item in urls:
                url = item['url']
                cursor.execute('INSERT INTO extracted_data (type, content) VALUES (?, ?)', ('url', url))

    def _save_text_data(self, cursor, text, data_type):
        """Chunk and save text data."""
        chunks = self._chunk_text(text, 1000)
        for chunk in chunks:
            cursor.execute('INSERT INTO extracted_data (type, content) VALUES (?, ?)', (data_type, chunk))

    def _chunk_text(self, text, chunk_size):
        """Split the text into chunks of specified size."""
        return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    
    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None