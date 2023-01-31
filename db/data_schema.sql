DROP TABLE IF EXISTS events;
CREATE TABLE IF NOT EXISTS events
(
    id serial primary key NOT NULL,
    event_time character varying(100) COLLATE pg_catalog."default",
    event_location character varying(200) COLLATE pg_catalog."default",
    event_title character varying(500) COLLATE pg_catalog."default",
    artists text[],
    works text[],
    image_link character varying(500) COLLATE pg_catalog."default",
    event_date character varying(10) COLLATE pg_catalog."default"
)