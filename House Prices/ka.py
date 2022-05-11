import pandas as pd 
from sklearn.tree import DecisionTreeRegressor

test = pd.read_csv("test.csv",sep=',')#leitura arquvo CVS com os dados imporados
train = pd.read_csv("train.csv",sep=',')
print(train.columns.tolist())

y = train['SalePrice']

feature_names = ['LotFrontage'
                ,'LotArea'
                ,'OverallQual'
                ,'OverallCond'
                ,'YearBuilt'
                ,'YearRemodAdd'
                ,'MasVnrArea'
                ,'BsmtFinSF1'
                ,'BsmtUnfSF'
                ,'TotalBsmtSF'
                ,'BsmtFullBath'
                ,'TotRmsAbvGrd'
                ,'Fireplaces'
                ,'GarageCars'
                ,'WoodDeckSF'
                ,'PoolArea']

x = train[feature_names]

model = DecisionTreeRegressor(random_state=1)

# Fit the model
model.fit(x,y)

predictions = odel.predict(x)
print(predictions)