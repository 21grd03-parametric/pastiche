<div align="center" style="margin-top:20px; margin-bottom:20px">
  <img src="pastiche_logo.svg" alt="PASTICHE: PaRaMetriC Atmospheric Spectral Tool for Irradiance Calculation using Hourly ERA5 data" width="300"/>
</div>

# PASTICHE
**P**aRaMetriC **A**tmospheric **S**pectral **T**ool for **I**rradiance **C**alculation using **H**ourly **E**RA5 data

### 📗 Table of Contents

* [📖 About the Project](#about-project)
* [🗃 Available Datasets](#available-datasets)
* [🧩 Data Structure](#data-structure)
* [🚀 Getting Started](#getting-started)
* [📚 References](#references)
* [👥 Authors](#authors)
* [📝 License](#license)
* [📜 History](#history)

---

## 📖 About the Project <a name="about-project"></a>

[PaRaMetriC](https://parametric.inrim.it/) is a metrological framework for passive radiative cooling technologies developed as a Joint Research Project within the European Partnership on Metrology Programme.

This repository contains the software used to simulate and evaluate downwelling longwave irradiance using atmospheric states derived from ERA5 reanalysis (Hersbach, 2023) and computed via RRTM_LW (Mlawer, 1997).

Fluxes are calculated over 16 contiguous longwave (infrared) spectral bands from 3–1000 μm wavelength.

ERA5 data points are defined on a regular latitude–longitude grid at 0.25° resolution and 37 fixed pressure levels.

The output fluxes are defined over the `time`, `latitude`, `longitude`, and `lw_bands` dimensions.

---

## 🗃️ Available Datasets <a name="available-datasets"></a>

> [!TIP]
> If you're unfamiliar with NetCDF format, we recommend NASA’s [Panoply](https://www.giss.nasa.gov/tools/panoply/) to explore, plot, and export the data.

### TMY

* Denver, USA – 9 points (3 lat × 3 lon), 12 months, hourly
* Las Vegas, USA – 9 points (3 lat × 3 lon), 12 months, hourly
* Madrid, Spain – 20 points (4 lat × 5 lon), 12 months, hourly
* Paris, France – 4 points (2 lat × 2 lon), 12 months, hourly
* Rome, Italy – 4 points (2 lat × 2 lon), 12 months, hourly
* Turin, Italy – 4 points (2 lat × 2 lon), 12 months, hourly
* Singapore – 9 points (3 lat × 3 lon), 12 months, hourly
* Tokyo, Japan – 9 points (3 lat × 3 lon), 12 months, hourly

### June, July, August (JJA) 2023

* Las Vegas, USA – 9 points (3 lat × 3 lon), 3 months (JJA), hourly
* Madrid, Spain – 20 points (4 lat × 5 lon), 3 months (JJA), hourly
* Riyadh, Saudi Arabia – 9 points (3 lat × 3 lon), 3 months (JJA), hourly
* Turin, Italy – 4 points (2 lat × 2 lon), 3 months (JJA), hourly

### Continental Europe

* France – 21 lat × 21 lon (5.25° × 5.25°), 2019–2023, 6-hourly
* Spain – 21 lat × 21 lon (5.25° × 5.25°), 2019–2023, 6-hourly

### Two Days over 35 Years

* Lleida, Spain – 4 points (2 lat × 2 lon), 31 July & 1 August, 1989–2023, hourly
* Sesto Fiorentino, Italy – 12 points (3 lat × 4 lon), 31 July & 1 August, 1989–2023, hourly

---

## 🧩 Data Structure <a name="data-structure"></a>

Each NetCDF4 file contains the following calculated variables:

- `sd(time, latitude, longitude, lw_bands)` – RRTM-calculated surface downward longwave radiation flux (W·m⁻²)
- `su(time, latitude, longitude, lw_bands)` – Surface upward longwave radiation flux (W·m⁻²)
- `sn(time, latitude, longitude, lw_bands)` – Surface net longwave radiation flux (W·m⁻²)
- `tu(time, latitude, longitude, lw_bands)` – TOA upward longwave radiation flux (W·m⁻²)
- `r(time, latitude, longitude)` – Relative humidity calculated from 2 m temperature and dewpoint (%)

> [!NOTE]
> - Band 0 contains total infrared flux; bands 1–16 represent spectral subdivisions.
> - Band limits are stored in `lw_band_limits` (cm⁻¹).

The following fields are copied directly from ERA5:

- `t2m` – 2 m temperature
- `skt` – Skin temperature
- `cbh` – Cloud base height
- `tcc` – Total cloud cover (as `cloud_area_fraction`)
- `tcwv` – Total column vertically integrated water vapour
- `u10`, `v10` – 10 m wind components
- `stl3`, `stl4` – Soil temperatures at levels 3 and 4
- `avg_sdlwrf`, `avg_sdlwrfcs` – Time-averaged surface downward LW radiation flux (all-sky / clear-sky)
- `avg_sdswrf`, `avg_sdswrfcs` – Time-averaged surface downward SW radiation flux
- `avg_snlwrf`, `avg_snlwrfcs` – Time-averaged surface net LW radiation flux
- `avg_snswrf`, `avg_snswrfcs` – Time-averaged surface net SW radiation flux
- `avg_tnlwrf`, `avg_tnlwrfcs` – Time-averaged TOA net LW radiation flux

> [!WARNING]
> - ERA5 fluxes are accumulated over one hour and normalized by 3600 s. We treat these as instantaneous values centered at _t – 0.5 h_.
> - ERA5 fluxes correspond to total LW radiation and should be compared to band 0 values from RRTM.
> - NaN values may appear over sea regions or where RRTM fails (e.g., north-west corner of the France dataset); further investigation is ongoing.

---

## 🚀 Getting Started <a name="getting-started"></a>

For a quick start, check out the interactive **Colab notebook**:

📓 **[RRTM_LW_ERA5_workflow.ipynb](./RRTM_LW_ERA5_workflow.ipynb)**

This notebook guides you through:

- Installing the required packages and dependencies
- Loading pre-fetched ERA5 data for the Madrid region in June (TMY)
- Running the RRTM_LW model
- Producing and plotting longwave irradiance output
- Setting your API key and prepare user-defined configurations

No local installation needed — everything runs in the cloud.

Otherwise, you can clone the repository locally with:

```bash
git clone https://github.com/21grd03-parametric/pastiche.git
cd pastiche
```

And run a full simulation from a configuration file with:

```bash
python3 main_parallel.py config_file.json
```

---

## 📚 References <a name="references"></a>

- Mlawer et al. (1997). *Radiative transfer for inhomogeneous atmospheres: RRTM, a validated correlated-k model for the longwave*. DOI: [10.1029/97JD00237](https://doi.org/10.1029/97JD00237)
- Hersbach et al. (2023). *ERA5 hourly data on single levels and pressure levels from 1940 to present*, Climate Data Store. DOIs: [cds.adbb2d47](https://doi.org/10.24381/cds.adbb2d47), [cds.bd0915c6](https://doi.org/10.24381/cds.bd0915c6)
- Beck et al. (2023). *High-resolution Köppen-Geiger maps for 1901–2099 based on constrained CMIP6 projections*. Scientific Data 10, 724.

---

<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

👤 **Claudio Belotti**

* 📧: [claudio.belotti@cnr.it](mailto:claudio.belotti@cnr.it)

👤 **Lorenzo Pattelli**

* 📧: [l.pattelli@inrim.it](mailto:l.pattelli@inrim.it)

---

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
