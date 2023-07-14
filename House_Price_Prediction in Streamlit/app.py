import pandas as pd
import numpy as np
import joblib
import streamlit as st
import matplotlib.pyplot as plt
import shap
import seaborn as sns

df = pd.read_csv("feature_engineered_data.csv")
df.rename(columns={'<1H OCEAN': 'In OCEAN'}, inplace=True)
print(df.info())


print("Min longitude and latitude: ", df['longitude'].min(
), df['latitude'].min(), df['longitude'].max(), df['latitude'].max())


class HousePricePrediction:
    def __init__(self):
        self.setTheme("California House Price Prediction")
        self.SideBar()
        model, predition = self.model_predictions()
        
        st.subheader("Scatter Plot")
        fig = plt.figure(figsize=(10, 4))
        sns.scatterplot(x=df['latitude'], y=df['longitude'],
                        data=df, hue=df['median_house_value'])
        plt.scatter(x=self.latitude, y=self.longitude, label='Prediction')
        
        st.pyplot(fig)
        st.subheader("California Map visualized on training set")
        st.map(df)

    def setTheme(self, name):
        st.title(name)

    def SideBar(self):
        with st.sidebar:
            # st.markdown(
            # """
            # <style>
            # [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
            #     width: 500px;
            # }
            # [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
            #     width: 500px;
            #     margin-left: -500px;
            # }
            # </style>
            # """,
            # unsafe_allow_html=True,
            # )
            st.title("Input Data")

            self.input_data = self.take_input()
            col_names = ['longitude', 'latitude', 'housing_median_age', 'total_rooms',
                         'total_bedrooms', 'population', 'households', 'median_income',
                         '<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN',
                         'household_per_room']
            self.input_data = pd.DataFrame(
                [self.input_data], columns=col_names)
            print(self.input_data.iloc[0].shape)

    def take_input(self):
        self.longitude = st.slider("Longitude", df['longitude'].min(
        ), df['longitude'].max(), float(df['longitude'].mean()))
        self.latitude = st.slider("Latitude", df['latitude'].min(
        ), df['latitude'].max(), float(df['latitude'].mean()))
        self.age = st.slider("Age", int(df['housing_median_age'].min()), 100, int(
            df['housing_median_age'].mean()))

        self.total_rooms = st.slider("Rooms (Total)", int(df['total_rooms'].min()), int(
            df['total_rooms'].max()), int(df['total_rooms'].min()), 5)
        self.total_bedrooms = st.slider("BedRooms", int(df['total_bedrooms'].min()), int(
            df['total_bedrooms'].max()), int(df['total_bedrooms'].mode()[0]))
        if self.total_rooms < self.total_bedrooms:
            st.error(
                "Error: Total number of rooms should be greater than or equal to the total number of bedrooms.")
        self.median_income = st.slider("Median Income ($10K)", float(df['median_income'].min(
        )), float(df['median_income'].max()), float(df['median_income'].mean()))
        self.population = df['population'].mean()
        self.households = df['households'].mean()
        area_options = ("IN OCEAN", "INLAND", "ISLAND",
                        "NEAR BAY", "NEAR OCEAN")
        area = st.selectbox(
            "Select area",
            area_options,
            index=1
        )
        self.area_encoded = [1 if option ==
                             area else 0 for option in area_options]
        self.household_per_room = self.total_rooms / self.households

        input_data = []

        input_data.append(float(self.longitude))
        input_data.append(float(self.latitude))
        input_data.append(int(self.age))
        input_data.append(float(self.total_rooms))
        input_data.append(float(self.total_bedrooms))
        input_data.append(float(self.population))
        input_data.append(float(self.households))
        input_data.append(float(self.median_income))
        input_data.extend(self.area_encoded)
        input_data.append(float(self.household_per_room))

        return input_data

    def model_predictions(self):
        model = joblib.load(
            'E:/SecondSummer/Projects/ML/ML-DL-Projects/House_Price_Prediction in Streamlit/model_jlib')
        # model = pickle.load('E:/SecondSummer/Projects/ML/ML-DL-Projects/House_Price_Prediction in Streamlit/model_jlib')
        yhat = model.predict(self.input_data)
        st.write('Model predictions: ', round(yhat[0], 2))
        return model, yhat


if __name__ == '__main__':
    hpp = HousePricePrediction()
