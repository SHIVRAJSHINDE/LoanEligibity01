from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder,OrdinalEncoder
from sklearn.preprocessing import MinMaxScaler,StandardScaler


class data_TransformationClass():

    def DropColumns(self,listOfColumns,df):
        df.drop(listOfColumns,axis=1,inplace=True)
        return df


    def ReplaceWithCorrectValue(self,colName,valuesToReplace,df):
        for key,value in valuesToReplace.items():
            df[colName].replace(key,value,inplace=True)
        return df



    def replaceWithMode(self,columnName,df):
        for i in columnName:
            modeSelf_Employed = df[i].mode()[0]
            df[i].fillna(modeSelf_Employed,inplace=True)
        return df 


    def replaceWithMean(self,columnName1,df):
        for i in columnName1:
            meanOfColumn = df[i].mean()
            df[i].fillna(meanOfColumn,inplace=True)
        return df 


    def removeOutlier(self,colName,df,LowerQuantile,HigherQuantile):

        q1 = df[colName].quantile(LowerQuantile)
        q3 = df[colName].quantile(HigherQuantile)

        IQR = q3-q1

        lowerLimit = q1-1.5*IQR 
        upperLimit = q3+1.5*IQR

        print(q1)
        print(q3)
        print(IQR)
        print(lowerLimit)
        print(upperLimit)
        
        higherOutlier = df[df[colName]>upperLimit]
        df = df.drop(higherOutlier.index,axis=0)

        return df

    def dataReadingAndSplitting(self,final_df):

        y = final_df.loc[:,'Loan_Status']
        X = final_df.drop(['Loan_Status'],axis=1)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 355)
        return (X_train, X_test, y_train, y_test)

   
    def dataTransformation(self):
        oneHotColumns = ['Self_Employed', 'Geography', 'Property_Area', 'Married', 'Gender']
        trf1 = ColumnTransformer([
            ('OneHot', OneHotEncoder(drop='first', handle_unknown='error'), oneHotColumns)], remainder='passthrough')

        trf2 = ColumnTransformer([
            ('Ordinal1', OrdinalEncoder(categories=[['VP', 'AVP', 'Senior Manager', 'Manager', 'Executive']]), [8])]
            , remainder='passthrough')
        trf3 = ColumnTransformer([
            ('Ordinal2', OrdinalEncoder(categories=[['Graduate', 'Not Graduate']]), [9])]
            , remainder='passthrough')

        trf4 = ColumnTransformer([
            ('scale', StandardScaler(), slice(0, 25))
        ])


        pipe = make_pipeline(trf1,trf2,trf3,trf4)
        return pipe
