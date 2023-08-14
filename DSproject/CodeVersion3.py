import numpy as np                                 # Import the NumPy library
import matplotlib.pyplot as plt                    # Import the Matplotlib pyplot module

def mandelbrot(c, max_iter):
    z = 0                                           # Initialize z to 0
    for i in range(max_iter):                       # Iterate max_iter times
        z = z**2 + c                                # Update z using the Mandelbrot equation
        if abs(z) > 2:                              # If the absolute value of z exceeds 2
            return i                                # Return the current iteration count
    return max_iter                                 # Return the maximum iteration count if not exceeded

def display_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    x = np.linspace(x_min, x_max, width)            # Generate an array of x values
    y = np.linspace(y_min, y_max, height)           # Generate an array of y values
    img = np.empty((height, width))                  # Create an empty 2D array for the image
    for i in range(height):                          # Iterate over the rows of the image
        for j in range(width):                       # Iterate over the columns of the image
            img[i, j] = mandelbrot(x[j] + 1j * y[i], max_iter)  # Compute the Mandelbrot value and store it in the image array

    plt.imshow(img, cmap='Blues_r', extent=(x_min, x_max, y_min, y_max))  # Display the image using a colormap and spatial extent
    plt.xlabel('Re(c)')                             # Set the label for the x-axis
    plt.ylabel('Im(c)')                             # Set the label for the y-axis
    plt.title("Mandelbrot Set")                      # Set the title of the plot
    plt.show()                                      # Show the plot

# Parameters for the Mandelbrot set
width = 800
height = 600
x_min = -2.0
x_max = 0.47
y_min = -1.12
y_max = 1.12
max_iter = 50                                    # Maximum number of iterations

display_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)  # Call the function to display the Mandelbrot set
