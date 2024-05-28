# Hurricane-Tracker
This Python project visualizes hurricane paths on a map using Turtle graphics, allowing users to input a storm name and displaying the hurricane's path and category based on wind speed. The code demonstrates proficiency in data manipulation, visualization, and user interaction.

# Project Structure
The project consists of the following files:

hurricane_tracker.py: Main Python file containing the code for the hurricane tracker.
images/atlantic-basin.png: Background image of the Atlantic Basin.
images/hurricane.gif: Image of a hurricane used as the turtle shape.
data/*.csv: CSV files containing hurricane data, with one file per hurricane.

# Getting Started
Clone the repository: git clone <repository URL>
Install Python: Download and install Python 3.x from https://www.python.org/downloads/.
Install Turtle: The Turtle module is part of the standard Python library, so it is already included.
Install Pandas: pip install pandas (optional)
Run the code: python hurricane_tracker.py

# Data Format
Each CSV file in the data directory contains hurricane data in the following format:

Column	Description
Date	Date of the hurricane data (YYYY-MM-DD HH:MM:SS)
Time	Time of the hurricane data (HH:MM:SS)
Latitude	Latitude of the hurricane center (decimal degrees)
Longitude	Longitude of the hurricane center (decimal degrees)
Wind Speed	Maximum sustained wind speed (knots)
Pressure	Central pressure (millibars)
