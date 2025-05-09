import streamlit as st
import joblib
import pandas as pd

model = joblib.load('nepal_model.pkl')

st.title("Building Damage Prediction App")

st.header("Input Features")
st.subheader('Please note: The model can accutrately predict 70% of the damage grade of buildings in Nepal only.')


age_building = st.number_input("Age of Building (0-999)", min_value=0, max_value=999)

foundation_type = st.selectbox("Foundation Type",  options=['Mud mortar-Stone/Brick', 'Cement-Stone/Brick', 'RC', 'Other', 'Bamboo/Timber'])

ground_floor_type = st.selectbox("Ground Floor Type", options=['Mud', 'Brick/Stone', 'RC', 'Timber', 'Other'])
height_ft_pre_eq = st.number_input("Height (ft) Pre-Earthquake (6-99)", min_value=6, max_value=99)
land_surface_condition = st.selectbox("Land Surface Condition", options=['Flat', 'Moderate slope', 'Steep slope' ])
other_floor_type = st.selectbox ("Other Floor Type", options =['Timber/Bamboo-Mud', 'Timber-Planck', 'RCC/RB/RBC', 'Not applicable'])
plan_configuration = st.selectbox("Plan Configuration", options=['Rectangular', 'Square', 'L-shape', 'Multi-projected', 'Others', 'U-shape', 'T-shape', 'H-shape', 
'E-shape', 'Building with Central Courtyard'])
plinth_area_sq_ft = st.number_input("Plinth Area (sq ft) (70-4995)", min_value = 70, max_value = 4995)
position = st.selectbox("Position", options= ['Not attached', 'Attached-1 side', 'Attached-2 side', 'Attached-3 side'])
roof_type = st.selectbox("Roof Type", options=['Bamboo/Timber-Heavy roof', 'Bamboo/Timber-Light roof', 'RCC/RB/RBC'])
superstructure = st.selectbox("superstructure", options=['mud_mortar_stone', 'cement_mortar_brick', 'rc_non_engineered', 'stone_flag', 'adobe_mud', 'mud_mortar_brick',
'timber', 'cement_mortar_stone', 'rc_engineered', 'bamboo', 'other'])
input_data = {
    'age_building': age_building,
    'foundation_type': foundation_type, 
    'ground_floor_type':ground_floor_type,
    'height_ft_pre_eq' :height_ft_pre_eq,
    'land_surface_condition': land_surface_condition,
    'other_floor_type': other_floor_type,
    'plan_configuration': plan_configuration,
    'plinth_area_sq_ft': plinth_area_sq_ft,
    'position': position,
    'roof_type': roof_type,
    'superstructure': superstructure
}







input_df= pd.DataFrame ([input_data])

if st.button("Predict"):
    prediction = model.predict(input_df)
    if prediction == 1:
        st.info("Prediction: was affected by earthquake")
    else:
        st.info("Prediction: was not affected by earthquake")