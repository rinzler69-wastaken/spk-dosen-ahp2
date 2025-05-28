from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route('/')
@app.route('/')
def index():
    nama = ['Dosen A', 'Dosen B', 'Dosen C']
    return render_template('index.html', nama=nama)

@app.route('/hasil', methods=['POST'])
def hasil():
    # Ambil nama dosen
    nama = request.form.getlist('nama[]')

    # Ambil nilai pairwise (segitiga atas)
    m_01 = float(request.form['m_01'])
    m_02 = float(request.form['m_02'])
    m_12 = float(request.form['m_12'])

    # Buat matriks AHP
    A = np.array([
        [1,    m_01, m_02],
        [1/m_01, 1,  m_12],
        [1/m_02, 1/m_12, 1]
    ])

    # Normalisasi & bobot
    col_sum = A.sum(axis=0)
    norm = A / col_sum
    weights = norm.mean(axis=1)

    hasil_perhitungan = list(zip(nama, weights))
    return render_template('hasil.html', hasil=hasil_perhitungan)

if __name__ == '__main__':
    app.run(debug=True)

