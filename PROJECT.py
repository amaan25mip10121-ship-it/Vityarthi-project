import numpy as np

def analyze_heart_rate(readings):
    readings = np.array(readings)

    avg_hr = np.mean(readings)
    max_hr = np.max(readings)
    min_hr = np.min(readings)
    sdnn = np.std(readings) 
    
    status = ""
    if avg_hr > 100:
        status = "Tachycardia (High Heart Rate)"
    elif avg_hr < 60:
        status = "Bradycardia (Low Heart Rate)"
    else:
        status = "Normal Heart Rate Range"


    diffs = np.abs(np.diff(readings))
    abnormal_jumps = np.where(diffs > 20)[0]

    print("=== HEART RATE ANALYSIS REPORT ===")
    print(f"Total Readings: {len(readings)}")
    print(f"Average HR: {avg_hr:.2f} bpm")
    print(f"Max HR: {max_hr} bpm")
    print(f"Min HR: {min_hr} bpm")
    print(f"Heart Rate Variability (SDNN): {sdnn:.2f}")
    print(f"Overall Status: {status}")
    print("----------------------------------")

    if len(abnormal_jumps) > 0:
        print("⚠️ Abnormal jumps detected at indices:", abnormal_jumps)
    else:
        print("No abnormal jumps in the readings.")

    print("==================================")
