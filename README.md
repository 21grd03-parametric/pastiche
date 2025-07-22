# PASTICHE
## The PaRaMetriC Atmospheric Spectral Tool for Irradiance Calculation using Hourly ERA5 data.

# 📗 Table of Contents

* [📖 About the Project](#about-project) 
  * [🗃 Available Datasets](#available-datasets)
  * [🧩 Data Structure](#datastructure)
  * [⚠ Use Note and Warning](#use-note-and-warning)
  * [📚 References](#references)
* [💻 Getting Started](#getting-started)
* [👥 Authors](#authors)
* [🔭 Future Features](#future-features)
* [❓ FAQ (OPTIONAL)](#faq)
* [📝 License](#license)
* [📜 History](#history)

<!-- PROJECT DESCRIPTION -->

# 📖 PaRaMetriC <a name="about-project"></a>

[PaRaMetriC](https://parametric.inrim.it/) a Metrological framework for passive radiative cooling technologies. A Joint Research Project within the European Partnership on Metrology Programme.

This is the software used to **...**

The long-wave radiation fluxes were calculated using RRM (Mlawer, 1997) using atmospheric states derived from ERA5 reanalysis (Hersbach, 2023).

RRTM calculates fluxes along the vertical dimension on 16 contiguous bands in the longwave (infrared) from 3 to 1000 μm in wavelength.

ERA 5 data points are defined on a regular lat/lon grid with resolution of 0.25° and over 37 fixed pressure level points.

The calculated fluxes therefore, are defined over the (time, latitude, longitude, lw_bands) dimensions.

## 🗃️ Available Datasets <a name="available-datasets"></a>

**Note:** if you are not familiar with netCDF format a good starting point is to download NASA's [Panoply](https://www.giss.nasa.gov/tools/panoply/) to explore, plot and export the data.

### TMY

* Denver, U.S.A. 9 data points (i.e. 3 lats x 3 lons), TMY (12 months), hourly
* Las Vegas, U.S.A. 9 data points (i.e. 3 lats x 3 lons), TMY (12 months), hourly
* Madrid, Spain 20 data points (i.e. 4 lats x 5 lons), TMY (12 months), hourly
* Paris, France 4 data points (i.e. 2 lats x 2 lons), TMY (12 months), hourly
* Rome, Italy 4 data points (i.e. 2 lats x 2 lons), TMY (12 months), hourly
* Turin, Italy 4 data points (i.e. 2 lats x 2 lons), TMY (12 months), hourly
* Singapore 9 data points (i.e. 3 lats x 3 lons), TMY (12 months), hourly
* Tokyo, Japan tbc, 12 months, , TMY (12 months), hourly

### June, July, August (JJA) 2023

* Las Vegas, U.S.A. 9 data points (i.e. 3 lats x 3 lons), JJA 2023 (3 months), hourly
* Madrid, Spain 20 data points (i.e. 4 lats x 5 lons), JJA 2023 (3 months), hourly
* Riyadh, Saudi Arabia 9 data points (i.e. 3 lats x 3 lons), JJA 2023 (3 months), hourly
* Turin, Italy 4 data points (i.e. 2 lats x 2 lons), JJA 2023 (3 months), hourly

### Continental Europe

* France, 21 lats x 21 lons (5.25° × 5.25°), 2019--2023 (60 months),  6-hourly
* Spain, 21 lats x 21 lons (5.25° × 5.25°), 2019--2023 (60 months),  6-hourly

### 2 days over 35 years

* Lleida, Spain 4 data points (i.e. 2 lats x 2 lons), 31 July and 1 Aug 1989–2023 (70 days), hourly
* Sesto Fiorentino, Italy 12 data points (i.e. 3 lats x 4 lons), 31 July and 1 Aug 1989–2023 (70 days), hourly

## 🧩 Data Structure <a name="datastructure"></a>

Each netCDF4 file contains the following calculated variables:

* sd(time, latitude, longitude, lw_bands),  "RRTM-calculated surface downward long-wave radiation flux", sd:units = "Wm$^{-2}$";
* su(time, latitude, longitude, lw_bands), "RRTM-calculated surface upward long-wave radiation flux", su:units = "Wm$^{-2}$";
* sn(time, latitude, longitude, lw_bands), "RRTM-calculated surface net long-wave radiation flux", sn:units = "Wm$^{-2}$";
* tu(time, latitude, longitude, lw_bands), "RRTM-calculated TOA upward long-wave radiation flux", tu:units = "Wm$^{-2}$";
* r (time, latitude, longitude);  "Relative humidity calculated from 2m-temperature and 2m-dewpoint temperature", r:units = "%";

**Note:** fluxes are given overt the whole infrared and the 16 bands, the band limits are defined in the variable "lw_band_limits" the m.u. is cm$^{-1}$ (i.e. the inverse of the wavelength).

The following variables are copied from ERA5 fields:

* t2m(time, latitude, longitude) "2 metre temperature";
* skt(time, latitude, longitude) "Skin temperature";
* cbh(time, latitude, longitude) "Cloud base height";
* tcc(time, latitude, longitude) "cloud_area_fraction";
* tcwv(time, latitude, longitude) "Total column vertically-integrated water vapour";
* u10(time, latitude, longitude) "10 metre U wind component";
* v10(time, latitude, longitude) "10 metre V wind component";
* stl3(time, latitude, longitude) "Soil temperature level 3";
* stl4(time, latitude, longitude) "Soil temperature level 4";
* avg_sdlwrf(time, latitude, longitude) "Time-mean surface downward long-wave radiation flux";
* avg_sdlwrfcs(time, latitude, longitude) "Time-mean surface downward long-wave radiation flux, clear sky";
* avg_sdswrf(time, latitude, longitude) "Time-mean surface downward short-wave radiation flux";
* avg_sdswrfcs(time, latitude, longitude) "Time-mean surface downward short-wave radiation flux, clear sky";
* avg_snlwrf(time, latitude, longitude) "Time-mean surface net long-wave radiation flux";
* avg_snlwrfcs(time, latitude, longitude) "Time-mean surface net long-wave radiation flux, clear sky";
* avg_snswrf(time, latitude, longitude) "Time-mean surface net short-wave radiation flux";
* avg_snswrfcs(time, latitude, longitude) "Time-mean surface net short-wave radiation flux, clear sky";
* avg_tnlwrf(time, latitude, longitude) "Time-mean top net long-wave radiation flux";
* avg_tnlwrfcs(time, latitude, longitude) "Time-mean top net long-wave radiation flux, clear sky"

## ⚠ Use Note and Warning <a name="use-note-and-warning"></a>

1. ERA5 fluxes are accumulated over one hour (and then divided by 3600s), we assume them as representative of the instantaneous value at time t-0.5h (e.g. flux at 06:00 is representative of flux at 05:30).
2. ERA5 fluxes should be compared with RRTM band 0 values (i.e. total infrared).
3. NaN values: some values are NaN this is the case for pixels on the sea (e.g. north-west corner of the France dataset) but unfortunately there are also few cases where RRTM fails: I'm still investigating the reason for that.

## 📚 References <a name="references"></a>

* Mlawer, E. J., Taubman, S. J., Brown, P. D., Iacono, M. J., Clough, S. A., Radiative transfer for inhomogeneous atmospheres: RRTM, a validated correlated-k model for the longwave, Journal of Geophysical Research: Atmospheres 102 (D14) (1997) 16663–16682, . DOI:10.1029/97JD00237.
* Hersbach, H., Bell, B., Berrisford, P., Biavati, G., Horányi, A., Muñoz Sabater, J., Nicolas, J., Peubey, C., Radu, R., Rozum, I., Schepers, D., Simmons, A., Soci, C., Dee, D., Thépaut, J-N. (2023): ERA5 hourly data on single levels from 1940 to present. Copernicus Climate Change Service (C3S) Climate Data Store (CDS), DOI: 10.24381/cds.adbb2d47 (Accessed on 2023 and 2024); ERA5 hourly data on pressure levels from 1940 to present. Copernicus Climate Change Service (C3S) Climate Data Store (CDS), DOI: 10.24381/cds.bd0915c6 (Accessed on 2023 and 2024)
* Beck, H. E., T. R. McVicar, N. Vergopolan, A. Berg, N. J. Lutsko, A. Dufour, Z. Zeng, X. Jiang, A. I. J. M. van Dijk, and D. G. Miralles. High-resolution (1 km) Köppen-Geiger maps for 1901–2099 based on constrained CMIP6 projections, Scientific Data 10, 724 (2023)

<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>

To get a local copy up and running, follow these steps.

```
git clone https://github.com/21grd03-parametric/pastiche.git
```

### Usage

```
python3 main_parallel.py config_file.json
```

* 
* 
* 

<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

👤 **Claudio Belotti**

* 📧: [claudio.belotti@cnr.it](mailto:claudio.belotti@cnr.it)

👤 **Lorenzo Pattelli**

* 📧: [l.pattelli@inrim.it](mailto:l.pattelli@inrim.it)

<!-- FUTURE FEATURES -->

## 🔭 Future Features <a name="future-features"></a>

> Describe 1 - 3 features you will add to the project.

* [ ] **[new_feature_1]**
* [ ] **[new_feature_2]**
* [ ] **[new_feature_3]**

<!-- FAQ (optional) -->

## ❓ FAQ (OPTIONAL) <a name="faq"></a>

> Add at least 2 questions new developers would ask when they decide to use your project.

* **[Question_1]** 
  * [Answer_1]
* **[Question_2]** 
  * [Answer_2]

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [GPL-3.0](./LICENSE) licensed.

<!-- HISTORY -->

## 📜 History <a name="history"></a>

### V0

* initial data release to INRIM and University of Lleida, datasets:

### V0.1

* added relative humidity at 2m above surface, calculated from ERA5 2m temperature and 2m dewpoint temperature.
* added ERA5 total cloud cover.
