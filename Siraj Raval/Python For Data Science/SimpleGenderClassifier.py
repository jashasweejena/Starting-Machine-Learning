from sklearn import tree

#[height, weight, age]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37],
	 [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40],
	 [171, 75, 42], [181, 85, 32]]

Y = ['male', 'female', 'female', 'female', 'male', 'male',
	 'male', 'female', 'male', 'male']

clf = tree.DecisionTreeClassifier();

clf = clf.fit(X, Y);

prediction = clf.predict([[111, 80, 43], [77, 52, 88]])

print(prediction)