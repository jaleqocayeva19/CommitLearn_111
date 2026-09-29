DROP TABLE IF EXISTS goals;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE goals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    target_days INTEGER NOT NULL,
    checkpoint_total INTEGER NOT NULL,
    checkpoint_done INTEGER DEFAULT 0,
    status TEXT NOT NULL, -- 'active' veya 'backlog'
    FOREIGN KEY (user_id) REFERENCES users (id)
);