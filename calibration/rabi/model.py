import numpy as np

def rabi_model(t, A, Omega, B):
    return A * np.sin(0.5 * Omega * t)**2 + B
