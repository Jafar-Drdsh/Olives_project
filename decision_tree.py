# Step 1: Load Python Packages
import pandas as pd
# pandas is a Python library that provides fast, flexible, and expressive data structures. the two primary
import pydotplus
# Load Libraries to Visualize Decision Tree
from IPython.display import Image
from sklearn import tree
# data structures of pandas, Series (one-dimensional) and DataFrame (two-dimensional). pandas is well suited for inserting
# and deleting columns from DataFrame, for easy handling of missing data
from sklearn.tree import DecisionTreeClassifier
# Import Decision Tree Classifier


# Step 2: Pre-Process The Data
candidates = pd.read_excel (r'DT_BuyComputer.xlsx')
df = pd.DataFrame(candidates,columns= ['age', 'income','student','credit_rating','buysComputer'])
print(df)

# Step 3: Subset The Data: (Our new dataset should only have the variables that we will be using to build the model)

X = df[['age', 'income','student','credit_rating']]
y = df['buysComputer']

# Step 4: Split The Data Into Train And Test Sets

print(' ')

# Convert categorical variable into dummy/indicator variables or (binary vairbles) essentialy 1's and 0's

one_hot_data = pd.get_dummies(X)


#Step 5: Build A DecisionTreeClassifier (Create Decision Tree classifer object)
# the default criterion in DecisionTreeClassifier is "gini", and we can use another criterion as in DecisionTreeClassifier(criterion=’gini’,...) see the link:
# https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier
# see the 6.3.2 Attribute Selection Measures section in Elsevier DM E-book pages 296 to 306

clf = DecisionTreeClassifier()
# Train Decision Tree Classifer
clf_train =clf.fit(one_hot_data, df['buysComputer'])


# Step 6: Predict: we will not measure the accuracy, because we have not subset the data into train and test.
# Step 7: Predictions for new data using Decision Tree
print(' ')
print(list(one_hot_data.columns.values))
print(' ')
# predict if it will paly or not for the following case:
prediction1 = clf.predict([[1, 0, 0, 1, 0, 0, 1, 0, 0, 1]])
print('Predicted Result1 using Decision Tree Classifier: ', prediction1)
print(' ')
prediction2 = clf.predict([[0, 0, 1, 0, 1, 0, 1, 0, 1, 0]])
print('Predicted Result2 using Decision Tree Classifier: ', prediction2)
print(' ')
print(' ')


# step 8: the draw tree ######
# Export/Print a decision tree in DOT format. DOT format: format as rules if then ... try to print next command
dot_data = tree.export_graphviz(clf_train, out_file=None, feature_names=list(one_hot_data.columns.values), class_names=['Not_Buy', 'Buy'], rounded=True, filled=True)
# rounded=True هذا يعني يجعل شكل النود مستطيل دائري وليس مربع , filled=True هذا يعني يجب ان يملأ النودات في الشجرة بالالوان
#Gini decides which attribute/feature should be placed at the root node, which features will act as internal nodes or leaf nodes

# #Create Graph from DOT data
graph = pydotplus.graph_from_dot_data(dot_data)

# Show graph
Image(graph.create_png())

# the resulted tree/files .png or .pdf ,, it will be saved in the same project folder
# C:\Users\Hadi\PycharmProjects\DT_PlayTenis_Ex12
# Create PNG
# if dot_data in ( graph = pydotplus.graph_from_dot_data(dot_data) ) is dummied the function: graph.write_png() will be released using GVEdit framework

graph.write_png("buyComp.png")
# Create PDF
# #graph.write_pdf("buyComp.pdf")
# note: check the youtube link for the example: https://www.youtube.com/watch?v=bT-43kgYI3o&feature=youtu.be
