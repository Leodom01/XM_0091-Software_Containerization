 FROM mongo

COPY . /app

# These two initilize the database with standard data
# They will need to be replaced with an init container that checks if the persistent valume
# already contains a initialized db, if yes moves on, else inits it 
# All the file in /docker-entrypoint-initdb.d/ will be run at container startup, initDb.sh will then be run
COPY initDb.sh /docker-entrypoint-initdb.d/