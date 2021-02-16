# To run a flask application

To run the application you can either use the flask command or python’s -m switch with Flask. Before you can do that you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable:

```
$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
 ```
If you are on Windows, the environment variable syntax depends on command line interpreter. On Command Prompt:

```
C:\path\to\app>set FLASK_APP=hello.py
```
And on PowerShell:
```
PS C:\path\to\app> $env:FLASK_APP = "hello.py"
```
Alternatively you can use python -m flask:

```
$ export FLASK_APP=hello.py
$ python -m flask run
 * Running on http://127.0.0.1:5000/
 ```

 Flask restful: for restful api