# .env file structure

```
DEBUG=true

LOCAL_DB_NAME= local-db-name
LOCAL_DB_USER= local-db-user
LOCAL_DB_PASSWORD= your-password
LOCAL_DB_HOST=127.0.0.1
LOCAL_DB_PORT=5432 

DJANGO_SECRET_KEY= #### only-for-deployment ###
SIMPLE_JWT_SINGNING_KEY= #### only-for-deployment ###

USE_PRODUCTION_DATABASE=<bool-value>

PRODUCTION_DB_NAME= production-db-name
PRODUCTION_DB_USER= production-db-user
PRODUCTION_DB_PASSWORD= db-password
PRODUCTION_DB_HOST= db-host(URL)
PRODUCTION_DB_PORT=5432

```