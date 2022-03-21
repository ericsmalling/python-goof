import json

from bottle import route, request, template, run, TEMPLATE_PATH, redirect
from pymongo import MongoClient
from time import sleep
from tasks import chef_task
from conf import HOST, PORT, DB, COLL


@route('/', method="GET")
def listquotes():
    client = MongoClient(HOST, PORT)
    db = client[DB]
    collection = db[COLL]

    return template('chefalize', rows=list(collection.find()))


@route('/', method="POST")
def chefalize():
    phrase = request.POST.get('phrase')
    chef_task.delay(phrase)
    sleep(1)
    return redirect('/')


@route('/edit/<id>', method='GET')
def edit(id):
    result = chef_task.AsyncResult(id)
    print('Task id: %s\nState: %s\nResult: %s' % (id, result.state, result.result))
    return template('edit', phrase=result.result, id=id)


@route('/edit', method='POST')
def edit():
    id = request.POST.get('id')
    phrase = request.POST.get('phrase')
    client = MongoClient(HOST, PORT)
    db = client[DB]
    collection = db[COLL]
    update_filter = {'_id': id}
    if collection.find_one(update_filter):
        update = {
            'status': 'FAILURE',
            'result': phrase
        }
        res = collection.update_one(update_filter, {'$set': update})
        if res.modified_count:
            print('Updated task metadata for task id: %s' % id)
            print(update)
        else:
            print('Failed to update task metadata for task id: %s' % id)

    else:
        print('Couldnt find metadata for task id: %s' % id)

    return redirect('/')


# TEMPLATE_PATH.insert(0, '/app/views')
run(host='0.0.0.0', port=8080, debug=False, reloader=False)
