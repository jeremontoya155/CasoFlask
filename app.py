from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Manejo del archivo subido
        file = request.files['file']
        if file.filename.endswith('.xls') or file.filename.endswith('.xlsx'):
            df = pd.read_excel(file)
            return render_template('index.html', tables=[df.to_html(classes='data')], titles=df.columns.values)
        elif file.filename.endswith('.txt'):
            content = file.read().decode('utf-8')
            rows = content.split('\n')
            return render_template('index.html', rows=rows)
        else:
            return "Formato de archivo no soportado."
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
