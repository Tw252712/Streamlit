import streamlit as st
import pandas as pd
import joblib 


model = joblib.load('expresso_churn.pkl')

st.title('EXPRESSO CHURN ANALYSIS')

top_packages = [
    'All-net 500F=2000F;5d','Data:200F=Unlimited,24H','Data:1000F=2GB,30d','MIXT:500F= 2500F on net _2500F off net;2d','Mixt 250F=Unlimited_call24H','Twter_U2opia_Weekly','Data:50F=30MB_24H',  
    'Data:3000F=10GB,30d','Data:490F=1GB,7d','Data: 100 F=40MB,24H','VAS(IVR_Radio_Daily)','Data: 200 F=100MB,24H','All-net 600F= 3000F ;5d','On-net 200F=60mn;1d',  
    'On net 200F=Unlimited _call24H','All-net 500F =2000F_AllNet_Unlimited','IVR Echat_Daily_50F','On-net 500=4000,10d','On-net 1000F=10MilF;10d',  
    'MIXT: 200mnoff net _unl on net _5Go;30d','All-net 300=600;2d','Jokko_Daily','On-net 500F_FNF;3d','Data:500F=2GB,24H','Data:DailyCycle_Pilot_1.5GB','Twter_U2opia_Monthly',  
    'Data:1000F=5GB,7d','MIXT: 590F=02H_On-net_200SMS_200 Mo;24h','Twter_U2opia_Daily','Data:300F=100MB,2d','Data:700F=1.5GB,7d','Pilot_Youth4_490','All-net 1000=5000;5d', 
    'YMGX 100=1 hour FNF, 24H/1 month,200=Unlimited1Day','New_YAKALMA_4_ALL','On net 200F= 3000F_10Mo ;24H','All-net 1000F=(3000F On+3000F Off);5d','SUPERMAGIK_1000',  
    'MROMO_TIMWES_OneDAY','Pilot_Youth1_290','Jokko_promo','Data:150F=SPPackage1,24H','Data:1500F=SPPackage1,30d','SUPERMAGIK_5000',  
    'MIXT: 390F=04HOn-net_400SMS_400 Mo;4h','Data:1500F=3GB,30D,Facebook_MIX_2D','All-net 500F=1250F_AllNet_1250_Onnet;48h','DataPack_Incoming','FIFA_TS_daily',  
    'Data: 490F=Night,00H-08H','On-net 300F=1800F;3d','Internat: 1000F_Zone_1;24H','EVC_500=2000F','Yewouleen_PKG,Data:700F=SPPackage1,7d',  
    'All-net 5000= 20000off+20000on;30d','MROMO_TIMWES_RENEW','CVM_on-net bundle 500=5000','Jokko_Monthly,On-net 2000f_One_Month_100H; 30d',  
    'MIXT:1000F=4250 Off net _ 4250F On net _100Mo; 5d','MIXT: 5000F=80Konnet_20Koffnet_250Mo;30d','Mixt : 500F=2500Fonnet_2500Foffnet ;5d','Data:30Go_V 30_Days','MIXT: 500F=75(SMS, ONNET, Mo)_1000FAllNet;24h',  
    'MIXT: 4900F= 10H on net_1,5Go ;30d','FNF2 ( JAPPANTE)','Incoming_Bonus_woma','TelmunCRBT_daily','VAS(IVR_Radio_Weekly)','Jokko_Weekly','1000=Unlimited7Day', 
    'All-net 500F=4000F ; 5d','VAS(IVR_Radio_Monthly)','IVR Echat_Weekly_200F','Internat: 2000F_Zone_2;24H','EVC_100Mo','Data: 200F=1GB,24H',  
    '200F=10mnOnNetValid1H','MIXT:10000F=10hAllnet_3Go_1h_Zone3;30d','EVC_JOKKO30','500=Unlimited3Day','CVM_200f=400MB','CVM_On-net 400f=2200F',305155009,'EVC_700Mo',  
    'APANews_weekly','IVR Echat_Monthly_500F','EVC_4900=12000F','Internat: 1000F_Zone_3;24h','FNF_Youth_ESN','EVC_1Go','pack_chinguitel_24h', 
    'CVM_100F_unlimited','1500=Unlimited7Day','CVM_100f=200 MB','NEW_CLIR_PERMANENT_LIBERTE_MOBILE','EVC_Jokko_Weekly','CVM_On-net 1300f=12500' ,0
    ]


st.header('Input Features')
col1,col2 = st.columns(2)
with col1:
    region = st.selectbox('REGION',['DAKAR','KAFFRINE','THIES','KAOLACK','TAMBACOUNDA','DIOURBEL','MATAM','LOUGA','FATICK','SAINT-LOUIS','KOLDA','ZIGUINCHOR','SEDHIOU','KEDOUGOU'])
with col2:
    tenure = st.selectbox('TENURE',['K > 24 month', 'I 18-21 month', 'J 21-24 month', 'E 6-9 month','H 15-18 month', 'F 9-12 month', 'G 12-15 month', 'D 3-6 month'])
with col1:
    montant = st.number_input('Enter your MONTANT',min_value=50.0,max_value=65000.0,value=1000.0,step=500.0)
with col2:
    frequence_rech = st.number_input('Enter your FREQUENCE_RECH',min_value=1.0,max_value=60.0,value=30.0,step=20.0)
with col1:
    arpu_segement = st.number_input('Enter your ARPU_SEGMENT',min_value=4.0,max_value=10000.0,value=1000.0,step=1000.0)
with col2:
    frequence = st.number_input('Enter your FREQUENCE',min_value=1.0,max_value=85.0,value=50.0,step=10.0)
with col1:
    data_volume = st.number_input('Enter your DATA_VOLUME',min_value=0.0,max_value=58984.0,value=1000.0,step=1000.0)
with col2:
    on_net = st.number_input('Enter your ON_NET',min_value=0.0,max_value=7251.0,value=1000.0,step=1000.0)
with col1:
    orange = st.number_input('Enter your ORANGE',min_value=0.0,max_value=1117.0,value=200.0,step=100.0)
with col2:
    mrg = st.selectbox('MRG',['NO','YES'])
with col1:
    regularity = st.number_input('Enter your REGULARITY',min_value=1.0,max_value=62.0,value=20.0,step=5.0)
selected_bundle = st.selectbox("Click or select a bundle offer:", top_packages)
st.warning('Note : Please refer to the next tab for the TOP PACKAGES')
top_pack = st.text_area("Selected Top Pack", value=selected_bundle, height=100)
with col2:
    freq_top_pack = st.number_input('Enter your FREQ_TOP_PACK',min_value=1.0,max_value=134.0,value=30.0,step=10.0)

inputs_features ={
'REGION' : region,
'TENURE' : tenure,
'MONTANT' : montant,
'FREQUENCE_RECH' : frequence_rech,
'ARPU_SEGMENT' : arpu_segement,
'FREQUENCE' : frequence,
'DATA_VOLUME' : data_volume,
'ON_NET' : on_net,
'ORANGE' : orange,
'MRG' : mrg,
'REGULARITY' : regularity,
'TOP_PACK' : top_pack,
'FREQ_TOP_PACK' : freq_top_pack
}

input_df = pd.DataFrame([inputs_features])

submitted = st.button('predict')

if submitted:
    prediction = model.predict(input_df)
    if prediction == 0:
        st.success(f'Has A Churn Probability of {prediction}')
    else:
        st.success(f'Has A Churn Probablity of {prediction}')

