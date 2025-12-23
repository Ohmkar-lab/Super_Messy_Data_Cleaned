import pandas as pd
import numpy as np
df=pd.read_csv('super_messy_ecommerce_test.csv')

#Understanding the data
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())

#Cleaning the data set 

df=df.drop_duplicates()
columns=['Customer Name', 
'Age',               
'Gender',            
'City',              
'Order Amount',      
'Payment Method',    
'Order Date',        
'Delivery Days']

df.columns=df.columns.str.upper().str.replace(' ','_')
df= df.rename(columns={'CUSTOMER__NAME': 'CUSTOMER_NAME'})

df['ORDER_ID']=df['ORDER_ID'].replace(r'^\s*$',np.nan,regex=True)
df['ORDER_ID']=pd.to_numeric(df['ORDER_ID'],errors='coerce')
df =df.dropna(subset=['ORDER_ID'])
df['ORDER_ID']=df['ORDER_ID'].astype(int)

df['CUSTOMER_NAME']=df['CUSTOMER_NAME'].replace(r'^\s*$',np.nan,regex=True)
df['CUSTOMER_NAME']=df['CUSTOMER_NAME'].str.lower()
df['CUSTOMER_NAME']=df['CUSTOMER_NAME'].fillna('Unknown')

df['AGE']=df['AGE']=df['AGE'].replace(r'^\s*$',np.nan,regex=True)
df['AGE']=pd.to_numeric(df['AGE'],errors='coerce')
df['AGE']=df['AGE'].fillna(df['AGE'].median())
df['AGE']=df['AGE'].abs()
df['AGE']=df['AGE'].astype(int)

df['GENDER']=df['GENDER'].str.strip().str.lower()

mapping={
    'male':'Male',
    'm':'Male',
    'female':'Female',
    'f':'Female',
    'unknown':'Unspecified'
}

df['GENDER']=df['GENDER'].map(mapping).fillna('Unspecified')

df['CITY']=df['CITY'].fillna('Unspecified')
df.loc[df['CITY'].str.isnumeric(), 'CITY'] = 'Unspecified'
df['CITY']=df['CITY'].str.lower()

df['ORDER_AMOUNT']=pd.to_numeric(df['ORDER_AMOUNT'],errors='coerce')
df['ORDER_AMOUNT']=df['ORDER_AMOUNT'].abs()
Median_amt=df['ORDER_AMOUNT'].median(skipna=True)
df['ORDER_AMOUNT']=df['ORDER_AMOUNT'].fillna(Median_amt)

# print(df['PAYMENT_METHOD'].value_counts())
df['PAYMENT_METHOD']=df['PAYMENT_METHOD'].str.strip().str.lower()

Mapping2={
    'cash':'Cash',
    'net_banking':'Net_Banking',
    'net banking':'Net_Banking',
    'upi':'Upi',
    'card':'Card'
}

df['PAYMENT_METHOD']=df['PAYMENT_METHOD'].map(Mapping2).fillna('Unspecified')

df['ORDER_DATE'] = df['ORDER_DATE'].astype(str).str.strip()
df['ORDER_DATE'] = df['ORDER_DATE'].replace(['', 'NA', 'N/A', 'nan'], np.nan)
df['ORDER_DATE']=pd.to_datetime(df['ORDER_DATE'],errors='coerce',dayfirst=True,infer_datetime_format=True)
median_date=df['ORDER_DATE'].median(skipna=True)
df['ORDER_DATE']=df['ORDER_DATE'].fillna(median_date)

df['DELIVERY_DAYS']=pd.to_numeric(df['DELIVERY_DAYS'],errors='coerce')
df['DELIVERY_DAYS']=df['DELIVERY_DAYS'].abs() 
Mean_days=df['DELIVERY_DAYS'].mean()
df['DELIVERY_DAYS']=df['DELIVERY_DAYS'].fillna(Mean_days).astype(int)

#outliers and adding columns

df=df[(df['AGE']>=18)&(df['AGE']<=70)]

mean_amt=df['ORDER_AMOUNT'].mean()
upper1=mean_amt+3*Median_amt
lower1=mean_amt-3*Median_amt
df=df[(df['ORDER_AMOUNT']>=lower1)&(df['ORDER_AMOUNT']<=upper1)]

#Adding new columns based on feature engineering

df.insert(loc=9,column='DELIVERY_SPEED',value=pd.qcut(df['DELIVERY_DAYS'],q=2,labels=['slow','fast'],duplicates='drop'))
df.insert(loc=9,column='ORDER_RANGE',value=pd.cut(df['ORDER_AMOUNT'],bins=[0,377,df['ORDER_AMOUNT'].max()],labels=['low','high'],duplicates='drop'))
# print(df.head(5))
#Deriving insights
# print(df['CITY'].value_counts().head(4))
#Top 3 cities are (banglore, new york, delhi)
# print(df['ORDER_AMOUNT'].mean())
#Mean order amount is 377.02
# print(df['DELIVERY_SPEED'].value_counts().head(4))
#Over all the delivery speed is faster 449:139 faster : slower ratio
# print(df['PAYMENT_METHOD'].value_counts().head(4))
#Top most payment method is Net Banking

df=df.reset_index(drop=True)
df.to_csv('Cleaned_Messy_data.csv')
print('Data successfully cleaned - "Cleaned_Messy_data.csv"')

