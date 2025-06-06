import streamlit as st
import pandas as pd
import joblib 

model = joblib.load('financial.pkl')


st.title('FINANCIAL INCLUSION DATASET')

st.header('Input Features')
col1,col2 = st.columns(2)
with col1:
    country = st.selectbox('country',['Kenya', 'Rwanda', 'Tanzania', 'Uganda'])
with col2:
    year = st.selectbox('year',[2016,2017,2018])
with col1:
    location_type = st.selectbox('location_type',['Rural','Urban'])
with col2:
    cellphone_access = st.selectbox('cellphone_access',['No','Yes'])
with col1:
    household_size = st.number_input('household_size',min_value=1,max_value=21,value=5,step=3)
with col2:
    age_of_respondent = st.number_input('Enter your age',min_value=15,max_value=100,value=18,step=20)
with col1:
    gender_of_respondent = st.selectbox('Select Gender:', ['Female', 'Male'])
with col2:
    relationship_with_head = st.selectbox('relationship_with_head',['Child','Head of Household','Other non-relatives','Other relative',
 'Parent','Spouse'])
with col1:
    marital_status = st.selectbox('marital_status',['Divorced/Seperated','Dont know','Married/Living together',
 'Single/Never Married' ,'Widowed'])
with col2:
    education_level = st.selectbox('education_level',['Secondary education', 'No formal education',
       'Vocational/Specialised training', 'Primary education',
       'Tertiary education', 'Other/Dont know/RTA'])
job_type = st.selectbox('job_type',['Self employed', 'Government Dependent',
       'Formally employed Private', 'Informally employed',
       'Formally employed Government', 'Farming and Fishing',
       'Remittance Dependent', 'Other Income',
       'Dont Know/Refuse to answer', 'No Income'])

input_feat = {
    'country' : country,
    'year' : year,
    'location_type' : location_type,
    'cellphone_access' : cellphone_access,
    'household_size' : household_size,
    'age_of_respondent' : age_of_respondent,
    'gender_of_respondent' : gender_of_respondent,
    'relationship_with_head' : relationship_with_head,
    'marital_status' : marital_status,
    'education_level' : education_level,
    'job_type' : job_type
}

input_df = pd.DataFrame([input_feat])

for col in ['gender_of_respondent', 'location_type', 'cellphone_access', 'relationship_with_head', 'marital_status']:
    le = joblib.load(f'le_{col}.pkl')
    input_df[col] = le.transform(input_df[col])


submitted = st.button('Predict')

if submitted:
    prediction = model.predict(input_df)
    if prediction == 'NO':
        st.error('Does Not Have A Bank Account')
    else:
        st.success('Has A Bank Account')
