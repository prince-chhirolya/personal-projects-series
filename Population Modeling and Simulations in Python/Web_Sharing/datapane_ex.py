import datapane as dp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

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

    
def sir_phase_space_plot(N, sim_days, orig_infected, prob_infect, contact_with_people, inf_days):
    fig = plt.figure(figsize=(8,8))
    y = simplified_sir_sim(N, sim_days, orig_infected, prob_infect, contact_with_people, inf_days)
    plt.plot(y[:, 0], y[:, 1])

    # Direction fields creation process from: https://scipy-cookbook.readthedocs.io/items/LoktaVolterraTutorial.html
    # Creating a grid and computing the direction at each point
    nb_points = 20
    ymax = plt.ylim(ymin=0)[1]
    xmax = plt.xlim(xmin=0)[1]
    x_grid = np.linspace(0, xmax, nb_points)
    y_grid = np.linspace(0, ymax, nb_points)
    X1 , Y1  = np.meshgrid(x_grid, y_grid) 
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
    return y, dp.Plot(fig)


def f(params, N, sim_days, orig_infected, prob_infect, contact_with_people, inf_days):
    y, sim_plt = sir_phase_space_plot(int(N), int(sim_days), int(orig_infected), prob_infect, int(contact_with_people), int(inf_days))
    df = pd.DataFrame(y, columns = ['Susceptible','Infected'])
    return dp.View(dp.DataTable(df), sim_plt)


N = 500
sim_days = 100
view = dp.View(dp.Form(on_submit=f,
        controls=dp.Controls(N=dp.Range(initial=N, min=0, max=1000, step=1), 
                             sim_days=dp.Range(initial=sim_days, min=0, max=1000, step=1),
                             orig_infected=dp.Range(initial=3, min=0, max=int(N), step=1),
                             prob_infect=dp.Range(initial=0.3, min=0, max=1, step=0.01),
                             contact_with_people=dp.Range(initial=2, min=0, max=int(N), step=1),
                             inf_days=dp.Range(initial=3, min=0, max=int(sim_days)//3, step=1),
                            )
        ))

dp.serve_app(view, host='0.0.0.0', port=5000, embed_mode=True)