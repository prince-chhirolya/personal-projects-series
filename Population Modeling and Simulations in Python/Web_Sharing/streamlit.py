import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

st.set_page_config(layout = "wide", page_title = "Streamlit Data-centric App", page_icon = ":taxi:")

def simple_sir_step_ahead(y, t, N, beta, gamma):
    S, I = y
    dsdt = -beta * I * (S / N)
    didt = beta * I * (S / N) - gamma * I
    return dsdt, didt


def simplified_sir_sim(N, sim_days, orig_infected, prob_infect, contact_with_people, inf_days):
    y0 = N-orig_infected, orig_infected
    beta = prob_infect*contact_with_people
    gamma = 1.0 / inf_days
    t = np.linspace(0, sim_days-1, sim_days)
    sim_res = odeint(simple_sir_step_ahead, y0, t, args=(N, beta, gamma))
    return sim_res

    
def sir_phase_space_plot():
    plt.clf()
    y = simplified_sir_sim(N, sim_days, orig_infected, prob_infect, contact_with_people, inf_days)
    plt.plot(y[:, 0], y[:, 1])

    # Direction fields creation process from: https://scipy-cookbook.readthedocs.io/items/LoktaVolterraTutorial.html
    # Creating a grid and computing the direction at each point
    nb_points = 20
    ymax = plt.ylim(ymin=0)[1]
    xmax = plt.xlim(xmin=0)[1]
    x = np.linspace(0, xmax, nb_points)
    y = np.linspace(0, ymax, nb_points)
    X1 , Y1  = np.meshgrid(x, y) 
    # Computing growth rate on the grid
    DX1, DY1 = simple_sir_step_ahead([X1 , Y1], 0, N, prob_infect*contact_with_people, 1.0 / inf_days)
    # Norm of the growth rate 
    M = (np.hypot(DX1, DY1))    
    # Avoiding zero division errors 
    M[ M == 0] = 1.0
    # Normalizing the arrows
    DX1 /= M      
    DY1 /= M

    plt.title('Trajectories and direction fields')
    # Drawing direction fields and using different colors to highlight gorwth speed
    Q = plt.quiver(X1, Y1, DX1, DY1, M, pivot='mid', cmap=plt.cm.jet)
    plt.xlabel('Susceptible')
    plt.ylabel('Infected')
    plt.grid()
    plt.xlim(0, xmax)
    plt.ylim(0, ymax)
    st.pyplot(plt)
    
    
st.title('Epidemic Modelling App')
    
st.text('Choose your favourite parameters to run the SIR Phase Space Plot')
    
N = st.slider('Population Size', 0, 1000, 500)
sim_days = st.slider('Simulation Days', 0, 1000, 100)
orig_infected = st.slider('Number of individuals originally infected', 0, N, 3)
prob_infect = st.slider('Probability to get infected', 0.0, 1.0, 0.3)
contact_with_people = st.slider('Avg Number of people we are in close contact with', 0, N, 2)
inf_days = st.slider('Days the infection lasts', 0, sim_days//3, 3)

sir_phase_space_plot()