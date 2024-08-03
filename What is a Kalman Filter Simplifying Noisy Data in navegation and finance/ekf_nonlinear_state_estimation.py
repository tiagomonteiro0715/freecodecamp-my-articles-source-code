import numpy as np
from filterpy.kalman import ExtendedKalmanFilter as EKF
from filterpy.common import Q_discrete_white_noise

def fx(x, dt):
    """ State transition function for the nonlinear system. """
    # Example: x' = [x[0] + x[1]*dt, x[1]]
    return np.array([x[0] + x[1]*dt, x[1]])

def hx(x):
    """ Measurement function for the nonlinear system. """
    # Example: z = [x[0]]
    return np.array([x[0]])

def jacobian_F(x, dt):
    """ Jacobian of the state transition function. """
    return np.array([[1, dt],
                     [0, 1]])

def jacobian_H(x):
    """ Jacobian of the measurement function. """
    return np.array([[1, 0]])

# Initialize EKF
ekf = EKF(dim_x=2, dim_z=1)

# Initial state
ekf.x = np.array([0, 1])
print("Initial state:", ekf.x)

# Initial state covariance
ekf.P = np.eye(2)
print("Initial state covariance:\n", ekf.P)

# Process noise covariance
ekf.Q = Q_discrete_white_noise(dim=2, dt=1, var=0.1)
print("Process noise covariance:\n", ekf.Q)

# Measurement noise covariance
ekf.R = np.array([[0.1]])
print("Measurement noise covariance:\n", ekf.R)

# Control input
dt = 1.0  # time step

# Simulated measurements
measurements = [1, 2, 3, 4, 5]

# True initial state for comparison (not used in the EKF)
true_state = np.array([0, 1])
print("\nTrue initial state:", true_state)

# Simulate the true state evolution (for comparison)
true_states = [true_state[0]]
for _ in range(len(measurements) - 1):
    true_state = fx(true_state, dt)
    true_states.append(true_state[0])

print("\nSimulated true states (for reference):", true_states)

for i, z in enumerate(measurements):
    print(f"\nStep {i+1}:")
    print("Measurement:", z)

    # Predict step
    ekf.predict(u=0)  # Use predict_x if you need to customize the prediction
    print("Predicted state before update:", ekf.x)

    # Update step
    ekf.update(z, HJacobian=jacobian_H, Hx=hx, args=(), hx_args=())
    print("Updated state after measurement:", ekf.x)
    print("State covariance after update:\n", ekf.P)
