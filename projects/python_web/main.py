from flask import Flask
from random import randint
import sys

from projects.python_calculator.calculator import Calculator

app = Flask(__name__)
my_calculator = Calculator()


@app.route('/')
def hell():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    message = "{} + {} = {}".format(num1, num2, my_calculator.add(num1, num2))
    return message


if __name__ == '__main__':
    print("Python version (string):", sys.version)
    print("Python version info (tuple):", sys.version_info)
    print("Path of the Python executable:", sys.executable)
    print("Path of the script:", __file__)
    app.run()
