from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books/<book_id>')
def read_book(book_id):
    try:
        with open(f'books/{book_id}.txt', 'r') as book_file:
            content = book_file.read()
        return render_template('read_book.html', content=content)
    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
