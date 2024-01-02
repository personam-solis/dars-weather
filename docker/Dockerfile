# Builds personamsolis/solis-db

FROM postgres

ENV POSTGRES_PASSWORD=password \
    POSTGRES_USER=postgres \
    POSTGRES_DB=weather

EXPOSE 5432

ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["postgres"]
