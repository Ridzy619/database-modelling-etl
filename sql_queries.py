# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE songplays (
        songplay_id SERIAL PRIMARY KEY,
        start_time TIMESTAMP NOT NULL,
        user_id int,
        LEVEL varchar,
        song_id varchar,
        artist_id varchar,
        session_id int,
        LOCATION varchar,
        user_agent varchar
    )
""")

user_table_create = ("""
    CREATE TABLE users (
        user_id int PRIMARY KEY,
        first_name varchar,
        last_name varchar,
        gender varchar,
        level varchar
    )
""")

song_table_create = ("""
    CREATE TABLE songs (
        song_id varchar PRIMARY KEY,
        title varchar,
        artist_id varchar,
        year int,
        duration numeric
    )
""")

artist_table_create = ("""
    CREATE TABLE artists (
        artist_id varchar PRIMARY KEY,
        name varchar,
        location varchar,
        latitude numeric,
        longitude numeric
    )
""")

time_table_create = ("""
    CREATE TABLE time (
        start_time timestamp PRIMARY KEY,
        hour int,
        day int,
        week int,
        month int,
        year int,
        weekday int
    )
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (
        start_time, 
        user_id, 
        level, 
        song_id,
        artist_id,
        session_id,
        location,
        user_agent
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    ON CONFLICT DO NOTHING
    """)

user_table_insert = ("""
    INSERT INTO users
    VALUES (%s,%s,%s,%s,%s)
    ON CONFLICT (user_id)
    DO UPDATE SET user_id = EXCLUDED.user_id
    """)

song_table_insert = ("""
    INSERT INTO songs
    VALUES (%s,%s,%s,%s,%s)
    ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""
    INSERT INTO artists
    VALUES (%s,%s,%s,%s,%s)
    ON CONFLICT DO NOTHING
    """)


time_table_insert = ("""
    INSERT INTO time
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    ON CONFLICT DO NOTHING
    """)

# FIND SONGS

song_select = ("""
    SELECT song_id, artists.artist_id
    FROM songs 
    JOIN artists 
    ON songs.artist_id = artists.artist_id
    WHERE title = %s  AND name = %s AND duration = %s
    """)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]