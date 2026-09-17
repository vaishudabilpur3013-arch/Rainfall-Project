import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("🌧️ Rainfall Prediction")

month = st.selectbox(
    "Month",
    ["January","February","March","April","May","June",
     "July","August","September","October","November","December"]
)

season = st.selectbox(
    "Season",
    ["Summer","Monsoon","Post-monsoon","Winter"]
)

avg_temperature = st.number_input("Average_Temperature")

if st.button("Predict Rainfall"):
    st.success("Prediction completed!")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Rainfall Prediction - Graphs(EDA)")

# Load dataset
df = pd.read_excel("india_weather_rainfall_data.xlsx")

# Show dataset
st.dataframe(df.head())

# 1. Rainfall by Month
st.subheader("Rainfall by Month")
m = df.groupby("month")["rainfall"].mean()
st.bar_chart(m)

# 2. Rainfall by Season
st.subheader("Rainfall by Season")
s = df.groupby("season")["rainfall"].mean()
st.bar_chart(s)

# 3. Rainfall by State
st.subheader("Rainfall by State")
state = df.groupby("state")["rainfall"].mean().sort_values(ascending=False).head(10)
st.bar_chart(state)

# 4. Temperature vs Rainfall
st.subheader("Temperature vs Rainfall")
fig, ax = plt.subplots()
ax.scatter(df["avg_temp"], df["rainfall"], alpha=0.3)
ax.set_xlabel("Average Temperature")
ax.set_ylabel("Rainfall")
st.pyplot(fig)

# 5. Rainfall Distribution
st.subheader("Rainfall Distribution")
fig, ax = plt.subplots()
ax.hist(df["rainfall"].dropna(), bins=30)
ax.set_xlabel("Rainfall")
ax.set_ylabel("Frequency")
st.pyplot(fig)
