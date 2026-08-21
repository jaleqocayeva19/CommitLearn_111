DROP TABLE IF EXISTS goals;

CREATE TABLE goals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    target_days INTEGER NOT NULL,
    checkpoint_total INTEGER NOT NULL,
    checkpoint_done INTEGER DEFAULT 0,
    last_update_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    drop_reason TEXT
);