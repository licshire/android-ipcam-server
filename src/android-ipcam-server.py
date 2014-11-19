__author__ = 'jan.chvala'

import sqlite3
import os
import db.db_init
import json
from bottle import get, run, debug, template, request, static_file, error


DB_NAME = 'db/sessions.db'
POLYMER_ROOT = os.getcwd() + "/polymer/"


# API for getting all session in JSON
@get('/rest/sessions')
def rest_session_list():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM session;")
    all_sessions = c.fetchall()
    c.close()
    result = []
    for session in all_sessions:
        s = {'id': session[0], 'name': session[1], 'url': session[2], 'content': session[3], 'status': session[4]}
        result.append(s)
    return json.dumps(result)


@get('/')
@get('/sessions')
def session_list():
    return template(POLYMER_ROOT + '/index.tpl')


@get('/rest/session/register')
def rest_session_register():
    name = request.GET.get('name', '').strip()
    url = request.GET.get('url', '').strip()
    content = request.GET.get('content', '').strip()
    conn = sqlite3.connect(DB_NAME)

    c = conn.cursor()
    c.execute("INSERT INTO session (name,url,content,status) VALUES (?,?,?,?)", (name, url, content, 1))
    new_id = c.lastrowid
    conn.commit()
    c.close()

    return {'id': new_id, 'name': name, 'url': url, 'content': content, 'status': 1}


@get('/rest/session/create')
def rest_session_create():
    return template('templates/new_session.tpl')


@get('/rest/session/:sid#[0-9]+#/edit')
def rest_session_edit(sid):
    if request.GET.get('save', '').strip():
        name = request.GET.get('name', '').strip()
        url = request.GET.get('url', '').strip()
        content = request.GET.get('content', '').strip()
        status = request.GET.get('status', '').strip()

        if status == 'active':
            status = 1
        else:
            status = 0

        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        update_statement = "UPDATE session SET name = ?, url = ?, content = ?, status = ? WHERE id LIKE ?"
        c.execute(update_statement, (name, url, content, status, sid))
        conn.commit()

        return '<p>The item number %s was successfully updated</p>' % sid

    else:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("SELECT name, url, content FROM session WHERE id = ?", (sid,))
        cur_data = c.fetchone()

        return template('templates/edit_session', old=cur_data, no=sid)


@get('/rest/sessions/clear')
def rest_session_clear_all():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM session")
    conn.commit()
    return rest_session_list()


@get('/rest/session/:sid#[0-9]+#/close')
def rest_session_close(sid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE session SET status = 0 WHERE id = ?", (sid,))
    conn.commit()
    return rest_session_get(sid)


@get('/rest/session/:sid#[0-9]+#/play')
def rest_session_play(sid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT id,name,url,content FROM session WHERE id = ?", (sid,))
    result = c.fetchone()
    c.close()

    if not result:
        return '<p>Session with ID %s does not exist</p>' % sid
    else:
        return template('templates/show_stream', sid=result[0], name=result[1], url=result[2], content=result[3])


@get('/rest/session/:sid#[0-9]+#')
def rest_session_get(sid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT id,name,url,content,status FROM session WHERE id = ?", (sid,))
    result = c.fetchone()
    c.close()

    if not result:
        return {'error': ' Session with ID does not exist!' % sid}
    else:
        return {'id': result[0], 'name': result[1], 'url': result[2], 'content': result[3], 'status': result[4]}


@get('/help')
def show_help():
    return template(POLYMER_ROOT + '/help.tpl')


@get('/<file_path:path>')
def server_static(file_path):
    path = POLYMER_ROOT + file_path
    if os.path.isdir(path):
        index_html = path + '/index.html'
        return static_file(index_html, root='.')
    else:
        return static_file(path, root='.')


@error(403)
def mistake403(code):
    return 'There is a mistake in your url!'


@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'


# will be called periodically to mark expired sessions
def check_expired_sessions():
    return True


# check if given url is reachable
def check_url_reachable(host):
    return True


# init database if it is not created
if not os.path.isfile(DB_NAME):
    db.db_init.init_database()


# server runs in debug mode
debug(True)
# run the server host="0.0.0.0" means that server is listening on every interface available
run(host="0.0.0.0", port=8080, reloader=True)
# remove reloader=True and debug(True) when you move your application from development to a productive environment
