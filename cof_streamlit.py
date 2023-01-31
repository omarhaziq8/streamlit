import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_excel(r'U:\Users\00148245\Desktop\omar\Digital_Analytics\CASA_ON_FILE\DEC\COF_DEC_22.xlsx')
df_active = pd.read_excel(r'U:\Users\00148245\Desktop\omar\Digital_Analytics\CASA_ON_FILE\DEC\COF_DEC_22.xlsx', "Total Active Tokens")
df_deactive = pd.read_excel(r'U:\Users\00148245\Desktop\omar\Digital_Analytics\CASA_ON_FILE\DEC\COF_DEC_22.xlsx', "Total Deactive Tokens")

st.set_page_config(layout="wide")

merchant_list  = ["GrabPay Malaysia", "Shopee Marketplace", "AliPay (Lazada)", "ShopeePay Wallet", "MBBCOF00000005", "MBBCOF00000006", "MBBCOF00000011"]

df_list=[]
for merchant in merchant_list:
    new = df[df["Merchant"] == merchant]
    df_list.append(new)
df_list_2021 = []
for i in np.arange(0,7):
    new = df_list[i].loc[(df_list[i]['Month-Year'] >= '2021-01-01') & (df_list[i]['Month-Year'] <= '2021-12-01')]
    df_list_2021.append(new)
df_list_2022 = []
for i in np.arange(0,7):
    new = df_list[i].loc[(df_list[i]['Month-Year'] >= '2022-01-01') & (df_list[i]['Month-Year'] <= '2022-12-01')]
    df_list_2022.append(new)


df_active_list=[]
for merchant in merchant_list:
    new = df_active[df_active["Merchant"] == merchant]
    df_active_list.append(new)
df_active_list_2021 = []
for i in np.arange(0,7):
    new = df_active_list[i].loc[(df_active_list[i]['Month-Year'] >= '2021-01-01') & (df_active_list[i]['Month-Year'] <= '2021-12-01')]
    df_active_list_2021.append(new)
df_active_list_2022 = []
for i in np.arange(0,7):
    new = df_active_list[i].loc[(df_active_list[i]['Month-Year'] >= '2022-01-01') & (df_active_list[i]['Month-Year'] <= '2022-12-01')]
    df_active_list_2022.append(new)


df_deactive_list=[]
for merchant in merchant_list:
    new = df_deactive[df_deactive["Merchant"] == merchant]
    df_deactive_list.append(new)
df_deactive_list_2021 = []
for i in np.arange(0,7):
    new = df_deactive_list[i].loc[(df_deactive_list[i]['Month-Year'] >= '2021-01-01') & (df_deactive_list[i]['Month-Year'] <= '2021-12-01')]
    df_deactive_list_2021.append(new)
df_deactive_list_2022 = []
for i in np.arange(0,7):
    new = df_deactive_list[i].loc[(df_deactive_list[i]['Month-Year'] >= '2022-01-01') & (df_deactive_list[i]['Month-Year'] <= '2022-12-01')]
    df_deactive_list_2022.append(new)




#merchants = st.sidebar.multiselect("Merchant Type: ", ['GrabPay Malaysia', 'Shopee Marketplace', 'AliPay (Lazada)', 'ShopeePay Wallet', 'MBBCOF00000005', 'MBBCOF00000006', 'MBBCOF00000011'])
merchants = st.multiselect("Merchant Type: ", ['GrabPay Malaysia', 'Shopee Marketplace', 'AliPay (Lazada)', 'ShopeePay Wallet', 'MBBCOF00000005', 'MBBCOF00000006', 'MBBCOF00000011'])
years = st.selectbox("Year: ", ["2021", "2022"])
service = st.selectbox("Service :", ["Total Payments", "Total Active Tokens", "Total Deactive Tokens"])

st.header("You selected: {}".format(", ".join(merchants)))

