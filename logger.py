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


logger.py
"""

# see https://python-bloggers.com/2024/04/logging-like-a-lumberjack/
import logging
from logging import debug, info, warning, error
from datetime import datetime

FMT_MESSAGE = "%(asctime)s [wp2 %(levelname)7s] %(message)s"
FMT_DATETIME = "%Y-%m-%d %H:%M:%S"

# Get default logger.
logger = logging.getLogger()

# Set logging level.
logger.setLevel(logging.INFO)

formatter = logging.Formatter(FMT_MESSAGE, datefmt=FMT_DATETIME)

# Logging to console.
console = logging.StreamHandler()
console.setFormatter(formatter)
logger.addHandler(console)

# Logging to file.
#
file = logging.FileHandler(datetime.now().strftime("wp2_%Y%m%d-%H%M%S.log"))
file.setFormatter(formatter)
logger.addHandler(file)
