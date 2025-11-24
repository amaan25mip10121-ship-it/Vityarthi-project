Heart Rate Analysis Tool - README

Overview

This project analyzes heart rate (HR) readings and provides a detailed
report, including: - Average heart rate
- Maximum and minimum heart rate
- Heart Rate Variability (SDNN)
- Basic HR classification (Normal, Tachycardia, Bradycardia)
- Detection of abnormal sudden jumps between consecutive readings

The script is intended for simple HR data insights and can be used in
health analytics, wearable device data processing, or personal
monitoring.


Features

1. Statistical Analysis

-   Average HR
-   Max HR
-   Min HR
-   SDNN (Standard Deviation of NN intervals): Basic heart rate
    variability metric.

2. Heart Rate Status Classification

Based on average HR: - > 100 bpm → Tachycardia
- < 60 bpm → Bradycardia
- 60–100 bpm → Normal

3. Abnormal Jump Detection

Flags sudden changes of more than 20 bpm between consecutive readings.


Usage

Function:

    analyze_heart_rate(readings)

Parameters:

-   readings: A list or array of heart rate values (integers or floats).

Example:

    data = [72, 75, 78, 110, 76, 75]
    analyze_heart_rate(data)


Output

The function prints a structured report:

    === HEART RATE ANALYSIS REPORT ===
    Total Readings: X
    Average HR: XX.XX bpm
    Max HR: XX bpm
    Min HR: XX bpm
    Heart Rate Variability (SDNN): XX.XX
    Overall Status: Normal / Tachycardia / Bradycardia
    ----------------------------------
    ⚠️ Abnormal jumps detected at indices: [...]
    ==================================

Notes

-   SDNN here uses population standard deviation (np.std), not
    clinically accurate SDNN (usually sample SD).
-   This script is not a medical diagnostic tool.
-   Sudden jumps may indicate sensor glitches or real physiological
    changes.

Requirements

-   Python 3.x
-   NumPy library

Install NumPy using:

    pip install numpy

# Vityarthi-project
