import numpy as np
from scipy import spatial

'''
Author: Antonio Lang
Date: 18 October 2022
'''

def KNN_test(X_train,Y_train,X_test,Y_test,K):
    num_correct = 0
    distances = spatial.distance.cdist(X_test, X_train) # distances between all samples
    for i, point_distances in enumerate(distances):
        label_dist = []
        for j, distance in enumerate(point_distances):
            label_dist.append((distance, Y_train[j])) # adds tuple of the point's distance to corresponding training label
        sorted_dist = sorted(label_dist, key=lambda l:l[0], reverse=False) # sorts in ascending distance
        if Y_test[i] == get_prediction(sorted_dist, K): num_correct += 1
    return num_correct / len(X_train) # accuracy of KNN

def choose_K(X_train,Y_train,X_val,Y_val):
    best_acc = 0
    best_k = 1
    for i in range(1, len(X_train)):
        acc = KNN_test(X_train, Y_train, X_val, Y_val, i)
        if acc > best_acc: best_acc = acc; best_k = i
    return best_k

def get_prediction(sorted_distances, K):
    # sums and returns the majority label
    label_sum = 0
    for i in range(K):
        label_sum += sorted_distances[i][1]
    return 1 if label_sum > 0 else -1