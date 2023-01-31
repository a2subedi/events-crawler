FROM postgres:latest
ENV POSTGRES_PASSWORD=locked
ENV POSTGRES_USER=user
ENV POSTGRES_DB=eventsdb
COPY data_schema.sql /docker-entrypoint-initdb.d/data_schema.sql