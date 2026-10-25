"""Plot the published WASP-39 b spectrum with illustrative reference feature locations.

Molecular identifications are from Rustamkulov et al. (2023), not calculated
from a model/retrieval here. This figure alone does not demonstrate detection.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'data' / 'table_WASP-39-b-Rustamkulov-et-al.-2023.csv'
OUT = ROOT / 'figures' / 'wasp39b_reference_features.png'
OUT.parent.mkdir(exist_ok=True)

df = pd.read_csv(DATA).sort_values('CENTRALWAVELNG')
x = df['CENTRALWAVELNG']
y = df['PL_TRANDEP']
errors = [df['PL_TRANDEPERR2'].abs(), df['PL_TRANDEPERR1'].abs()]

# Approximate guides to regions discussed in the reference paper; these are not
# spectral-model fits, abundance estimates, or independent detections.
features = [
    ('Na near 0.58 µm', 0.56, 0.61, '#86b8aa'),
    ('H₂O near 1.4 µm', 1.35, 1.50, '#b6a5d8'),
    ('CH₄ near 3.3 µm (not detected)', 3.23, 3.38, '#c5c5c5'),
    ('SO₂ near 4.05 µm (tentative)', 3.99, 4.12, '#b8c7e8'),
    ('CO₂ near 4.3 µm', 4.22, 4.45, '#efc18b'),
    ('CO near 4.7 µm', 4.64, 4.83, '#cf9da8'),
]
fig, ax = plt.subplots(figsize=(11.8, 6.0), dpi=160)
for name, lo, hi, color in features:
    ax.axvspan(lo, hi, color=color, alpha=.35, lw=0)
ax.errorbar(x, y, yerr=errors, fmt='.', markersize=4.8,
            color='#22385b', ecolor='#b7bfd0', capsize=1.5, lw=.8)
ax.set(xlabel='Wavelength (µm)', ylabel='Transit depth (%)',
       title='WASP-39 b · JWST NIRSpec PRISM transmission spectrum')
ax.set_xlim(.48, 5.58)
ax.grid(alpha=.2)
ax.spines[['top','right']].set_visible(False)
ax.legend(handles=[Patch(facecolor=c,alpha=.55,label=n) for n,lo,hi,c in features],
          loc='upper center', bbox_to_anchor=(.5,-.14), ncol=2,
          frameon=False, fontsize=9)
fig.subplots_adjust(bottom=.3,top=.91,left=.10,right=.98)
fig.text(.01,.01,'Feature labels follow Rustamkulov et al. (2023); bands are illustrative, not a retrieval.',
         size=8.5,color='#4f5360')
fig.savefig(OUT, dpi=160, bbox_inches='tight')
plt.close(fig)
print('Saved', OUT)
