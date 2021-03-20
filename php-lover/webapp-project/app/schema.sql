DROP TABLE IF EXISTS calculate_history;

CREATE TABLE calculate_history (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    input   TEXT    NOT NULL,
    result  TEXT
);
