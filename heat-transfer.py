import numpy as np
import plotly.express as px
import streamlit as st
from scipy.ndimage import gaussian_filter
import random
import time

st.title('2D Heat Equation Simulation')
st.sidebar.header('Parameters')

Lx = st.sidebar.number_input('Domain Length (Lx)', min_value=1.0, max_value=100.0, value=1.0, step=0.1)
Ly = st.sidebar.number_input('Domain Width (Ly)', min_value=1.0, max_value=100.0, value=1.0, step=0.1)
Nx = st.sidebar.number_input('Grid Points (Nx)', min_value=10, max_value=100, value=50, step=10)
Ny = st.sidebar.number_input('Grid Points (Ny)', min_value=10, max_value=100, value=50, step=10)
alpha = st.sidebar.number_input('Thermal Diffusivity (alpha)', min_value=0.01, max_value=1.0, value=0.01, step=0.001)
T_left = st.sidebar.number_input('Temperature at Left Boundary', min_value=0, max_value=1000, value=500, step=10)
T_right = st.sidebar.number_input('Temperature at Right Boundary', min_value=0, max_value=1000, value=500, step=10)
T_top = st.sidebar.number_input('Temperature at Top Boundary', min_value=0, max_value=1000, value=500, step=10)
T_bottom = st.sidebar.number_input('Temperature at Bottom Boundary', min_value=0, max_value=1000, value=100, step=10)

T = np.random.randint(5000, size=(Ny,Nx))
#T = np.zeros((Ny, Nx))
T = gaussian_filter(T, sigma=2)

dx = Lx / (Nx - 1)
dy = Ly / (Ny - 1)

T = np.zeros((Ny, Nx))

T[0, :] = T_bottom
T[Ny - 1, :] = T_top
T[:, 0] = T_left
T[:, Nx - 1] = T_right

# Create a placeholder for the Plotly figure
st_plot = st.empty()

# Main simulation loop
num_iterations = 2000
for iteration in range(num_iterations):
    for i in range(1, Ny - 1):
        for j in range(1, Nx - 1):
            T[i, j] = 0.25 * (T[i+1, j] + T[i-1, j] + T[i, j+1] + T[i, j-1])
    if iteration % 100 == 0:
        #time.sleep(1)
        X, Y = np.meshgrid(np.linspace(0, Lx, Nx), np.linspace(0, Ly, Ny))
        fig = px.imshow(T, x=X[0], y=Y[:, 0], color_continuous_scale='viridis')  # Use 'viridis' colorscale
        fig.update_layout(title='Temperature Distribution', xaxis_title='X', yaxis_title='Y')
        st_plot.plotly_chart(fig)

# Final temperature distribution
X, Y = np.meshgrid(np.linspace(0, Lx, Nx), np.linspace(0, Ly, Ny))
fig_final = px.imshow(T, x=X[0], y=Y[:, 0], color_continuous_scale='viridis')
fig_final.update_layout(title='Temperature Distribution Final', xaxis_title='X', yaxis_title='Y')
st_plot.plotly_chart(fig_final)