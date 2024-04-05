from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    pizzas = [
        {'name': 'Маргарита', 'description': 'Помідори, моцарела, базилік', 'price': 150},
        {'name': 'Пепероні', 'description': 'Помідори, пепероні, моцарела', 'price': 170},
        {'name': 'Гавайська', 'description': 'Помідори, ананаси, шинка, моцарела', 'price': 180}
    ]
    return render_template('menu.html', pizzas=pizzas)

if __name__ == "__main__":
    app.run(debug=True)

