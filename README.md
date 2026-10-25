# Atmospheric Analysis of WASP-39 b Using JWST Transmission Spectra

## Project Overview

This project examines the atmosphere of WASP-39 b, a hot gas-giant exoplanet, using publicly available James Webb Space Telescope (JWST) NIRSpec PRISM transmission-spectrum data. During a transit, some starlight passes through the planet's atmosphere. Different atmospheric constituents absorb different wavelengths, producing features in the measured transit depth. The analysis explores those patterns through Python-based visualization, wavelength-band comparisons, and basic statistical measurements.

## Methods and Tools

The analysis uses **Python**, **pandas**, **NumPy**, **SciPy**, and **Matplotlib** to:

- Load the published spectrum (207 wavelength measurements), including transit depths and measurement uncertainties.
- Plot the transmission spectrum with error bars and highlight selected molecular absorption windows.
- Compare average transit depth in each selected window with a nearby continuum region to examine relative spectral features.
- Calculate exploratory depth-to-uncertainty ratios and fit a linear spectral slope over 0.8–2.0 µm.
- Generate reproducible figures; a separate reference plot marks molecular features identified in the published research.

The main input is `data/table_WASP-39-b-Rustamkulov-et-al.-2023.csv`. Additional NASA Exoplanet Archive and MAST catalog records are supplied as reference metadata, not used to calculate the spectrum.

## Findings and Interpretation

The spectrum contains noticeable wavelength-dependent variations, particularly in the infrared. The published JWST analysis identifies **water vapor (H₂O), carbon dioxide (CO₂), carbon monoxide (CO), and sodium (Na)**, with a possible **sulfur dioxide (SO₂)** signature and no significant methane (CH₄) detection. In particular, the prominent feature around 4.3 µm is attributed to CO₂, while CO is identified nearer 4.7 µm.

The original code is an exploratory band-window analysis, not a full atmospheric retrieval. Its selected windows and simplified signal-to-noise calculations should not be interpreted as formal molecular-detection significances. Molecular assignments above come from the cited peer-reviewed study, not from independent model fitting in this repository.

## Real-World Applications

- Atmospheric characterization: Transmission spectroscopy helps determine which molecules may be present in distant planetary atmospheres and provides constraints for atmospheric models.
- Planet formation and chemistry: Comparing carbon-bearing molecules, water, and possible photochemical products can improve understanding of planetary composition, temperature-dependent chemistry, and formation histories.
- Future exoplanet research: Data visualization and uncertainty-aware spectral analysis are building blocks for more advanced atmospheric-retrieval workflows, including studies of smaller planets and potentially habitable environments. WASP-39 b itself is not considered habitable.

## Sources and Citations

1. **Primary spectral dataset and interpretation:** Rustamkulov, Z., Sing, D. K., Mukherjee, S., et al. (2023). [*Early Release Science of the exoplanet WASP-39b with JWST NIRSpec PRISM*](https://doi.org/10.1038/s41586-022-05677-y). *Nature*, **614**, 659–663.
2. **Spectrum download:** [NASA Exoplanet Archive — Exoplanet Atmospheres](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/atmospheres/nph-firefly?atmospheres), operated by Caltech/IPAC.
3. **Observation and planetary metadata:** [MAST — Barbara A. Mikulski Archive for Space Telescopes](https://archive.stsci.edu/) and [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/).
4. **Transmission-spectroscopy explanation:** [NASA Science — WASP-39 b NIRSpec transmission spectrum](https://science.nasa.gov/asset/webb/exoplanet-wasp-39-b-nirspec-transmission-spectrum/).

The **JWST observations and source data are credited to their original research team and archives**; the Python analysis and project presentation are independent work.
