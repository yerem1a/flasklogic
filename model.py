def split_data(data, split_ratio=0.7):
    split_idx = int(len(data) * split_ratio)
    return data[:split_idx], data[split_idx:]

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


# Bagi data menjadi data latih (training data) dan data uji (testing data)
train_data, test_data = split_data(data_dummy)

# Hitung probabilitas kelas dan gejala
def calculate_class_probabilities(data):
    class_counts = {}
    for item in data:
        if item[1] in class_counts:
            class_counts[item[1]] += 1
        else:
            class_counts[item[1]] = 1
    
    total_count = len(data)
    
    class_probabilities = {k: v / total_count for k, v in class_counts.items()}
    
    return class_probabilities

def calculate_feature_probabilities(data):
    feature_counts = {}
    for item in data:
        for feature in item[0]:
            if feature in feature_counts:
                feature_counts[feature] += 1
            else:
                feature_counts[feature] = 1
    
    total_count = len(data)
    
    feature_probabilities = {k: v / total_count for k, v in feature_counts.items()}
    
    return feature_probabilities

def naive_bayes_classify(item, class_probabilities, feature_probabilities):
    probabilities = {k: class_probabilities[k] for k in class_probabilities}
    for feature in item:
        if feature in feature_probabilities:
            for k in probabilities:
                probabilities[k] *= feature_probabilities[feature]
    
    return max(probabilities, key=probabilities.get)

class_probabilities = calculate_class_probabilities(train_data)
feature_probabilities = calculate_feature_probabilities(train_data)

correct_count = 0
for item in test_data:
    predicted_class = naive_bayes_classify(item[0], class_probabilities, feature_probabilities)
    if predicted_class == item[1]:
        correct_count += 1

accuracy = correct_count / len(test_data)
print(f"Akurasi: {accuracy * 100:.2f}%")
