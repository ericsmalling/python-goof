from bottle import route, request, response, template, run

@route('/search')
@route('/search/')
def display_search():
    search_query = request.query.q
    return template('search_template', query=search_query)

run(host='0.0.0.0', port=8080, debug=False, )
