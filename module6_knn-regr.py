import numpy as np
def knn_regression(x_train, y_train, x_input, k):
    distances = np.abs(x_train - x_input)
    nearest_indices = distances.argsort()[:k]
    return np.mean(y_train[nearest_indices])
  
def main():
    try:
        N = int(input("Enter number of data points (N): "))
        k = int(input("Enter number of neighbors (k): "))
        if k > N or N <= 0 or k <=0:
          print("Error: Ensure N > 0, k > 0, and k <= N")
          return
        x_vals = []
        y_vals = []
  
        print(f"Enter {N} (x,y) pairs:")
        for _ in range(N):
            x, y = map(float, input("Enter x and y separated by space: ").split())
            x_vals.append(x)
            y_vals.append(y)
  
        x_vals = np.array(x_vals)
        y_vals = np.array(y_vals)
  
        x_input = float(input("Enter X value to predict Y: "))
        y_output = knn_regression(x_vals, y_vals, x_input, k)
  
        print(f"predicted Y value using k-NN Regression: {y_output:.3f}")
  
    except ValueError:
      print("Invalid input. Please enter numeric values")
  
if __name__ == "__main__":
      main()