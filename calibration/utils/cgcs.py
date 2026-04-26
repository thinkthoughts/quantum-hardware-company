import numpy as np

def phase_lock_metric(signal, fit):
    # cosine similarity between signal and model
    dot = np.dot(signal, fit)
    norm = np.linalg.norm(signal) * np.linalg.norm(fit)
    return dot / norm

def is_phase_locked(metric, threshold=1/np.sqrt(2)):
    return metric >= threshold
