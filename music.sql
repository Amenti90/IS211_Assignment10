CREATE TABLE musician (
    id INTEGER PRIMARY KEY NOT NULL,
    stage_name TEXT
);

CREATE TABLE album(
    id INTEGER PRIMARY KEY NOT NULL
    album_name TEXT
    musician_id
);

CREATE TABLE song(
    id INTEGER PRIMARY KEY NOT NULL
    song_name TEXT
    trackLength INTEGER
    album_id INTEGER
    trackNum INTEGER
    FOREIGN KEY album_id REFERENCES album(id))
);