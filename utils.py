import numpy as np
import planck


def relative_humidity_from_dewpoint(temperature, dewpoint):
    """
    relative_humidity_from_dewpoint(temperature, dewpoint)
    see: https://unidata.github.io/MetPy/latest/api/generated/metpy.calc.relative_humidity_from_dewpoint.html
    """
    e = saturation_vapor_pressure(dewpoint)
    e_s = saturation_vapor_pressure(temperature)
    return e / e_s


def saturation_vapor_pressure(temperature):
    """
    saturation_vapor_pressure(temperature [K]) [Pa]
    see: https://unidata.github.io/MetPy/latest/api/generated/metpy.calc.saturation_vapor_pressure.html#metpy.calc.saturation_vapor_pressure
    """
    return 611.2 * np.exp(17.67 * (temperature - 273.15) / (temperature - 29.65))


def __normalise_lon(longitude):
    normalised_ln = longitude
    normalised_ln[longitude >= 180.0] -= 360
    return normalised_ln


def __calc_emissivity(Fsd, Fsn, Ts):
    epsilon = Fsn / (Fsd - planck.stefan_boltzmann(Ts))
    return epsilon


def __calc_eq_T(F):
    return planck.inv_stefan_boltzmann(F)


def nanrmse(X, Y):
    return np.sqrt(np.nanmean((X - Y) ** 2))
