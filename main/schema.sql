DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS menu;
DROP TABLE IF EXISTS item;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE menu (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT UNIQUE NOT NULL,
    special BOOLEAN,
    CONSTRAINT menu_unique UNIQUE (category)
);

CREATE TABLE item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER NOT NULL,
    category TEXT NOT NULL,
    code TEXT NOT NULL,
    dish TEXT NOT NULL,
    price TEXT NOT NULL,
    notes TEXT,
    spicy BOOLEAN,
    FOREIGN KEY (author_id) REFERENCES user (id),
    FOREIGN KEY (category) REFERENCES menu (category)
);