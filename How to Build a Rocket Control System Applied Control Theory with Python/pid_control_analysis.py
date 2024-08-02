# Step 1: Import libraries
import matplotlib.pyplot as plt
import control as ctrl

# Step 2: Define a new rocket transfer function with poles closer to the imaginary axis
num = [10] 
den = [2, 2, 1] 
G = ctrl.TransferFunction(num, den)

# Step 3: Design a PID controller with new parameters
Kp = 5
Ki = 2
Kd = 1
C = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])

# Step 4: Applying the PID controller to the rocket transfer function
CL = ctrl.feedback(C * G, 1)

# Step 5: Plot Root Locus for Closed-Loop System
plt.figure(figsize=(10, 6))
ctrl.root_locus(C * G, grid=True)
plt.title("Root Locus Plot (Closed-Loop)")

# Step 6: Plot Bode Plot for Closed-Loop System
plt.figure(figsize=(10, 6))
ctrl.bode_plot(CL, dB=True, Hz=False, deg=True)
plt.suptitle("Bode Plot (Closed-Loop)", fontsize=16)

# Step 7: Plot Nyquist Plot for Closed-Loop System
plt.figure(figsize=(10, 6))
ctrl.nyquist_plot(CL)
plt.title("Nyquist Plot (Closed-Loop)")

plt.show()
