from turtle import color
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_excel(r'U:\Users\00148245\Desktop\omar\Digital_Analytics\CASA_ON_FILE\DEC\COF_DEC_22.xlsx')
df_active = pd.read_excel(r'U:\Users\00148245\Desktop\omar\Digital_Analytics\CASA_ON_FILE\DEC\COF_DEC_22.xlsx', "Total Active Tokens")
df_deactive = pd.read_excel(r'U:\Users\00148245\Desktop\omar\Digital_Analytics\CASA_ON_FILE\DEC\COF_DEC_22.xlsx', "Total Deactive Tokens")

def add_year_column(dataframe):
    years = []
    for i in np.arange(0, len(dataframe)):
        yr = dataframe["Month-Year"][i].strftime("%Y")
        years.append(yr)
    dataframe["Year"] = years

add_year_column(df)
add_year_column(df_active)
add_year_column(df_deactive)

def get_statistics(dataframe, service, i, j):
    value = np.array(dataframe[service][(dataframe["Year"] == year_list[i]) & (dataframe["Merchant"] == merchant_list[j])])
    value_max = value.max()
    value_min = value.min()
    value_avg = value.mean()
    date_max = dataframe["Month-Year"][(dataframe[service] == value_max) & (dataframe["Merchant"] == merchant_list[j])].to_string().split(" ")[3]
    date_min = dataframe["Month-Year"][(dataframe[service] == value_min) & (dataframe["Merchant"] == merchant_list[j])].to_string().split(" ")[3]

    st.text("Max: {} at {}".format(value_max, date_max))
    st.text("Min: {} at {}".format(value_min, date_min))
    st.text("Avg: {}".format(value_avg))

st.set_page_config(layout="wide")

merchant_list  = pd.unique(df["Merchant"])
year_list = pd.unique(df["Year"])
service_list = ["Total Payments", "Total Active Tokens", "Total Deactive Tokens"]

merchants = st.multiselect("Merchant Type: ", merchant_list)
col1, col2  = st.columns([1,1])
with col1:
    years = st.selectbox("Year: ", year_list)
with col2:
    service = st.selectbox("Service :", service_list)
st.header("You selected: {}".format(", ".join(merchants)))

st.header("Transaction Volume")

for merch in merchants:
    for i in np.arange(0, len(year_list)):
        for j in np.arange(0, len(merchant_list)):

            if merch == merchant_list[j] and years == year_list[i] and service == "Total Payments":
                
                fig = plt.figure(figsize=(20, 3.5))
                st.subheader(merchant_list[j])

                get_statistics(df, "Total Transaction Volume", i, j)

                bar1 = plt.bar(x = df["Month-Year"][(df["Year"] == year_list[i]) & (df["Merchant"] == merchant_list[j])], height=df["Total Transaction Volume"][(df["Year"] == year_list[i]) & (df["Merchant"] == merchant_list[j])], width=5.5)
                for rect in bar1:
                    height = rect.get_height()
                    plt.text(rect.get_x() + rect.get_width() /2.0, height, f'{height:.0f}', ha='center', va='bottom')
                st.pyplot(fig)

            if merch == merchant_list[j] and years == year_list[i] and service == "Total Active Tokens":
                fig = plt.figure(figsize=(20, 3.5))
                st.subheader(merchant_list[j])

                get_statistics(df_active, "No. of Active Tokenised Accounts for the Month", i, j)
            
                bar1 = plt.bar(x = df_active["Month-Year"][(df_active["Year"] == year_list[i]) & (df_active["Merchant"] == merchant_list[j])], height=df_active["No. of Active Tokenised Accounts for the Month"][(df_active["Year"] == year_list[i]) & (df_active["Merchant"] == merchant_list[j])], width=5.5)
                for rect in bar1:
                    height = rect.get_height()
                    plt.text(rect.get_x() + rect.get_width() /2.0, height, f'{height:.0f}', ha='center', va='bottom')
                st.pyplot(fig)

            if merch == merchant_list[j] and years == year_list[i] and service == "Total Deactive Tokens": 
                fig = plt.figure(figsize=(20, 3.5))
                st.subheader(merchant_list[j])

                get_statistics(df_deactive, "No. of Detokenised Accounts for the Month", i, j)

                bar1 = plt.bar(x = df_deactive["Month-Year"][(df_deactive["Year"] == year_list[i]) & (df_deactive["Merchant"] == merchant_list[j])], height=df_deactive["No. of Detokenised Accounts for the Month"][(df_deactive["Year"] == year_list[i]) & (df_deactive["Merchant"] == merchant_list[j])], width=5.5)
                for rect in bar1:
                    height = rect.get_height()
                    plt.text(rect.get_x() + rect.get_width() /2.0, height, f'{height:.0f}', ha='center', va='bottom')
                st.pyplot(fig)

st.header("Transaction Value (RM)")
for merch in merchants:
    for i in np.arange(0, len(year_list)):
        for j in np.arange(0, len(merchant_list)):

            if merch == merchant_list[j] and years == year_list[i] and service == "Total Payments":
                
                fig = plt.figure(figsize=(20, 3.5))
                st.subheader(merchant_list[j])

                get_statistics(df, "Total Transaction Value (RM)", i, j)

                bar1 = plt.bar(x = df["Month-Year"][(df["Year"] == year_list[i]) & (df["Merchant"] == merchant_list[j])], height=df["Total Transaction Value (RM)"][(df["Year"] == year_list[i]) & (df["Merchant"] == merchant_list[j])], width=5.5, color = "orange")
                for rect in bar1:
                    height = rect.get_height()
                    plt.text(rect.get_x() + rect.get_width() /2.0, height, f'{height:.0f}', ha='center', va='bottom')
                st.pyplot(fig)

            if merch == merchant_list[j] and years == year_list[i] and service == "Total Active Tokens":
                fig = plt.figure(figsize=(20, 3.5))
                st.subheader(merchant_list[j])

                get_statistics(df_active, "Average Customer Limit Set for Active Accounts (RM)", i, j)
            
                bar1 = plt.bar(x = df_active["Month-Year"][(df_active["Year"] == year_list[i]) & (df_active["Merchant"] == merchant_list[j])], height=df_active["Average Customer Limit Set for Active Accounts (RM)"][(df_active["Year"] == year_list[i]) & (df_active["Merchant"] == merchant_list[j])], width=5.5, color = "orange")
                for rect in bar1:
                    height = rect.get_height()
                    plt.text(rect.get_x() + rect.get_width() /2.0, height, f'{height:.0f}', ha='center', va='bottom')
                st.pyplot(fig)

            if merch == merchant_list[j] and years == year_list[i] and service == "Total Deactive Tokens": 
                fig = plt.figure(figsize=(20, 3.5))
                st.subheader(merchant_list[j])

                get_statistics(df_deactive, "Average Customer Limit Set for Deactive Accounts (RM)", i, j)

                bar1 = plt.bar(x = df_deactive["Month-Year"][(df_deactive["Year"] == year_list[i]) & (df_deactive["Merchant"] == merchant_list[j])], height=df_deactive["Average Customer Limit Set for Deactive Accounts (RM)"][(df_deactive["Year"] == year_list[i]) & (df_deactive["Merchant"] == merchant_list[j])], width=5.5, color = "orange")
                for rect in bar1:
                    height = rect.get_height()
                    plt.text(rect.get_x() + rect.get_width() /2.0, height, f'{height:.0f}', ha='center', va='bottom')
                st.pyplot(fig)
