#!/usr/bin/env python3

import cgi
import cgitb
cgitb.enable()

print("Content-Type: text/html\n")

form = cgi.FieldStorage()

# Retrieve values
num1 = float(form.getvalue('num1', 0))
num2 = float(form.getvalue('num2', 0))
operation = form.getvalue('operation')

# Perform calculation
if operation == 'add':
    result = num1 + num2
    symbol = '+'
elif operation == 'subtract':
    result = num1 - num2
    symbol = '−'
elif operation == 'multiply':
    result = num1 * num2
    symbol = '×'
elif operation == 'divide':
    if num2 == 0:
        result = 'Error: Division by zero'
    else:
        result = num1 / num2
    symbol = '÷'
else:
    result = 'Invalid operation'

# Output result page
print(f"""
<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Calculation Result</title>
    <link rel=\"stylesheet\" href=\"script.css\">
</head>
<body>
    <div class=\"calculator-container\">
        <h1>Result</h1>
        <p>{num1} {symbol} {num2} = {result}</p>
        <a href=\"index.html\"><button>New Calculation</button></a>
    </div>
</body>
</html>
""")