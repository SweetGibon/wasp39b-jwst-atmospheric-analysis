
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# Load data
df = pd.read_csv('table_WASP-39-b-Rustamkulov-et-al.-2023.csv')

# Prepare values
wavelengths = df['CENTRALWAVELNG']
depths = df['PL_TRANDEP']
yerr_lower = df['PL_TRANDEPERR2'].abs()
yerr_upper = df['PL_TRANDEPERR1'].abs()
errors = [yerr_lower, yerr_upper]

# Define molecular absorption bands
absorption_labels = {
    "H₂O": (1.35, 1.46),
    "CO₂": (1.95, 2.1),
    "CO": (4.2, 4.6),
    "CH₄": (3.2, 3.6),
    "Na/K": (0.75, 0.9)
}

# ---------- Quantitative Analysis ----------
def mean_band_depth(wavelengths, depths, band_range):
    mask = (wavelengths >= band_range[0]) & (wavelengths <= band_range[1])
    return depths[mask].mean(), mask

def compute_band_stats():
    print("\nMolecule Detection Summary:")
    print(f"{'Molecule':<6} {'Range (µm)':<15} {'Mean Depth':<12} {'ΔDepth vs. Cont':<18} {'SNR':<6}")
    print("-" * 60)

    for mol, band in absorption_labels.items():
        mean_in_band, mask_band = mean_band_depth(wavelengths, depths, band)
        band_err = ((yerr_lower[mask_band] + yerr_upper[mask_band]) / 2).mean()
        # Continuum window: ±0.1 µm before band start (adjustable)
        cont_range = (band[0] - 0.15, band[0] - 0.05)
        mean_cont, _ = mean_band_depth(wavelengths, depths, cont_range)
        delta = mean_in_band - mean_cont
        snr = delta / band_err if band_err != 0 else 0
        print(f"{mol:<6} {f'{band[0]}–{band[1]}':<15} {mean_in_band:<12.4f} {delta:<18.4f} {snr:<6.2f}")

compute_band_stats()

# ---------- Slope Analysis ----------
mask_slope = (wavelengths >= 0.8) & (wavelengths <= 2.0)
slope, intercept, r_value, p_value, std_err = linregress(wavelengths[mask_slope], depths[mask_slope])
print(f"\nSlope of transmission spectrum (0.8–2.0 µm): {slope:.2e} per µm")

# ---------- Plot: Spectrum with Error Bars and Shaded Molecule Bands ----------
plt.figure(figsize=(14, 6))
plt.errorbar(wavelengths, depths, yerr=errors,
             fmt='o', markersize=4, capsize=3,
             color='darkslateblue', ecolor='lightgray',
             label='WASP-39 b')

# Highlight molecular absorption bands
for molecule, (start, end) in absorption_labels.items():
    plt.axvspan(start, end, color='orange', alpha=0.2)
    plt.text((start + end) / 2, max(depths)*0.98, molecule,
             horizontalalignment='center', verticalalignment='top',
             fontsize=10, color='black', rotation=90)

# Plot the fitted slope line
x_fit = np.linspace(0.8, 2.0, 100)
y_fit = slope * x_fit + intercept
plt.plot(x_fit, y_fit, '--', color='gray', alpha=0.6, label='Slope Fit (0.8–2.0 µm)')

plt.xlabel('Wavelength (μm)')
plt.ylabel('Transit Depth')
plt.title('WASP-39 b Transmission Spectrum with Molecular Bands and Slope')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('/mnt/data/wasp39b_transmission_spectrum.png')
plt.show()

# ---------- Optional Plot: SNR-Color Scatter ----------
snr = depths / ((yerr_lower + yerr_upper) / 2)

plt.figure(figsize=(14, 4))
scatter = plt.scatter(wavelengths, depths, c=snr, cmap='plasma', edgecolor='black', s=50)
plt.colorbar(scatter, label='Signal-to-Noise Ratio')
plt.title('WASP-39 b Spectrum Colored by SNR')
plt.xlabel('Wavelength (μm)')
plt.ylabel('Transit Depth')
plt.grid(True)
plt.tight_layout()
plt.savefig('/mnt/data/wasp39b_snr_colored_spectrum.png')
plt.show()
