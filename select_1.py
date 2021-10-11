import sqlalchemy
#import psycopg2

def seconds_min(seconds_in):
    minute = seconds_in // 60
    sec = seconds_in % 60
    sec = '{:02}'.format(sec)
    return (minute, sec)

db = 'postgresql://polesonair:poles@localhost:5432/05102021'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

sel = connection.execute('SELECT name_of_album FROM albums WHERE release_date = 2018.').fetchall()
print('Альбомы выпущенные в 2018 году:')
for i in sel:
    print(*i)

print()
print('Название и продолжительность самого длительного трека.')
max_time = connection.execute('SELECT MAX(duration) FROM tracklist ').fetchone()
name_max_time = connection.execute(f'SELECT name_of_track FROM tracklist where time = {max_time[0]}').fetchone()

max_time = sec_min(max_time[0])  # секунды в минуты

print(f'Трек: {name_max_time[0]}, длительность: {max_time[0]}:{max_time[1]}')
print()

print('Название треков, продолжительность которых не менее 3,5 минуты.')
long_tracks = connection.execute('SELECT duration, name_of_track FROM tracklist WHERE duration >= 210').fetchall()

for i in long_tracks:
    track_time = sec_min(i[0])
    print(f'Трек: {i[1]}, длительность: {track_time[0]}:{track_time[1]}')
print()

print('Названия сборников, вышедших в период с 2018 по 2020 год включительно.')
sel = connection.execute('SELECT collection, release_date FROM collection WHERE release_date BETWEEN 2018 AND 2020').fetchall()
for i in sel:
    print(f'Сборник: {i[0]}, год выпуска: {i[1]}')
print()

print('Исполнители, чье имя состоит из 1 слова.')
sel = connection.execute('SELECT name_of_artist FROM artist').fetchall()
for i in sel:
    if ' ' not in i[0].strip():
        print(i[0])
print()

print('Название треков, которые содержат слово "я"/"me".')
sel = connection.execute("""SELECT name_of_track FROM tracklist WHERE name_of_track iLIKE 'me %%'
 OR name_of_track iLIKE '%% me %%' OR name_of_track iLIKE '%% me' OR name_of_track iLIKE 'я %%'
 OR name_of_track iLIKE '%% я %%' OR name_of_track iLIKE '%% я'""").fetchall()
for i in sel:
    print(i[0])