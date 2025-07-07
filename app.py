import streamlit as st
from operations import *
import time


st.set_page_config(
    page_title="MathBuddy",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.sidebar.title("Configuraciones")
st.session_state.max_cifras = int(st.sidebar.text_input("¿Cuántas cifras máximo?", value=1))

st.sidebar.markdown("---")
oper_sumas = st.sidebar.checkbox("Sumas", value=True)
oper_restas = st.sidebar.checkbox("Restas", value=False)
oper_mul = st.sidebar.checkbox("Multiplicaciones", value=False)
oper_div = st.sidebar.checkbox("Divisiones", value=False)

st.session_state.oper = []
if oper_sumas:
    st.session_state.oper.append('+')
if oper_restas:
    st.session_state.oper.append('-')
if oper_mul:
    st.session_state.oper.append('*')
if oper_div:
    st.session_state.oper.append('/')


st.title("MathBuddy")
st.write("Prueba tus conocimientos de matemáticas!! 😆")

if "operacion" not in st.session_state:
    operando = random.choice(st.session_state.oper)
    st.session_state.operacion = generate_random_operation(st.session_state.max_cifras, operando)
    st.session_state.operacion_res = f"{st.session_state.operacion[0]} {st.session_state.operacion[1]} {st.session_state.operacion[2]}"
    st.session_state.n_res_correctas = 0
    st.session_state.n_res_incorrectas = 0

if 'operacion' in st.session_state:
    st.title(st.session_state.operacion_res +" = ")
    respuesta = st.text_input("¿Cuánto es "+st.session_state.operacion_res+"?")
    if respuesta:
        if int(respuesta.strip()) == corregir(st.session_state.operacion):
            st.success("🤗 Welldone!!")
            st.session_state.n_res_correctas+=1
            time.sleep(2)
            operando = random.choice(st.session_state.oper)
            st.session_state.operacion = generate_random_operation(st.session_state.max_cifras, operando)
            st.session_state.operacion_res = f"{st.session_state.operacion[0]} {st.session_state.operacion[1]} {st.session_state.operacion[2]}"
            st.session_state.respuesta = ""
            st.rerun()
        else:
            st.error("🚨 Keep trying 💪")
            st.session_state.n_res_incorrectas+=1

st.write("🌟: "+ str(st.session_state.n_res_correctas) +" 🥺: "+ str(st.session_state.n_res_incorrectas))
