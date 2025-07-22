"""
Copyright (C) 2025
Claudio Belotti (CNR-INO, Italy), claudio.belotti@cnr.it
Lorenzo Pattelli (INRiM, Italy), l.pattelli@inrim.it


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


era5.py
"""

import numpy as np
import datetime
import logging
# from sklearn.neighbors import BallTree

def closest_gridpoint(x, latitude=None, longitude=None):
    '''
    closest_gridpoint(x, latitude=None, longitude=None):
    given x 
    x = (lat, lon)
    finds c closest ERA5 gridpoint to x.
    returns:
    indices (i,j) of the point wrt the grid
    c=(lat,lon);
    if latitude and longitude are None (default) 
    assumes a full ERA5 grid 721x1440, 0.25 deg resolution;
    distance from x to c in km
    '''
    if latitude is None:
        latitude = np.linspace(90., -90., 721) # full ERA5 grid
    if longitude is None:
        longitude = np.linspace(0., 359.75, 1440) # full ERA5 grid

    LT,LN = np.meshgrid(latitude,longitude)
    D = __haversine((LT.ravel(),LN.ravel()), x)
    ii = D.argmin()
    d = D[ii]
    indices = np.unravel_index(ii, LT.shape) # (ln,lt)
    indices = (indices[1], indices[0]) # swap -> (lt,ln)
    c = (latitude[indices[0]], longitude[indices[1]])

    # if lon of x is negative
    # adapt c lon to -180:180 grid
    if (x[1]<0) and (c[1]>=180):
        c = (latitude[indices[0]], longitude[indices[1]]-360)

    logging.debug(f"x={x}, c={c}, indices={indices}, d(x,c)={d:.3} km")
    return indices, c, d
    
def __haversine(A, B):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)

    see: https://stackoverflow.com/a/4913653
    """
    Alt, Aln = A
    Blt, Bln = B
    # convert decimal degrees to radians 
    lat1, lon1, lat2, lon2 = map(np.deg2rad, [Alt, Aln, Blt, Bln])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r

def z2h(z, Re=6371.2290, g0=9.80665):
    ''' geopotential [m**2 s**-2] to altitude [m]
    Ref:
    https://confluence.ecmwf.int/display/CKB/ERA5%3A+compute+pressure+and+geopotential+on+model+levels%2C+geopotential+height+and+geometric+height#heading-Geometricheight
    https://unidata.github.io/MetPy/latest/api/generated/metpy.calc.geopotential_to_height.html#metpy.calc.geopotential_to_height
    '''
    Re *= 1000 # m
    return z*Re/(g0*Re-z)


def time2datetime(e5time):
    d0 = datetime.datetime(1900, 1, 1, 0, 0, 0)
    if hasattr(e5time, '__len__'):
        d1 = [d0 + datetime.timedelta(hours=int(t)) for t in e5time.flatten()]
        if len(d1)==1: # this is UGLY
            d1 = d1[0]
    else:
        d1 = d0 + datetime.timedelta(hours=int(e5time))
    return d1


def np_time2datetime(e5time):
    d0 = np.datetime64('1900-01-01')
    d1 = d0 + e5time.astype('timedelta64[h]')
    return d1

