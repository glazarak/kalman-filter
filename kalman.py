import matplotlib.pyplot as plt
import numpy as np

dt = 0.1
steps = 200
target = 10.0
position = 0.0
velocity = 0.0
Kp = 2.0
Kd = 1.5
velocity_error = 0.1
Q = 0.01
R = 1.0
Ks = np.zeros(steps)

times = np.zeros(steps)
true_positions = np.zeros(steps)
measurements = np.zeros(steps)
predictions = np.zeros(steps)
estimates = np.zeros(steps)
estimate = 0.0
P = 1.0
Ps = np.zeros(steps)

for i in range(steps):
    error = target - position
    acceleration = Kp * error - Kd * velocity
    velocity += acceleration * dt
    position += velocity * dt
    times[i] = i * dt
    true_positions[i] = position
    measurement = position + np.random.normal(0, 1)
    measurements[i] = measurement
    sensed_velocity = velocity + velocity_error
    prediction = estimate + sensed_velocity * dt
    P = P + Q
    K = P / (P + R)
    estimate = prediction + K * (measurement - prediction)
    P = (1 - K) * P
    Ks[i] = K
    Ps[i] = P
    predictions[i] = prediction
    estimates[i] = estimate


plt.plot(times, true_positions, label='True Position')
plt.plot(times, measurements, label='Sensor')
plt.plot(times, predictions, label='Physics Prediction')
plt.plot(times, estimates, label='Estimate')
plt.xlabel("time (s)")
plt.ylabel("height (m)")
plt.title("Kalman Filter")
plt.legend()
plt.savefig("plot.png")
plt.figure()
plt.plot(times, Ks, label='K')
plt.plot(times, Ps, label='P')
plt.xlabel("time (s)")
plt.legend()
plt.savefig("gain.png")
plt.show()    