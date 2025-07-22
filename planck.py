"""
Copyright (C) 2025, Claudio Belotti, Consiglio Nazionale delle Ricerche (CNR)
claudio.belotti@cnr.it

    This file is part of PASTICCIO:
    the PaRaMetriC Atmospheric Spectral Tool for Irradiance CalCulation, Infrared Output.

    PASTICCIO is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    PASTICCIO is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with PASTICCIO.  If not, see <http://www.gnu.org/licenses/>.


planck.py
"""


import numpy as np

# see
# https://www.spectralcalc.com/blackbody/CalculatingBlackbodyRadianceV2.pdf

K = 1.3806488e-23 # Boltzmann constant [JK^-1]
h = 6.62606957e-34 # Planck constant [Js]
c = 2.99792458e8 # speed of light ms^-1
c1 = 2e8*h*c**2
c2 = 100*h*c/K

def B(sigma, T):
    '''
    B(sigma,T):
    Blackbody spectral radiance per wavenumber [cm-1]
    [W (m2 sr cm-1)-1]
    sigma: wavenumber [cm-1]
    T: temperature [K]
    '''
    ## come B_sigma ma lo lascio per ragioni "storiche"
    s = sigma
    return c1*s**3/(np.exp(c2*s/T)-1) # W (m^2 sr cm^-1)^-1


def B_sigma(sigma, T):
    '''
    B_sigma(sigma,T):
    Blackbody spectral radiance per wavenumber [cm-1]
    [W (m2 sr cm-1)-1]
    sigma: wavenumber [cm-1]
    T: temperature [K]
    '''
    v = 100*c*sigma
    return 100*c*B_nu(v,T) # W (m^2 sr cm^-1)^-1


def B_nu(nu, T):
    '''
    B(nu,T):
    Blackbody spectral radiance per frequency [Hz]
    [W (m2 sr Hz)-1]
    nu: frequency [Hz]
    T: temperature [K]
    '''
    a = 2*h/c**2
    b = h/K
    return a*nu**3/(np.exp(b*nu/T)-1) # W (m^2 sr Hz)^-1


def sigma_peak(T):
    '''
    sigma_peak(T) [cm-1]
    wavenumber of the maximum spectral radiance

    Notice that for a given temperature, parameterization by frequency (or wavenumber) 
    implies a different maximal wavelength than parameterization by wavelength.
    https://en.wikipedia.org/wiki/Wien%27s_displacement_law#Maxima_differ_according_to_parameterization    '''
    return  nu_peak(T)/(100*c)# [cm-1]


def nu_peak(T):
    '''
    nu_peak(T) [Hz]
    frequency of the maximum spectral radiance

    Notice that for a given temperature, parameterization by frequency (or wavenumber) 
    implies a different maximal wavelength than parameterization by wavelength.
    https://en.wikipedia.org/wiki/Wien%27s_displacement_law#Maxima_differ_according_to_parameterization    '''
    a3 = 2.82143937212
    return a3*K*T/h # [Hz]


def dBdT(sigma, T):
    '''
    dBdT(sigma, T)
    sigma: wavenumber [cm-1]
    T: temperature [K]
    '''
    s = sigma
    return c1*s**3/(np.exp(c2*s/T)-1)**2 * np.exp(c2*s/T) * (c2*s/T**2)


def BT(sigma, L, epsilon=1.0):
    '''
    BT(sigma,L,epsilon=1.0):
    Brightness temperature per wavenumber [cm-1]
    [K]
    sigma: wavenumber [cm-1]
    L: radiance [W (m2 sr cm-1)-1]
    epsilon: emissivity
    '''
    s = sigma
    return c2*s/np.log(1 + epsilon*c1*(s**3)/L)


def B_integral_band(sigma1, sigma2, temperature):
    # integral of spectral radiance over a spectral band
    # from sigma1 to sigma2 (cm-1)
    # returns [W m-2 sr-1] 
    return __planck_integral(sigma1, temperature)- __planck_integral(sigma2, temperature)


def __planck_integral(sigma, temperature):
    # https://www.spectralcalc.com/blackbody/appendixA.html 
    # integral of spectral radiance from sigma (cm-1) to infinity.
    # result is W/m2/sr.
    # follows Widger and Woodall, Bulletin of the American Meteorological
    # Society, Vol. 57, No. 10, pp. 1217
 
    # constants

    Planck =  6.6260693e-34     
    Boltzmann = 1.380658e-23 
    Speed_of_light = 299792458.0 
    Speed_of_light_sq = Speed_of_light * Speed_of_light 

    # compute powers of x, the dimensionless spectral coordinate

    c1 =  (Planck*Speed_of_light/Boltzmann) 
    x =  c1 * 100 * sigma / temperature 
    x2 = x *  x  
    x3 = x *  x2 

    # decide how many terms of sum are needed

    iterations = 2.0 + 20.0/x ;
    iterations = iterations if (iterations<512) else 512
    iter = int(iterations)

    # add up terms of sum

    sum = 0  ;
    for n in range(1,iter):
        dn = 1.0/n ;
        sum  += np.exp(-n*x)*(x3 + (3.0 * x2 + 6.0*(x+dn)*dn)*dn)*dn

    # return result, in units of W/m2/sr
    c2 =  (2.0*Planck*Speed_of_light_sq)
    return  sum*c2*(temperature/c1)**4


def B_lambda(l,T):
    '''
    B_lambda(l,T):
    Blackbody spectral radiance per wavelength [µm]
    [W m-2 sr-1 µm-1]
    l: wavelength [µm]
    T: temperature K
    '''
    
    a = 2e24*h*c**2
    b = 1e6*h*c/K
    return a/l**5/(np.exp(b/(l*T))-1)


def lambda_peak(T):
    '''
    lmabda_peak(T) [µm]
    wavelength of the maximum spectral radiance

    Notice that for a given temperature, parameterization by frequency (or wavenumber) 
    implies a different maximal wavelength than parameterization by wavelength.
    https://en.wikipedia.org/wiki/Wien%27s_displacement_law#Maxima_differ_according_to_parameterization    '''
    a5 = 4.96511423174    
    return 1e6*h*c/(a5*K*T) # [µm]


def stefan_boltzmann(T):
    sigma = 5.670367e-8 # W m**-2 K**-4
    return sigma*np.power(T,4)

def inv_stefan_boltzmann(F):
    sigma = 5.670367e-8 # W m**-2 K**-4
    return np.power(F/sigma,1./4)
