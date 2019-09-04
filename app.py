from flask import Flask,render_template,request,redirect,url_for
import socket
import platform

app = Flask(__name__)

def add(x,y):
    return x+y
#getting the details


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y

@app.route('/machineinfo')
def machineinfo():
    #get machine details
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    os_name = platform.system()

    return render_template("machineinfo.html", host_name=host_name, host_ip=host_ip, os_name=os_name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