for merch in merchants:
    for i in np.arange(0,len(merchant_list)):
        if merch == merchant_list[i] and years == "2022" and service == "Total Payments":
            fig = plt.figure(figsize=(20, 3.5))
            st.subheader(merchant_list[i])
            bar1 = plt.bar(x = df_list_2022[i].loc[(df_list[i]['Month-Year'] >= '2022-01-01') & (df_list_2022[i]['Month-Year'] <= '2022-12-01')]["Month-Year"], height=df_list_2022[i].loc[(df_list_2022[i]['Month-Year'] >= '2022-01-01') & (df_list_2022[i]['Month-Year'] <= '2022-12-01')]["Total Transaction Volume"], width=5.5)
            for rect in bar1:
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width() /2.0, height, f'{height:.0f}', ha='center', va='bottom')
            st.pyplot(fig)

        if merch == merchant_list[i] and years == "2021" and service == "Total Payments":
            fig = plt.figure(figsize=(20, 3.5))
            st.subheader(merchant_list[i])
            bar1 = plt.bar(x = df_list_2021[i].loc[(df_list[i]['Month-Year'] >= '2021-01-01') & (df_list_2021[i]['Month-Year'] <= '2021-12-01')]["Month-Year"], height=df_list_2021[i].loc[(df_list_2021[i]['Month-Year'] >= '2021-01-01') & (df_list_2021[i]['Month-Year'] <= '2021-12-01')]["Total Transaction Volume"], width=5.5)
            for rect in bar1:
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width() /2.0, height, f'{height:.0f}', ha='center', va='bottom')
            st.pyplot(fig)

        if merch == merchant_list[i] and years == "2021" and service == "Total Active Tokens":
            fig = plt.figure(figsize=(20, 3.5))
            st.subheader(merchant_list[i])
            bar1 = plt.bar(x = df_active_list_2021[i].loc[(df_active_list[i]['Month-Year'] >= '2021-01-01') & (df_active_list_2021[i]['Month-Year'] <= '2021-12-01')]["Month-Year"], height=df_active_list_2021[i].loc[(df_active_list_2021[i]['Month-Year'] >= '2021-01-01') & (df_active_list_2021[i]['Month-Year'] <= '2021-12-01')]["No. of Active Tokenised Accounts for the Month"], width=5.5)
            for rect in bar1:
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width() /2.0, height, f'{height:.0f}', ha='center', va='bottom')
            st.pyplot(fig)

        if merch == merchant_list[i] and years == "2022" and service == "Total Active Tokens":
            fig = plt.figure(figsize=(20, 3.5))
            st.subheader(merchant_list[i])
            bar1 = plt.bar(x = df_active_list_2022[i].loc[(df_active_list[i]['Month-Year'] >= '2022-01-01') & (df_active_list_2022[i]['Month-Year'] <= '2022-12-01')]["Month-Year"], height=df_active_list_2022[i].loc[(df_active_list_2022[i]['Month-Year'] >= '2022-01-01') & (df_active_list_2022[i]['Month-Year'] <= '2022-12-01')]["No. of Active Tokenised Accounts for the Month"], width=5.5)
            for rect in bar1:
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width() /2.0, height, f'{height:.0f}', ha='center', va='bottom')
            st.pyplot(fig)

        if merch == merchant_list[i] and years == "2021" and service == "Total Deactive Tokens": 
            fig = plt.figure(figsize=(20, 3.5))
            st.subheader(merchant_list[i])
            bar1 = plt.bar(x = df_deactive_list_2021[i].loc[(df_deactive_list[i]['Month-Year'] >= '2021-01-01') & (df_deactive_list_2021[i]['Month-Year'] <= '2021-12-01')]["Month-Year"], height=df_deactive_list_2021[i].loc[(df_deactive_list_2021[i]['Month-Year'] >= '2021-01-01') & (df_deactive_list_2021[i]['Month-Year'] <= '2021-12-01')]["No. of Detokenised Accounts for the Month"], width=5.5)
            for rect in bar1:
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width() /2.0, height, f'{height:.0f}', ha='center', va='bottom')
            st.pyplot(fig)

        if merch == merchant_list[i] and years == "2022" and service == "Total Deactive Tokens": 
            fig = plt.figure(figsize=(20, 3.5))
            st.subheader(merchant_list[i])
            bar1 = plt.bar(x = df_deactive_list_2022[i].loc[(df_deactive_list[i]['Month-Year'] >= '2022-01-01') & (df_deactive_list_2022[i]['Month-Year'] <= '2022-12-01')]["Month-Year"], height=df_deactive_list_2022[i].loc[(df_deactive_list_2022[i]['Month-Year'] >= '2022-01-01') & (df_deactive_list_2022[i]['Month-Year'] <= '2022-12-01')]["No. of Detokenised Accounts for the Month"], width=5.5)
            for rect in bar1:
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width() /2.0, height, f'{height:.0f}', ha='center', va='bottom')
            st.pyplot(fig)