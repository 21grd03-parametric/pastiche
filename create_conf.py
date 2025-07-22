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


create_conf.py
"""

import json
import calendar


ALL_HOURS = [f"{x:02d}:00" for x in range(24)]
SYNOPTIC_HOURS = [f"{x:02d}:00" for x in (0, 6, 12, 18)]

areas = [
    {
        "label": "sf",
        "area": [
            44,
            10.75,
            43.5,
            11.5,
        ],
    },  # Sesto F.no
    {
        "label": "ll",
        "area": [
            41.75,
            0.5,
            41.5,
            0.75,
        ],
    },  # Lleida
    {
        "label": "fr",
        "area": [
            50.0,
            0.0,
            45.0,
            5.0,
        ],
    },  # France
    {
        "label": "sp",
        "area": [
            43.0,
            -6.0,
            38.0,
            -1.0,
        ],
    },  # Spain
    {
        "label": "sp",
        "area": [
            43.0,
            -6.0,
            38.0,
            -1.0,
        ],
    },  # Spain
    {
        "label": "wg",
        "area": [
            55.0,
            5.0,
            50.0,
            10.0,
        ],
    },  # West Germany
    {
        "label": "eg",
        "area": [
            55.0,
            10.0,
            50.0,
            15.0,
        ],
    },  # East Germany
]

dates = [f"{yyyy}{mm:02d}01" for yyyy in range(2019, 2024) for mm in range(1, 12)]

# for area in areas:
#     area.update({'dates': dates})
#     area.update({'hours': SYNOPTIC_HOURS})
#     json.dump(area, open(f"./config/{area['label']}.json", 'w'))

# PoliTo
polito = [
    {
        "label": "denver",
        "area": [40, -105.25, 39.5, -104.75],
        "TMY": [2022, 2019, 2010, 2009, 2013, 2014, 2023, 2023, 2023, 2016, 2007, 2011],
    },
    {
        "label": "las_vegas",
        "area": [
            36.25,
            -115.5,
            35.75,
            -115.0,
        ],
        "TMY": [2012, 2023, 2018, 2014, 2008, 2010, 2018, 2015, 2011, 2015, 2006, 2018],
    },
    {
        "label": "madrid",
        "area": [
            40.75,
            -4.0,
            40.0,
            -3,
        ],
        "TMY": [2015, 2014, 2009, 2020, 2023, 2022, 2008, 2009, 2016, 2013, 2023, 2015],
    },
    {
        "label": "riyadh",
        "area": [
            25.0,
            46.5,
            24.5,
            47.0,
        ],
    },
    {
        "label": "singapore",
        "area": [1.5, 103.5, 1.0, 104.0],
        "TMY": [2006, 2023, 2017, 2014, 2013, 2014, 2013, 2007, 2013, 2009, 2009, 2023],
    },
    {
        "label": "tokyo",
        "area": [36.0, 139.5, 35.5, 140],
        "TMY": [2017, 2020, 2007, 2019, 2021, 2018, 2017, 2020, 2007, 2014, 2014, 2013],
    },
    {
        "label": "torino",
        "area": [
            45.25,
            7.5,
            45.0,
            7.75,
        ],
        "TMY": [2016, 2016, 2018, 2018, 2011, 2012, 2006, 2012, 2007, 2005, 2007, 2013],
    },
    {
        "label": "roma",
        "area": [
            42.0,
            12.25,
            41.75,
            12.5,
        ],
        "TMY": [2018, 2018, 2017, 2005, 2005, 2014, 2018, 2022, 2023, 2005, 2018, 2018],
    },
    {
        "label": "paris",
        "area": [
            49.0,
            2.25,
            48.75,
            2.5,
        ],
        "TMY": [2015, 2020, 2019, 2009, 2009, 2015, 2012, 2017, 2007, 2018, 2016, 2005],
    },
]

dates = [f"202306{dd:02d}" for dd in range(1, 31)]
dates += [f"2023{mm:02d}{dd:02d}" for mm in range(7, 9) for dd in range(1, 32)]

for city in polito:
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
