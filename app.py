from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        print(f"Имя: {name}, Email: {email}, Сообщение: {message}")
        with open('collected_data.txt', 'a') as f:
            f.write(f"Имя: {name}, Email: {email}, Сообщение: {message}\n")

        return 'Форма отправлена'

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
