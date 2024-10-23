import sqlite3
from storage.storage import Storage
import pandas as pd

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
        ''')  # Content is set to BLOB to support binary data like images
        conn.commit()
        conn.close()

    def save(self, data, data_type: str):
        """Save extracted data based on its type."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        if data_type == 'table':
            # Save tables as text
            self._save_table_data(cursor, data)
        elif data_type == 'image':
            # Save images as BLOB
            self._save_image_data(cursor, data)
        elif data_type == 'url':
            # Save URLs as text
            self._save_url_data(cursor, data)
        else:
            # Save text or other types normally
            self._save_text_data(cursor, data, data_type)

        conn.commit()
        conn.close()

    def _save_table_data(self, cursor, tables):
        for table in tables:
            # If the table is a DataFrame, check if it's empty
            if isinstance(table, pd.DataFrame):
                if table.empty:  # Skip empty DataFrames
                    continue
            elif not table:  # Skip empty lists or non-DataFrame tables
                continue

            # Convert the table to a string format
            # If it's a DataFrame, use its values; otherwise, assume it's a list of lists
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




# import sqlite3
# from storage.storage import Storage

# class SQLStorage(Storage):
#     def __init__(self, db_path: str):
#         self.db_path = db_path
#         self._create_table()

#     def _create_table(self):
#         conn = sqlite3.connect(self.db_path)
#         cursor = conn.cursor()
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS extracted_data (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 type TEXT,
#                 content BLOB
#             )
#         ''') #content set to blob in order to support binary data like image
#         conn.commit()
#         conn.close()

#     def save(self, data, data_type: str):
#         """Save extracted data based on its type."""
#         conn = sqlite3.connect(self.db_path)
#         cursor = conn.cursor()

#         if data_type == 'table':
#             row_accumulator = []  # To collect cells into rows
#             row_length = 3  # Assume tables have 3 columns, adjust this based on your table structure

#             for table in data:
#                 table_content_list = []

#             for idx, cell in enumerate(table):
#                 row_accumulator.append(str(cell))  # Accumulate cells as strings
#                 if (idx + 1) % row_length == 0:  # Once we have enough cells for a row
#                     table_content_list.append("\t".join(row_accumulator))  # Join the row
#                     row_accumulator = []  # Reset for the next row

#             # If there are any leftover cells, add them as a row
#             if row_accumulator:
#                 table_content_list.append("\t".join(row_accumulator))

#             # Combine all rows into a single string with newline separation
#             table_content = "\n".join(table_content_list)
#             cursor.execute('INSERT INTO extracted_data (type, content) VALUES (?, ?)', (data_type, table_content))

#         elif data_type == 'image':
#             # Save images as BLOB
#             if isinstance(data, list):
#                 for item in data:
#                     if isinstance(item, dict) and 'image_data' in item:
#                         image_data = item['image']
#                         cursor.execute('INSERT INTO extracted_data (type, content) VALUES (?, ?)', (data_type, image_data))
#         elif data_type == 'url':
#             # Insert each URL into the structured table with columns for url, slide, and text
#             if isinstance(data, list):
#                 for item in data:
#                     if isinstance(item, dict) and 'url' in item:

#                         cursor.execute('INSERT INTO extracted_data (type, content) VALUES (?, ?)', 
#                            (data_type,  item.get('url', None)))
#         else:
#             # Save text or other types normally
#             chunks = self._chunk_text(data, 1000)
#             for chunk in chunks:
#                 cursor.execute('INSERT INTO extracted_data (type, content) VALUES (?, ?)', (data_type, chunk))

#         conn.commit()
#         conn.close()

#     def _chunk_text(self, text, chunk_size):
#         """Split the text into chunks of specified size."""
#         return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]