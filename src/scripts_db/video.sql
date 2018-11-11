CREATE TABLE IF NOT EXISTS video (
    id integer PRIMARY KEY,
    title varchar(200),
    seconds integer
);

insert into video (title, seconds) values ('First Video', 30);
insert into video (title, seconds) values ('Second Video',70);
insert into video (title, seconds) values ('Third Video', 120);
