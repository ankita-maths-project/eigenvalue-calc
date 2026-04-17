import streamlit as st
import numpy as np

st.set_page_config(page_title="Maths Activity", page_icon="📊")
st.title("📊 Eigenvalue & Eigenvector Calculator")
st.write("Engineering Mathematics-II Activity")

# Matrix input
size = st.radio("Matrix Size:", [2, 3], horizontal=True)
matrix = []
for i in range(size):
    cols = st.columns(size)
    row = []
    for j in range(size):
        val = cols[j].number_input(f"A[{i+1},{j+1}]", value=0.0, key=f"{i}{j}")
        row.append(val)
    matrix.append(row)

if st.button("Calculate"):
    A = np.array(matrix)
    eigenvalues, eigenvectors = np.linalg.eig(A)
    st.success("Calculated Successfully!")
    st.subheader("Eigenvalues:")
    st.write(eigenvalues)
    st.subheader("Eigenvectors:")
    st.write(eigenvectors)
