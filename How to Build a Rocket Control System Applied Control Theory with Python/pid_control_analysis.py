import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Step 1: Define the Transfer Function of the System
zeta = 0.7  # Damping ratio
omega_n = 1  # Natural frequency (rad/s)
numerator = [omega_n**2]
denominator = [1, 2*zeta*omega_n, omega_n**2]
system = ctrl.TransferFunction(numerator, denominator)

# Step 2: Use Ziegler-Nichols Rules to Find Initial PID Parameters
Ku = 5.0  # Ultimate gain (experimentally determined)
Pu = 2.0  # Oscillation period (experimentally determined)

# Ziegler-Nichols PID parameters
Kp = 0.6 * Ku
Ti = Pu / 2
Td = Pu / 8

Ki = Kp / Ti
Kd = Kp * Td

# Define the PID controller transfer function
pid_controller = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])

# Closed-loop system
closed_loop_system = ctrl.feedback(pid_controller * system, 1)


# Step 3: Root Locus for Gain Analysis
plt.figure()
ctrl.root_locus(system)
plt.title("Root Locus of the System")
plt.grid()

# Step 4: Bode Plot for Stability Analysis
plt.figure()
ctrl.bode_plot(closed_loop_system, dB=True)
plt.title("Bode Plot of the Closed-Loop System")
plt.grid()

# Customizing the x-axis
ax_mag, ax_phase = plt.gcf().axes

# Set more x-ticks for magnitude plot
ax_mag.set_xticks(np.logspace(-2, 2, num=20))  # Add more x-axis ticks on a log scale
ax_mag.get_xaxis().set_major_formatter(plt.ScalarFormatter())  # Use scalar formatting for better readability

# Set more x-ticks for phase plot
ax_phase.set_xticks(np.logspace(-2, 2, num=20))  # Add more x-axis ticks on a log scale
ax_phase.get_xaxis().set_major_formatter(plt.ScalarFormatter())  # Use scalar formatting for better readability

# Step 5: Nyquist Plot for Stability Analysis
plt.figure()
ctrl.nyquist_plot(closed_loop_system)
plt.title("Nyquist Plot of the Closed-Loop System")
plt.grid()



# Show plots
plt.show()

# Iterative process to adjust gains based on analysis and repeat steps
# Here you would analyze the plots and adjust Kp, Ki, Kd accordingly
