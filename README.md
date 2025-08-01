# Obstacle-avoider-prototype
🚘 Obstacle-Aware Car Simulation – Pygame Project
This is a simple yet engaging Pygame simulation where a self-steering car detects and avoids falling rectangular obstacles using basic ray-like distance sensing. It uses horizontal and diagonal virtual sensors to steer left or right in real-time based on the proximity of obstacles.


🎮 Features
🟥 Interactive Obstacle Spawning: Click anywhere to spawn a falling red obstacle.

🚗 Auto-Navigating Car: The car adjusts its velocity based on the proximity of objects detected by:

Left sensor

Right sensor

Left diagonal sensor

Right diagonal sensor

📏 Sensor-Based Movement: Distance-based color-coded lines:

🟢 Green – Safe distance

🟡 Yellow – Caution zone

🔴 Red – Immediate obstacle detected


🧠 How It Works
The car uses 4 virtual sensors (left, right, left-diagonal, right-diagonal) to measure the distance to falling rectangular objects. Based on these measurements:

It accelerates away from obstacles.

The sensor lines change colors based on threat level.

Velocities are updated every frame for smooth simulation.

🛠️ Tech Stack
Python

Pygame

▶️ How to Run
Install Pygame (if not already):

bash
Copy code
pip install pygame
Run the Script:

bash
Copy code
python car_simulation.py
Controls:

Left click anywhere to drop an obstacle.

The car will automatically move to avoid collisions.

📁 File Structure
bash
Copy code
car_simulation.py  # Main game file
README.md          # Project documentation


🌟 Future Ideas
Add vertical sensors for front obstacle detection.

Introduce multiple levels of difficulty (faster falling objects).

Train a neural network for movement instead of rule-based logic.


🌟🌟training a neural net with RL can improve accuracy and will be much like self driving car simulations

Visualize sensor ranges more clearly with fading colors.

📜 License
This project is free to use and modify under the MIT License.

👨‍💻 Author


Divyansh Agarwal


Crafting creative simulations with code. 🚀

