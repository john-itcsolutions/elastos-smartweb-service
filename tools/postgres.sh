#!/bin/bash 

if [[ "$OSTYPE" == "darwin"* ]]; then
    # Mac OSX
    export PATH="/usr/local/opt/openssl/bin:$PATH"
fi

set -euo pipefail

sudo rm -f privkey.pem server.crt server.key server.req

# generate the server.key and server.crt
openssl req -new -text -passout pass:abcd -subj /CN=localhost -out server.req
openssl rsa -in privkey.pem -passin pass:abcd -out server.key
openssl req -x509 -in server.req -text -key server.key -out server.crt

if [[ "$OSTYPE" == "linux-gnu" ]]; then
    # linux
    sudo chown 0:70 server.key
    sudo chmod 640 server.key
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # Mac OSX
    sudo chmod 600 server.key
    sudo chown $USER server.key
fi

docker container stop smartweb-postgres || true && docker container rm -f smartweb-postgres || true

# start a postgres docker container, mapping the .key and .crt into the image.
docker run -d --name smartweb-postgres \
    -v "$PWD/.postgres-data:/var/lib/postgresql/data"     \
    -v "$PWD/server.crt:/var/lib/postgresql/server.crt:ro" \
    -v "$PWD/server.key:/var/lib/postgresql/server.key:ro" \
    -e POSTGRES_DB=smartweb_master                   \
    -e POSTGRES_USER=gmu                         \
    -e POSTGRES_PASSWORD=gmu                     \
    -p 5434:5432                                        \
    postgres:11-alpine                                  \
    -c ssl=on                                           \
    -c ssl_cert_file=/var/lib/postgresql/server.crt     \
    -c ssl_key_file=/var/lib/postgresql/server.key   

# wait for database to start
sleep 5
# Copy .sql files to the running container
docker cp ../grpc_adenine/database/scripts/create_table_scripts.sql smartweb-postgres:/create_table_scripts.sql

# Run the sql scripts 
docker container exec -it smartweb-postgres psql -h localhost -d smartweb_master -U gmu -a -q -f /create_table_scripts.sql
