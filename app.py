import streamlit as st

# Constante de los gases en atm·L/mol·K
R = 0.0821

st.title("Calculadora de la ecuación de los gases ideales")
st.markdown("Ecuación: **PV = nRT**")

opcion = st.selectbox(
    "¿Qué variable deseas calcular?",
    ("Presión (P)", "Volumen (V)", "Temperatura (T)", "Número de moles (n)")
)

if opcion == "Presión (P)":
    volumen = st.number_input("Volumen (L)", min_value=0.0, format="%.4f")
    temperatura = st.number_input("Temperatura (K)", min_value=0.0, format="%.2f")
    moles = st.number_input("Número de moles (mol)", min_value=0.0, format="%.4f")
    if st.button("Calcular Presión"):
        if volumen > 0:
            presion = (moles * R * temperatura) / volumen
            st.success(f"Presión = {presion:.4f} atm")
        else:
            st.error("El volumen debe ser mayor que 0")

elif opcion == "Volumen (V)":
    presion = st.number_input("Presión (atm)", min_value=0.0, format="%.4f")
    temperatura = st.number_input("Temperatura (K)", min_value=0.0, format="%.2f")
    moles = st.number_input("Número de moles (mol)", min_value=0.0, format="%.4f")
    if st.button("Calcular Volumen"):
        if presion > 0:
            volumen = (moles * R * temperatura) / presion
            st.success(f"Volumen = {volumen:.4f} L")
        else:
            st.error("La presión debe ser mayor que 0")

elif opcion == "Temperatura (T)":
    presion = st.number_input("Presión (atm)", min_value=0.0, format="%.4f")
    volumen = st.number_input("Volumen (L)", min_value=0.0, format="%.4f")
    moles = st.number_input("Número de moles (mol)", min_value=0.0, format="%.4f")
    if st.button("Calcular Temperatura"):
        if moles > 0:
            temperatura = (presion * volumen) / (moles * R)
            st.success(f"Temperatura = {temperatura:.2f} K")
        else:
            st.error("Los moles deben ser mayores que 0")

elif opcion == "Número de moles (n)":
    presion = st.number_input("Presión (atm)", min_value=0.0, format="%.4f")
    volumen = st.number_input("Volumen (L)", min_value=0.0, format="%.4f")
    temperatura = st.number_input("Temperatura (K)", min_value=0.0, format="%.2f")
    if st.button("Calcular Número de moles"):
        if temperatura > 0:
            moles = (presion * volumen) / (R * temperatura)
            st.success(f"Número de moles = {moles:.4f} mol")
        else:
            st.error("La temperatura debe ser mayor que 0")
