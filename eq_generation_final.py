import matplotlib.pyplot as plt
import numpy as np
import random

# Position equation - make more diverse later?
def generate_equation():
    degree = random.randint(1, 4)
    coeffs = [random.uniform(-5, 5) for _ in range(degree)]
    equation = np.poly1d(coeffs)
    return equation

# Position, First Derivative, Second Derivative
position = generate_equation()
velocity = position.deriv(1)
acceleration = position.deriv(2)

# Rerun Button
def refresh_plot(event):
    global position, velocity, acceleration
    
    # Generate new random equations
    position = generate_equation()
    velocity = position.deriv(1)
    acceleration = position.deriv(2)
    
    # Generate new y values for position, velocity, and acceleration
    y_position = position(x)
    y_velocity = velocity(x)
    y_acceleration = acceleration(x)
    
    # Update the plots
    ax1.clear()
    ax1.plot(x, y_position)
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Position')
    ax1.set_title('Position versus Time')

    ax2.clear()
    ax2.plot(x, y_velocity)
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Velocity')
    ax2.set_title('Velocity versus Time')

    ax3.clear()
    ax3.plot(x, y_acceleration)
    ax3.set_xlabel('Time')
    ax3.set_ylabel('Acceleration')
    ax3.set_title('Acceleration versus Time')
    
    fig.canvas.draw()

# Generate x values 1-10
x = np.linspace(0, 10, 100)

# Evaluate position, velocity, and acceleration equations for y values
y_position = position(x)
y_velocity = velocity(x)
y_acceleration = acceleration(x)

# MAIN PLOTS
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12))

ax1.plot(x, y_position)
ax1.set_xlabel('Time')
ax1.set_ylabel('Position')
ax1.set_title('Position versus Time')

ax2.plot(x, y_velocity)
ax2.set_xlabel('Time')
ax2.set_ylabel('Velocity')
ax2.set_title('Velocity versus Time')

ax3.plot(x, y_acceleration)
ax3.set_xlabel('Time')
ax3.set_ylabel('Acceleration')
ax3.set_title('Acceleration versus Time')

# Rerun
refresh_button_ax = plt.axes([0.9, 0.05, 0.1, 0.075])
refresh_button = plt.Button(refresh_button_ax, 'Refresh')
refresh_button.on_clicked(refresh_plot)

plt.tight_layout()
plt.show()
