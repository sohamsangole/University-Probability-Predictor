import streamlit as st
import pandas as pd
import admission as ad

st.title('University Probability  Predictor')
DATA_URL = pd.read_csv("admission_predict.csv")

def load_Data():
    # Create a text element and let the reader know the data is loading.
    data_load_state = st.text('Loading data...')
    # Load 10,000 rows of data into the dataframe.
    st.table(DATA_URL)
    # Notify the reader that the data was successfully loaded.
    data_load_state.text('Loading data...done!')

with st.form("my_form"):
    st.write("Enter your details")
    gre = st.text_input("GRE SCORE")
    toefl = st.text_input("TOEFL SCORE")
    uni = st.text_input("University Rating")
    cgpa = st.text_input("CGPA")
    sop = st.text_input("SOP Rating")
    lor = st.text_input("LOR Rating")
    research = st.text_input("Research")
    # Every form must have a submit button.

    submitted = st.form_submit_button("Submit")
    if submitted:
        try:
            percent = ad.model.predict([[int(gre),int(toefl),float(uni),float(sop),float(lor),float(cgpa),int(research)]])[0]
            percent = round(percent*100,3)
            st.subheader("Your Percentage of getting that UNIVERSITY IS " + str(percent))
        except:
            st.write("Invalid Details")
# round(model.predict([[337, 118, 4, 4.5, 4.5, 9.65, 0]])[0]*100, 3)
st.write("Graphical Analysis")

import plotly.express as px

st.subheader("GRE SCORE - TOEFL SCORE - Chance of Admit")
df = DATA_URL
fig = px.scatter(
    df,
    x='Chance of Admit ',
    y='GRE Score',
    color='TOEFL Score',
    color_continuous_scale="reds",
)
st.plotly_chart(fig, theme="streamlit", use_container_width=True)

st.subheader("CGPA - GRE SCORE - Chance of Admit")
df = DATA_URL
fig = px.scatter(
    df,
    x='Chance of Admit ',
    y='CGPA',
    color='GRE Score',
    color_continuous_scale="purpor",
)
st.plotly_chart(fig, theme="streamlit", use_container_width=True)