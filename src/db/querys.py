CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS websites (
        id INTEGER PRIMARY KEY,
        url TEXT NOT NULL,
        processing_time_second REAL,
        links_count INTEGER,
        path TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
"""

ADD_RESULT = """
    INSERT INTO websites
    (url, processing_time_second, links_count, path)
    VALUES (?, ?, ?, ?)
"""

SELECT_RESULTS = """
    SELECT url, processing_time_second, links_count, path
    FROM websites
"""
