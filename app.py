from flask import Flask
from database import conn

app = Flask(__name__)



@app.route('/')
def main():  # put application's code here
    # read from database table flats
    cursor = conn.cursor()
    cursor.execute('''
        SELECT title, image FROM flats LIMIT 500
    ''')
    flats = cursor.fetchall()
    cursor.close()
    
    # create html
    html = """
    <html>
        <body>
            <h1>Flats</h1>
            <ol>

    
    """
    for flat in flats:
        html += """
                <li>
                    <h2>{}</h2>
                    <img src="{}" />
                </li>
        """.format(flat[0], flat[1])

    html += """
            </ol>
        </body>
    </html>
    """

    return html



if __name__ == '__main__':
    app.run()
