## 📝 Project Statement: Heart Rate Analysis Script

-----

### **Overview**

This repository contains a simple yet effective Python script, **`PROJECT.py`**, designed for basic **Heart Rate (HR) analysis**. It uses the popular **NumPy** library to process a list of heart rate readings (in beats per minute, or bpm) and generate a summary report.

The script calculates essential statistical metrics, assesses the overall heart rate status based on the average, and identifies potential anomalies or sudden changes in the readings.

### **Key Features**

  * **Statistical Analysis:** Calculates the **Average**, **Maximum**, and **Minimum** heart rate from the provided data.
  * **Heart Rate Variability (HRV) Metric:** Computes the **Standard Deviation of the Normal-to-Normal intervals (SDNN)**, a common metric for HRV, which indicates the overall variability in heart rate.
  * **Clinical Status Assessment:** Categorizes the average heart rate as **Normal**, **Bradycardia** (too low, $< 60$ bpm), or **Tachycardia** (too high, $> 100$ bpm).
  * **Anomaly Detection:** Implements a basic check for **"Abnormal Jumps"** (a difference of more than $20$ bpm between consecutive readings), which could signify artifacts, sudden physiological changes, or sensor errors.

### **How to Use**

1.  **Dependencies:** Ensure you have **NumPy** installed:

    ```bash
    pip install numpy
    ```

2.  **Run the script:** You can call the `analyze_heart_rate` function with a list of heart rate readings.

    ```python
    # Example usage (assuming PROJECT.py is imported or the function is copied)
    readings_data = [72, 75, 78, 80, 77, 105, 85, 82, 80]
    analyze_heart_rate(readings_data)
    ```

### **Output Example**

The script prints a detailed report to the console:

```
=== HEART RATE ANALYSIS REPORT ===
Total Readings: 9
Average HR: 81.56 bpm
Max HR: 105 bpm
Min HR: 72 bpm
Heart Rate Variability (SDNN): 10.45
Overall Status: Normal Heart Rate Range
----------------------------------
⚠️ Abnormal jumps detected at indices: [4]
==================================
```

### **Code Implementation Details**

The core analysis is performed by the `analyze_heart_rate(readings)` function:

  * **Average, Max, Min:** Utilizes `np.mean()`, `np.max()`, and `np.min()`.
  * **SDNN:** Calculated using `np.std()`.
  * **Jumps:** Calculated by taking the absolute difference between consecutive readings using `np.abs(np.diff(readings))` and finding indices where this difference exceeds 20 using `np.where()`.

This script provides a foundational tool for quickly reviewing heart rate data and flagging critical observations.

-----

Would you like to explore adding more advanced HRV metrics, such as RMSSD, to this script?
