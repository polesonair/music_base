create table if not exists Music_Genres(
id_genre serial primary key,
name_of_genre varchar(50) not null unique
);

create table if not exists Artist(
id_artist serial primary key,
name_of_artist varchar(50) not null
)

create table if not exists Albums(
id_album primary key,
name_of_album varchar(40) not null,
release_date integer check(release_date > 1950 and release_date < 2021)
);

create table if not exists Tracklist(
id_track serial primary key,
name_of_track varchar(30) not null,
duration integer check(duration > 0  and duration < 5000),
id_album integer references Albums(id_album)
);

create table if not exists Collection(
id_collection serial primary key,
name_of_collection varchar(40) not null,
release_date integer check(release_date > 1900 and release_date < 2021)
);

create table if not exists Artists_album(
id_artist integer references Artist(id_artist),
id_album integer references Albums(id_album)
);


create table if not exists Artist_Genre(
id_artist integer references Artist(id_artist),
id_genre integer references Music_Genres(id_genre)
);

create table if not exists Tracks_In_Collections(
id_track integer references Tracklist(id_track),
id_collection integer references Collection(id_collection)
);