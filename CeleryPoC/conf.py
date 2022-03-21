
HOST = 'mongodb'
PORT = 27017
DB = 'celery'
COLL = 'celery-coll'

result_backend = 'mongodb'
mongodb_backend_settings = {
    "host": HOST,
    "port": PORT,
    "database": DB,
    "taskmeta_collection": COLL,
}
