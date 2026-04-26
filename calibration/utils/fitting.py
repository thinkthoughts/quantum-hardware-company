from scipy.optimize import curve_fit

def fit_model(model, t, y, p0):
    params, cov = curve_fit(model, t, y, p0=p0)
    return params, cov

def residuals(model, t, y, params):
    return y - model(t, *params)
