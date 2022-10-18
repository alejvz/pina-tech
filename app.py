
import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle
import warnings

# Path del modelo preentrenado
MODEL_PATH = 'models/pickle_model_dtr.pkl'

st.set_page_config(page_title="APP - Rosinver", page_icon="🍍", layout='centered', initial_sidebar_state="collapsed")


def load_model(modelfile):
	loaded_model = pickle.load(open(modelfile, 'rb'))
	return loaded_model

def main():
    # title with streamlit 
    st.title("🌻APP para predecir la Capacidad de Intercambio Catiónico")
    st.subheader("Creado por: 👨‍🚀 Rosinver Alejandro Vásquez Durán")
    st.subheader(" Diseño e implementación de un sistema de aprendizaje automatico para la prediccion de Capacidad de Intercambio Catiónico 🌱")
    #agregar barra lateral
    st.sidebar.title("Parametros de entrada")

    col1, col2 = st.columns(2)
    with col1:
        ph = st.number_input('pH agua:suelo 2.5:1.0', min_value=0.0, max_value=6.580000, value=0.0, step=1.0, format="%f", key="1")
        p = st.number_input('Fósforo (P) Bray II mg/kg', min_value=0.0, max_value=1708.360000, value=0.0, step=1.0, format="%f", key="2")
        mo = st.number_input('Materia orgánica (MO) %', min_value=0.0, max_value=68.089436, value=0.0, step=1.0, format="%f", key="3")
        ca = st.number_input('Calcio (Ca) intercambiable cmol(+)/kg', min_value=0.0, max_value=103.814240, value=0.0, step=10.0, format="%f", key="4")
        mg = st.number_input('Magnesio (Mg) intercambiable cmol(+)/kg', min_value=0.0, max_value=27.451389, value=0.0, step=1.0, format="%f", key="5")
        k = st.number_input('Potasio (K) intercambiable cmol(+)/kg', min_value=0.0, max_value=8.307200, value=0.0, step=1.0, format="%f", key="6")
        na = st.number_input('Sodio (Na) intercambiable cmol(+)/kg', min_value=0.0, max_value=35.937241, value=0.0, step=1.0, format="%f", key="7")
        s = st.number_input('Azufre (S) mg/kg', min_value=0.0, max_value=1768.167365, value=0.0, step=1.0, format="%f", key="8")
        
    with col2:
        al = st.number_input('Aluminio (Al) intercambiable cmol(+)/kg', min_value=0.0, max_value=25.812844, value=0.0, step=1.0, format="%f", key="9")
        fe = st.number_input('Hierro (Fe) disponible olsen mg/kg', min_value=0.0, max_value=7972.920000, value=0.0, step=100.0, format="%f", key="10")
        ac = st.number_input('Acidez (Al+H) KCL cmol(+)/kg', min_value=0.0, max_value=28.306478, value=0.0, step=1.0, format="%f", key="11")
        ce = st.number_input('Conductividad electrica (CE) relacion 2.5:1.0 dS/m', min_value=0.0, max_value=52.155194, value=0.0, step=1.0, format="%f", key="12")
        cu = st.number_input('Cobre (Cu) disponible mg/kg', min_value=0.0, max_value=221.153925, value=0.0, step=10.0, format="%f", key="20")
        mn = st.number_input('Manganeso (Mn) disponible Olsen mg/kg', min_value=0.0, max_value=883.370000, value=0.0, step=50.0, format="%f", key="21")
        zn = st.number_input('Zinc (Zn) disponible Olsen mg/kg', min_value=0.0, max_value=552.381000, value=0.0, step=50.0, format="%f", key="22")
        b = st.number_input('Boro (B) disponible mg/kg', min_value=0.0, max_value=9.229649, value=0.0, step=1.0, format="%f", key="23")
        
        feature_list = [ph, mo, p, s, ca, mg, ac, al, k, na, ce, fe,  cu, mn, zn, b]
        single_pred = np.array(feature_list).reshape(1, -1)
        #si feature_list tiene algun valor 0, no se puede predecir y se muestra un mensaje de error
        if 0 in feature_list:
            st.warning('Por favor, complete todos los campos', icon="⚠️")
        elif st.button("Predecir"):
            model = load_model(MODEL_PATH)
            prediction = model.predict(single_pred)
            st.write("Predicción: ", prediction)
            st.success('Predicción realizada correctamente', icon="✅")
            st.balloons()

        #mostrar array
        st.write(single_pred)


if __name__ == '__main__':
	main()