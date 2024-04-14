import numpy as npimport pandas as pdfrom collections import defaultdictfrom sklearn.model_selection import train_test_splitfrom sklearn.linear_model import LogisticRegressionfrom sklearn.metrics import accuracy_scorewith open('AI_2qubits_training_data.txt', 'r') as file:    data = file.readlines()    type_1=data[:2000]type_2=data[2001:4000]type_3=data[4001:6000]delimiter = ' 'first_column_1 = [row.split(delimiter)[0] for row in type_1]first_column_2 = [row.split(delimiter)[0] for row in type_2]first_column_3 = [row.split(delimiter)[0] for row in type_3]def average_frequency(first_column):    frequencies_per_row = []    for row in first_column:        frequency_1 = 0        frequency_0 = 0        for bit in row:            if bit == '1':                frequency_1 += 1            elif bit == '0':                frequency_0 += 1        total_bits = len(row)    distribution = {'1': frequency_1 / total_bits, '0': frequency_0 / total_bits}    frequencies_per_row.append(distribution)            total_frequency_1 = 0    total_frequency_0 = 0    num_rows = len(frequencies_per_row)# Calculate the total frequency of 1s and 0s across all rows    for distribution in frequencies_per_row:        total_frequency_1 += distribution['1']        total_frequency_0 += distribution['0']# Calculate the average frequency distribution across all rows    average_distribution = {    '1': (total_frequency_1 / num_rows),    '0': (total_frequency_0 / num_rows)    }        return(average_distribution)                                   print("Average Distribution of Type 1:",average_frequency(first_column_1))print("Average Distribution of Type 2:",average_frequency(first_column_2))print("Average Distribution of Type 3:",average_frequency(first_column_3))def markov_chain(first_column):    transition_pairs = ['01', '10', '00', '11']    #transition_matrix = {pair: [0]*4 for pair in transition_pairs}    rates=[0,0,0,0]    for row in first_column:        for i in range(len(row)-1):            transition=row[i:i+2]            if transition in transition_pairs:                #transition_matrix[transition][transition_pairs.index(transition)] += 1                rates[transition_pairs.index(transition)]+=1    return rates        print(markov_chain(first_column_1))print(markov_chain(first_column_2))print(markov_chain(first_column_3))from sklearn.utils import shuffleX=np.array([[int(bit) for bit in row[0]] for row in data])y=np.array([int(row[1]) for row in data])X_shuffled, y_shuffled = shuffle(X, y)#Shuffled in order to prevent learning bias created by organized data.X_train, X_test, y_train, y_test = train_test_split(X_shuffled, y_shuffled, test_size=0.3, random_state=42)classifier = LogisticRegression()classifier.fit(X_train, y_train)y_pred = classifier.predict(X_test)accuracy = accuracy_score(y_test, y_pred)print("Accuracy:", accuracy)'''print("Predicted Results:")for i in range(10):    print("Actual:", y_test[i], "Predicted:", y_pred[i])      import tensorflow as tffrom tensorflow import kerasfrom tensorflow.keras import layersmodel = tf.keras.Sequential([    layers.Dense(64, activation='relu', input_shape=(50,)),    layers.Dense(32, activation='relu'),    layers.Dense(1, activation='sigmoid')])X_train, X_temp, y_train, y_temp = train_test_split(X_shuffled, y_shuffled, test_size=0.2, random_state=42)X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_val, y_val))test_loss, test_acc = model.evaluate(X_test, y_test)print('Test accuracy:', test_acc)from statsmodels.tsa.arima.model import ARIMAtime_series_data['timestamp_column'] = data.to_datetime(time_series_data['timestamp_column'])time_series_data.set_index('timestamp_column', inplace=True)# Visualize the time series datatime_series_data['value_column'].plot()plt.xlabel('Timestamp')plt.ylabel('Value')plt.title('Time Series Data')plt.show()# Fit an ARIMA model to the time series datamodel = ARIMA(time_series_data['value_column'], order=(1, 1, 1))  # Example order (p, d, q)results = model.fit()# Print the model summaryprint(results.summary())# Make forecasts using the fitted modelforecast = results.forecast(steps=10)  # Example forecast for the next 10 time stepsprint("Forecast:", forecast)'''import matplotlib.pyplot as pltunique_values, counts = np.unique(data, return_counts=True)probabilities = counts / len(data)entropy = -np.sum(probabilities * np.log2(probabilities))print("Entropy:", entropy)'''from sklearn.cluster import KMeansfrom sklearn.metrics import silhouette_scoreX=np.array([[int(bit) for bit in row[0]] for row in data])silhouette_scores=[]min_clusters=2max_clusters=10for n_clusters in range(min_clusters,max_clusters+1):    kmeans=KMeans(n_clusters=n_clusters,random_state=40)    kmeans.fit(X)    cluster_labels=kmeans.labels_    centroids=kmeans.cluster_centers_    silhouette_avg=silhouette_score(X,cluster_labels)    silhouette_scores.append(silhouette_avg)    print(n_clusters,silhouette_avg)  plt.plot(range(min_clusters,max_clusters+1),silhouette_scores,marker='o')plt.xlabel('num clusters')plt.ylabel('silhouette')plt.title('silhouette vs number')plt.grid(True)plt.show()kmeans=KMeans(n_clusters=3,random_state=40)kmeans.fit(X)cluster_labels=kmeans.labels_centroids=kmeans.cluster_centers_plt.scatter(X,[0]*len(X), c=cluster_labels, cmap='viridis',alpha=0.5)plt.scatter(centroids,[0]*len(centroids),marker='x',c='red',label="Cluster Centers")plt.xlabel('50-bit Binaries')plt.ylabel('Cluster')plt.title('K-means Clustering')plt.legend()plt.show()def binaryToDecimal(binary):    decimal,i=0,0    while(binary!=0):        dec=binary%10        decimal=decimal+dec*pow(2,i)        binary=binary//10        i+=1    print(decimal)    binaryToDecimal(100100)binary_strings=data.iloc[:,0].valuesbinary_integers=[int(binary,2) for binary in binary_strings]new_df=pd.DataFrame({'Binary Integers':binary_integers})new_df.to_csv('new_dataset.txt',sep=' ', index=False,header=False)print(new_df.head())'''