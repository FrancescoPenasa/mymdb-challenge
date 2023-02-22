
# build & testing
`docker-compose up -d --build`
`docker ps` identifica il container di del postgres      
`docker exec -i {CONTAINER_PG} /bin/bash -c "PGPASSWORD=postgres psql --username postgres postgres" < dump.sql`
