import numpy as np
import pandas as pd

def compute_weights(matrix):
    col_sum = matrix.sum(axis=0)
    norm = matrix / col_sum
    return norm.mean(axis=1)

def hitung_ahp():
    criteria = ["Pendidikan", "Penelitian", "Pengabdian Masyarakat", "Kegiatan Penunjang"]
    alternatives = ["Dosen A", "Dosen C", "Dosen E"]

    pairwise_criteria = np.array([
        [1,     2,     3,     4],
        [1/2,   1,     2,     3],
        [1/3, 1/2,     1,     2],
        [1/4, 1/3,   1/2,     1]
    ])
    criteria_weights = compute_weights(pairwise_criteria)

    pendidikan = compute_weights(np.array([
        [1,     3,     4],
        [1/3,   1,     2],
        [1/4, 1/2,     1]
    ]))
    penelitian = compute_weights(np.array([
        [1,     1/2,   3],
        [2,     1,     4],
        [1/3, 1/4,     1]
    ]))
    pengabdian = compute_weights(np.array([
        [1,     5,     7],
        [1/5,   1,     3],
        [1/7, 1/3,     1]
    ]))
    kegiatan = compute_weights(np.array([
        [1,     1,     2],
        [1,     1,     2],
        [1/2, 1/2,     1]
    ]))

    global_scores = (
        pendidikan * criteria_weights[0] +
        penelitian * criteria_weights[1] +
        pengabdian * criteria_weights[2] +
        kegiatan * criteria_weights[3]
    )

    df = pd.DataFrame({
        "Dosen": alternatives,
        "Skor Akhir": global_scores
    }).sort_values(by="Skor Akhir", ascending=False)

    return df.values.tolist()  # Kirim ke template sebagai list
