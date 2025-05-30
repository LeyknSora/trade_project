from fastapi import FastAPI, File, UploadFile
import pandas as pd
import sqlite3
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# SQLite database connection
conn = sqlite3.connect('data.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, column_x REAL, column_y REAL)''')
conn.commit()

@app.post('/process')
async def process_file(file: UploadFile = File(...)):
    # Read CSV file
    contents = await file.read()
    df = pd.read_csv(pd.compat.StringIO(contents.decode('utf-8')))

    # Example preprocessing
    df['column_x'] = df['column_x'] * 2
    df['column_y'] = df['column_y'] + 10

    # Store in SQLite
    df.to_sql('data', conn, if_exists='replace', index=False)

    # Return processed data
    return df.to_dict(orient='records')