#!/bin/bash
need_init=0

echo "Running the init script"

if [ $(mongosh localhost:27017 --eval 'db.getMongo().getDBNames().indexOf("appDb")' --quiet) -lt 0 ] || \
   [ $(mongosh localhost:27017/appDb --eval 'db.getCollectionNames().indexOf("users")' --quiet) -lt 0 ] || \
   [ $(mongosh localhost:27017/appDb --eval 'db.getCollectionNames().indexOf("reminders")' --quiet) -lt 0 ]; then
    
    need_init=1
    echo "I am gonna initialize the db..."
    # Drop the whole databases in case some collections, but not all of them
    mongosh localhost:27017 --eval 'db.dropDatabase("appDb")' --quiet
else 
    need_init=0
    echo "Db already initialized"
fi

if [ "$need_init" -eq "1" ]; then
    echo "Initialization procedure started..."
    mongosh localhost:27017 --eval 'use appDb' --quiet
    mongoimport --db appDb --collection users --file /app/users.json --jsonArray
    mongoimport --db appDb --collection reminders --file /app/reminders.json --jsonArray
    mongosh localhost:27017/appDb --eval "db.createUser({user:\"$MONGODB_USER\",pwd:\"$MONGODB_PW\",roles:[\"readWrite\"]})" --quiet

    echo "Db initialized!"
fi

echo "Initialization routine finished"