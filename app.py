from flask import Flask, request, jsonify
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

app = Flask(__name__)


# Mengonversi data ke dalam format yang dapat digunakan oleh model
data = [
     [4, 10, 50, 3, 'Lolos'],
    [5, 7, 40, 5, 'Lolos'],
    [5, 5, 37, 5, 'Lolos'],
    [4, 5, 40, 4, 'Lolos'],
    [4, 5, 40, 4, 'Lolos'],
    [3, 6, 37, 5, 'Lolos'],
    [3, 5, 45, 4, 'Lolos'],
    [4, 7, 45, 4, 'Lolos'],
    [3, 6, 50, 5, 'Lolos'],
    [4, 10, 50, 3, 'Lolos'],
    [5, 7, 40, 5, 'Lolos'],
    [3, 6, 37, 5, 'Lolos'],
    [2, 2, 20, 3, 'Tidak'],
    [2, 0, 14, 1, 'Tidak'],
    [3, 1, 30, 2, 'Tidak'],
    [1, 0, 23, 2, 'Tidak'],
    [3, 0, 11, 1, 'Tidak'],
    [3, 1, 19, 3, 'Tidak'],
    [3, 1, 21, 3, 'Tidak'],
    [5, 6, 37, 5, 'Lolos'],
    [3, 1, 25, 3, 'Tidak'],
    [2, 0, 17, 3, 'Tidak'],
    [2, 0, 20, 2, 'Tidak'],
    [2, 1, 17, 4, 'Tidak'],
    [1, 1, 9, 1, 'Tidak'],
    [1, 0, 14, 1, 'Tidak'],
    [2, 2, 8, 3, 'Tidak'],
    [3, 0, 24, 3, 'Tidak'],
    [3, 2, 21, 4, 'Tidak'],
    [4, 2, 40, 1, 'Tidak'],
    [3, 2, 32, 4, 'Tidak'],
    [3, 3, 19, 3, 'Tidak'],
    [4, 0, 21, 4, 'Tidak'],
    [2, 1, 17, 4, 'Tidak'],
    [3, 6, 50, 5, 'Lolos'],
    [2, 4, 32, 2, 'Tidak'],
    [2, 0, 8, 3, 'Tidak'],
    [3, 0, 24, 3, 'Tidak'],
    [3, 1, 21, 3, 'Tidak'],
    [4, 5, 40, 4, 'Lolos'],
    [2, 2, 23, 3, 'Tidak'],
    [3, 1, 19, 3, 'Tidak'],
    [4, 0, 12, 2, 'Tidak'],
    [2, 0, 17, 4, 'Tidak'],
    [2, 2, 23, 4, 'Tidak'],
    [2, 0, 14, 2, 'Tidak'],
    [2, 0, 10, 3, 'Tidak'],
    [4, 5, 40, 4, 'Lolos'],
    [4, 1, 27, 4, 'Tidak'],
    [3, 3, 20, 3, 'Tidak'],
    [4, 0, 18, 4, 'Tidak'],
    [2, 1, 17, 3, 'Tidak'],
    [3, 6, 25, 5, 'Tidak'],
    [2, 4, 32, 2, 'Tidak'],
    [2, 0, 13, 3, 'Tidak'],
    [2, 0, 20, 3, 'Tidak'],
    [3, 5, 45, 4, 'Lolos'],
    [4, 1, 27, 4, 'Tidak'],
    [3, 0, 23, 4, 'Tidak'],
    [3, 0, 27, 4, 'Tidak'],
    [3, 1, 37, 3, 'Tidak'],
    [3, 2, 25, 4, 'Tidak'],
    [2, 0, 21, 2, 'Tidak'],
    [4, 0, 28, 3, 'Tidak'],
    [2, 1, 41, 3, 'Tidak'],
    [3, 1, 37, 4, 'Tidak'],
    [3, 0, 23, 4, 'Tidak'],
    [2, 1, 27, 4, 'Tidak'],
    [3, 1, 19, 2, 'Tidak'],
    [4, 0, 27, 4, 'Tidak'],
    [4, 7, 45, 4, 'Lolos'],
    [3, 2, 25, 4, 'Tidak'],
    [3, 0, 21, 3, 'Tidak'],
    [2, 0, 28, 2, 'Tidak'],
    [2, 2, 24, 2, 'Tidak'],
    [3, 0, 13, 3, 'Tidak'],
    [3, 6, 30, 4, 'Lolos'],
    [2, 5, 25, 3, 'Lolos'],
    [4, 9, 42, 5, 'Lolos'],
    [3, 7, 38, 4, 'Lolos'],
    [4, 8, 40, 5, 'Lolos'],
    [2, 5, 28, 3, 'Lolos'],
    [3, 6, 35, 4, 'Lolos'],
    [4, 7, 42, 5, 'Lolos'],
    [3, 6, 30, 4, 'Lolos'],
    [5, 10, 50, 5, 'Lolos']

]

# Membuat DataFrame dari data
columns = ['umur', 'fisik', 'prestasi', 'teknik', 'hasil']
df = pd.DataFrame(data, columns=columns)

# Memisahkan fitur dan label
X = df.drop('hasil', axis=1)
y = df['hasil']

# Membagi data menjadi set pelatihan dan set pengujian
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat model Decision Tree (C4.5)
model = DecisionTreeClassifier()

# Melatih model
model.fit(X_train, y_train)

# Menguji model
y_pred = model.predict(X_test)

# Mengevaluasi performa model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

@app.route('/klasifikasi', methods=['POST'])
def klasifikasi_penyakit():
    try:
        # Get features from the request JSON
        data = request.json
        features = data['features']

        print(f"Received features: {features}")

        # Convert features to a DataFrame
        features_df = pd.DataFrame([features], columns=X.columns)

        print("Features DataFrame:")
        print(features_df)

        # Make a prediction using the trained Decision Tree model
        predicted_class = model.predict(features_df)[0]

        print(f"Predicted class: {predicted_class}")

        # Get the probability of the predicted class
        probability = model.predict_proba(features_df)[0]
        success_percentage = max(probability) * 100

        print(f"Prediction probabilities: {probability}")
        print(f"Success percentage: {success_percentage}%")

        # You can add more information or processing here if needed

        return jsonify({'hasil_klasifikasi': predicted_class, 'persentase': success_percentage})

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)