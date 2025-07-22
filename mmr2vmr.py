"""
Copyright (C) 2025
Claudio Belotti (CNR-INO, Italy), claudio.belotti@cnr.it
Lorenzo Pattelli (INRiM, Italy), l.pattelli@inrim.it


    This file is part of PASTICHE:
    the PaRaMetriC Atmospheric Spectral Tool for Irradiance Calculation using Hourly ERA5 data.

    PASTICHE is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    PASTICHE is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with PASTICHE.  If not, see <http://www.gnu.org/licenses/>.


mmr2vmr.py
"""


def mmr2vmr(MMR, species):
    '''
    Calcola il volume mixing ratio in ppm 
    a partire dal mass mixing ratio.
    
    '''
    species = species.lower()
    molar_mass = {
        'o3': 47.9982,
        'h2o': 18.0153 }
    md = 28.9644
    vmr = MMR * md / molar_mass[species]
    return vmr * 1e+06

