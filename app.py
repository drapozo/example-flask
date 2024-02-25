from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def input_strings():
    return '''
        <form method="post" action="/result">
            <label>Enter the first string:</label><br>
            <input type="text" name="string1"><br>
            <label>Enter the second string:</label><br>
            <input type="text" name="string2"><br>
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/result', methods=['POST'])
def result():
    string1 = request.form['string1']
    string2 = request.form['string2']

    command = ['python', 'extraccion.py', string1, string2]
    result = subprocess.check_output(command).decode()

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
