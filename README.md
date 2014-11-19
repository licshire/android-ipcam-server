android-ipcam-server
====================

Experimental server for android-ipcam project. It is used as very simple server database (sqlite3) of clients sessions. Server provides REST API for session objects manipulation and Other endpoints to list the sessions.


> This server is used as local server and it is implemented using python and Polymer.

> Please **bear in mind** that this project is developed as part of my diploma thesis so It is changing constantly. I cannot accept or merge pull requests and I will provide no support.

Install and run
====================
Requirements and other instructions how to run server.

### Requirements
In order to be able to run this server you need to have [Python](https://www.python.org/downloads/) installed with some additional modules. This project is based on [bottle](http://bottlepy.org/docs/dev/index.html) and uses [sqlite3](https://docs.python.org/2/library/sqlite3.html).

###### Bottle can be easily installed using pip:
```python
pip install bottle
```

### Run the server
Server is going to listen on localhost (all interfaces) at port 8080 - if you download and run the server as is. To change this behavior go to android-ipcam-server.py and change the run(...) command near the end of the script.

Availible API
====================
Below you can find all the APIs provided by server.

### REST API
The server provides some end points for session manipulation. These endpoint are accessible with GET HTTP requests with base address  `http://server.ip.address:port/rest`. Each endpoints are defined:
* **/sessions** - returns all sessions as JSON
* **/sessions/SID** - returns session with SID id as JSON
* **/session/register?name=&url=&content=** - registers new session and sets it's state to 1 (enabled)
  * *name* - name of the session
  * *url* - url address of the stream
  * *content* - additional information for the session
* **/session/SID/edit?name=&url=&content=&status=** - gets the session with SID id and updates its values
  * *name* - name of the session
  * *url* - url address of the stream
  * *content* - additional information for the session
  * *status* - status of session 1 (enabled) and 0 (disabled)
* **/sessions/clear** - removes all sessions from database
* **/session/SID/close** - terminates the session with SID id by setting status to 0

### Other API
* **/sessions** - this will list all sessions with Polymer look
* **/FILE_PATH** - serves any file with given classpath
* **/help** - serves the help (currently nothing)
* **/rest/session/create** - templated HTML for session creation WILL BE REMOVED
* **/rest/session/SID/play** - tempalted view for session streaming WILL BE REMOVED

Licensing
====================
This server is currently licensed under the Apache 2.0 Licensing conditions (see LICENSE file in repository root). This may change in the future.
