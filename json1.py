##       PYTHON JSON
# JSON(JavaScript Object Notation)
# It is mainly used for storing and tranfering data b/w the browser and the server.
# JSON is text, written with JavaScript object notaion.
# Python too suports JSON with a built-in package called JSON.
import json
d={
    'course_name':'Python',
    'fees' : 14000
}
f=json.dumps(d)
print(type(f))
print(f)