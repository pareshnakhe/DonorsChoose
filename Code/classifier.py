import pandas as pd
import numpy as np
import matplotlib
import lightgbm as lgb
import xgboost as xgb
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import log_loss, mean_squared_error
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import cross_val_score

data = pd.read_csv('clean_classfn_data.csv')
X = data.drop(['percent_full'], axis=1)
y = data['percent_full']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=43)


clf = LogisticRegression(penalty='l1', tol=0.01).fit(X_train, y_train)
scores = cross_val_score(clf, X, y, cv=5)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
# print 'Prediction Accuracy', clf.score(X_test, y_test)*100.0, 'Prediction log-loss', log_loss(y_test, clf.predict_proba(X_test))

# boosting_type = ['gbdt', 'goss']
for l_rate in np.arange(0.20, 0.250, 0.05):
    gbm = lgb.LGBMClassifier(learning_rate=l_rate, num_leaves=51,  n_estimators=100, silent=True)
    gbm.fit(X_train, y_train, eval_set=[(X_test, y_test)], early_stopping_rounds=5, verbose=False)
    scores = cross_val_score(gbm, X, y, cv=5)
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    # print 'Prediction Accuracy', gbm.score(X_test, y_test), 'Prediction log-loss', log_loss(y_test, gbm.predict_proba(X_test))


adaBoost = AdaBoostClassifier()
adaBoost.fit(X_train, y_train)
scores = cross_val_score(adaBoost, X, y, cv=5)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
# print 'Prediction Accuracy', adaBoost.score(X_test, y_test), 'Prediction log-loss', log_loss(y_test, adaBoost.predict_proba(X_test))

# xg_train = xgb.DMatrix(X_train, label=y_train)
# xg_test = xgb.DMatrix(X_test, label=y_test)
#
# param = {'max_depth': 15, 'eta': 1, 'silent': 1, 'objective': 'binary:logistic' }
# num_round = 20
# bst = xgb.train(param, xg_train, num_round)
# preds = bst.predict(xg_test)
# print log_loss(y_test, preds)