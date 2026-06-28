# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 18:33:16 2026

@author: samasiedu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline  # Added for the smooth spline curve

file_path = "D:/GEOTECH/ML/Python/compaction.xlsx" # replace with your file path
df = pd.read_excel(file_path)

moisture_content = df['Moisture Content'].to_numpy()
dry_density = df['Dry Density'].to_numpy()


# This creates a localized smooth curve passing through every single data point
cs = CubicSpline(moisture_content, dry_density)

# Generate a high-density smooth curve (1000 points for precise peak detection)
x_smooth = np.linspace(min(moisture_content), max(moisture_content), 1000)
y_smooth = cs(x_smooth)


# We locate the index of the highest point along our generated smooth curve
idx_max = np.argmax(y_smooth)
omc = x_smooth[idx_max]
mdd = y_smooth[idx_max]

## Plot Compaction Curve 
plt.figure(figsize=(8,6))
plt.scatter(moisture_content, dry_density, color='black', label='Lab Data', zorder=5)
plt.plot(x_smooth, y_smooth, 'r-', label='Cubic Spline Fit')

# Mark MDD & OMC
plt.scatter(omc, mdd, color='green', s=100, zorder=6,
            label=f'MDD={mdd:.2f}, OMC={omc:.2f}')
plt.axvline(x=omc, linestyle='--', color='gray', alpha=0.7)
plt.axhline(y=mdd, linestyle='--', color='gray', alpha=0.7)

# Formatting
plt.title("Compaction Curve")
plt.xlabel("Moisture Content (%)")
plt.ylabel("Dry Density (g/cc or kg/m³)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig("compactionCurve.png", dpi=300, bbox_inches='tight')

plt.show()
