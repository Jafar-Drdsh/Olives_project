import pandas as pd
import pydotplus
from IPython.display import Image
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

candidates = pd.read_excel(r'DT_BuyComputer.xlsx')
df = pd.DataFrame(candidates)
print(df)

X = df[['age', 'income','student','credit_rating']]
y = df['buysComputer']
print(' ')

one_hot_data = pd.get_dummies(X)

clf = DecisionTreeClassifier()
clf_train =clf.fit(one_hot_data, df['buysComputer'])
print(' ')

print(list(one_hot_data.columns.values))

print(' ')

prediction1 = clf.predict([[1, 0, 0, 1, 0, 0, 1, 0, 0, 1]])
print('Predicted Result1 using Decision Tree Classifier: ', prediction1)
print(' ')

prediction2 = clf.predict([[0, 0, 1, 0, 1, 0, 1, 0, 1, 0]])
print('Predicted Result2 using Decision Tree Classifier: ', prediction2)
print(' ')
print(' ')

dot_data = tree.export_graphviz(clf_train, out_file=None,feature_names=list(one_hot_data.columns.values),class_names=['Not_Buy', 'Buy'], rounded=True,filled=True)
graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())
graph.write_png("buyComp.png")


