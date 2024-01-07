# Builds personamsolis/solis-db

FROM postgres

ENV POSTGRES_PASSWORD=password \
    POSTGRES_USER=postgres \
    POSTGRES_DB=weather

RUN chmod -f 777 /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]

STOPSIGNAL SIGINT

EXPOSE 5432

COPY build_weather_db.sql /docker-entrypoint-initdb.d/

CMD ["postgres"]
