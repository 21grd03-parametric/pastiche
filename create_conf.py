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


create_conf.py
"""

import json
import calendar


ALL_HOURS = [f"{x:02d}:00" for x in range(24)]
SYNOPTIC_HOURS = [f"{x:02d}:00" for x in (0, 6, 12, 18)]

cities = [
    {
        "label": "mytest_1",
        "area": [
            40.75,
            -4.0,
            40.0,
            -3,
        ],
        "TMY": [2015, 2014, 2009, 2020, 2023, 2022, 2008, 2009, 2016, 2013, 2023, 2015],
    },
    {
        "label": "mytest_2",
        "area": [
            42.0,
            12.25,
            41.75,
            12.5,
        ],
        "TMY": [2018, 2018, 2017, 2005, 2005, 2014, 2018, 2022, 2023, 2005, 2018, 2018],
    },
]

for city in cities:
    city.update({"hours": ALL_HOURS})
    if "TMY" in city:
        tmy_dates = []
        for mm in range(1, 13):
            # use 2025 as TMY February has always 28 days
            _, days_in_month = calendar.monthrange(2025, mm)
            tmy_dates += [
                f"{city['TMY'][mm - 1]}{mm:02d}{dd:02d}"
                for dd in range(1, days_in_month + 1)
            ]
        city.update({"dates": tmy_dates})
        json.dump(city, open(f"./config/tmy_{city['label']}.json", "w"))
    else:
        city.update({"dates": dates})
        json.dump(city, open(f"./config/{city['label']}.json", "w"))
