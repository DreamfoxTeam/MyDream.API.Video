CREATE TABLE IF NOT EXISTS video (
    id integer PRIMARY KEY,
    title varchar(200),
    description longtext NULL,
    seconds integer,
    created datetime default current_timestamp
);

insert into video (title, description, seconds) values ('First Video', 'Desc first video', 30);
insert into video (title, description, seconds) values ('Second Video', 'Desc Second video', 70);
insert into video (title, description, seconds) values ('Third Video', '', 120);

SELECT * FROM video;
