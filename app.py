from flask import Flask, request, jsonify
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

# Data dummy (saya mengubah data menjadi data teks untuk keperluan contoh)
data_dummy = [
    ([18, "G07", "G02", "G03", "G04"], "DBD"),
    ([51, "G01", "G04", "G02", "G09"], "DBD"),
    ([15, "G05", "G03", "G03", "G04"], "DBD"),
    ([2, "G01", "G05", "G12", "G13", "G14", "G18"], "DBD"),
    ([19, "G01", "G14", "G05", "G05"], "DBD"),
    ([3, "G07", "G12"], "DBD"),
    ([5, "G05", "G04", "G18"], "DBD"),
    ([24, "G17", "G07", "G07", "G05", "G08", "G08"], "DBD"),
    ([27, "G17", "G14", "G06", "G05", "G06", "G10", "G10"], "DBD"),
    ([13, "G05", "G13", "G02", "G02", "G13", "G16", "G16", "G13", "G09", "G06", "G06"], "DBD"),
    ([13, "G05", "G14", "G13", "G13", "G13", "G13", "G13", "G11"], "DBD"),
    ([5, "G05", "G05", "G07", "G03", "G03", "G13"], "DBD"),
    ([8, "G07", "G17"], "DBD"),
    ([8, "G05", "G07", "G14", "G11", "G13", "G13"], "DBD"),
    ([53, "G07", "G02", "G03"], "DBD"),
    ([89, "G04", "G08", "G15", "G01", "G13", "G07", "G07", "G04", "G13", "G17"], "DBD"),
    ([1, "G09", "G03", "G03", "G01", "G01", "G13", "G11"], "DBD"),
    ([58, "G17", "G17", "G17", "G13", "G13", "G07", "G11", "G17"], "DBD"),
    ([46, "G08", "G18", "G07"], "DBD"),
    ([5, "G01", "G08", "G08"], "DBD"),
    ([12, "G07", "G02", "G03"], "DBD"),
    ([10, "G05", "G14", "G02", "G13"], "DBD"),
    ([22, "G05", "G05"], "DBD"),
    ([2, "G05", "G06", "G04"], "DBD"),
    ([21, "G05", "G02", "G09", "G09"], "DBD"),
    ([14, "G05", "G07", "G11"], "DBD"),
    ([6, "G07", "G08", "G09", "G03"], "DBD"),
    ([7, "G05", "G06", "G09"], "DBD"),
    ([42, "G05", "G03", "G03", "G04"], "DBD"),
    ([13, "G05", "G09", "G04", "G04"], "DBD"),
    ([20, "G17", "G13", "G03", "G04"], "DBD"),
    ([3, "G05", "G13", "G02"], "DBD"),
    ([4, "G05", "G08", "G03", "G09"], "DBD"),
    ([12, "G05", "G12", "G09", "G03"], "DBD"),
    ([13, "G05", "G07", "G13", "G02", "G02"], "DBD"),
    ([2, "G12", "G10"], "DBD"),
    ([35, "G05", "G05"], "DBD"),
    ([92, "G18", "G13", "G14", "G09"], "DBD"),
    ([32, "G03", "G10", "G14", "G05"], "DBD"),
    ([6, "G05", "G17", "G13"], "DBD"),
    ([17, "G05", "G05", "G09", "G15", "G02"], "DBD"),
    ([14, "G05", "G09", "G02", "G03", "G08", "G08"], "DBD"),
    ([3, "G05", "G02", "G03"], "DBD"),
    ([12, "G05", "G02", "G03", "G14"], "DBD"),
    ([6, "G05", "G07"], "DBD"),
    ([8, "G05", "G02", "G08"], "DBD"),
    ([60, "G05", "G05", "G04", "G03"], "DBD"),
    ([14, "G05", "G02", "G02"], "DBD"),
    ([46, "G05", "G01"], "DBD"),
    ([35, "G05", "G07"], "DBD"),
    ([16, "G05", "G17", "G13", "G14"], "DBD"),
    ([9, "G05", "G14", "G10"], "DBD"),
    ([7, "G05", "G13", "G15", "G09"], "DBD"),
    ([18, "G12", "G05", "G02"], "DBD"),
    ([0, "G05", "G05", "G03", "G09"], "DBD"),
    ([23, "G16", "G05", "G14", "G17"], "DBD"),
    ([12, "G05", "G13", "G13", "G18", "G09", "G09"], "DBD"),
    ([16, "G05", "G13", "G09"], "DBD"),
    ([11, "G05", "G09", "G02", "G09"], "DBD"),
    ([10, "G05", "G04", "G13"], "DBD"),
    ([8, "G05", "G05"], "DBD"),
    ([9, "G05", "G13"], "DBD"),
    ([5, "G05", "G13", "G13", "G14"], "DBD"),
    ([10, "G05", "G02", "G03", "G04"], "DBD"),
    ([7, "G05", "G04"], "DBD"),
    ([23, "G05", "G09"], "DBD"),
    ([71, "G05", "G02", "G14", "G13", "G17"], "DBD"),
    ([76, "G05", "G17", "G08"], "DBD"),
    ([22, "G05", "G17"], "DBD"),
    ([71, "G18", "G17", "G04"], "DBD"),
    ([39, "G05", "G05"], "DBD"),
    ([22, "G05", "G17", "G18"], "Non-DBD"),
    ([3, "G13", "G03", "G19"], "Non-DBD"),
    ([5, "G07", "G14", "G08", "G19"], "Non-DBD"),
    ([10, "G14", "G04", "G04", "G19"], "Non-DBD"),
    ([14, "G07", "G13", "G02", "G02", "G19"], "Non-DBD"),
    ([20, "G17", "G13", "G03", "G04", "G18"], "Non-DBD"),
    ([3, "G05", "G13", "G02", "G20"], "Non-DBD"),
    ([4, "G05", "G08", "G03", "G09", "G19"], "Non-DBD"),
    ([12, "G05", "G12", "G09", "G03", "G20"], "Non-DBD"),
    ([13, "G05", "G07", "G13", "G02", "G02", "G19"], "Non-DBD"),
    ([9, "G05", "G13", "G21"], "Non-DBD"),
    ([10, "G05", "G02", "G03", "G04", "G19"], "Non-DBD"),
    ([7, "G05", "G04", "G20"], "Non-DBD"),
    ([23, "G05", "G09", "G20"], "Non-DBD"),
    ([22, "G05", "G17", "G18", "G21"], "Non-DBD"),
    ([71, "G18", "G17", "G04", "G20"], "Non-DBD"),
    ([20, "G04", "G08", "G18", "G19"], "Non-DBD"),
    ([23, "G03", "G09", "G19", "G20"], "Non-DBD"),
    ([26, "G05", "G08", "G19", "G21"], "Non-DBD"),
    ([29, "G05", "G09", "G16", "G20"], "Non-DBD"),
    ([32, "G05", "G14", "G20"], "Non-DBD"),
    ([35, "G06", "G09", "G15", "G19"], "Non-DBD"),
    ([38, "G04", "G14", "G16", "G19"], "Non-DBD"),
    ([41, "G07", "G15", "G20"], "Non-DBD"),
    ([44, "G08", "G21"], "Non-DBD"),
    ([47, "G09", "G18", "G19"], "Non-DBD"),
    ([50, "G11", "G19"], "Non-DBD"),
    ([53, "G13", "G20"], "Non-DBD"),
    ([56, "G15", "G21"], "Non-DBD"),
    ([59, "G06", "G15", "G21"], "Non-DBD")
]

# Membagi data menjadi data latih dan data uji
X = [" ".join(map(str, item[0])) for item in data_dummy]  # Menggabungkan fitur ke dalam teks
y = [item[1] for item in data_dummy]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Mengubah teks menjadi vektor menggunakan CountVectorizer
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Membuat dan melatih model Naive Bayes
naive_bayes = MultinomialNB()
naive_bayes.fit(X_train_vectorized, y_train)

# Memprediksi kelas
y_pred = naive_bayes.predict(X_test_vectorized)

app = Flask(__name__)

@app.route('/klasifikasi', methods=['POST'])
def klasifikasi_penyakit():
    data = request.json
    features = data['features']  # Pastikan data yang diperlukan sesuai dengan format yang diharapkan
    features_text = " ".join(map(str, features))
    features_vectorized = vectorizer.transform([features_text])
    predicted_class = naive_bayes.predict(features_vectorized)
    hasil_klasifikasi = predicted_class[0]
    return jsonify({'hasil_klasifikasi': hasil_klasifikasi})

if __name__ == '__main__':
    app.run(debug=True)