
## Spotify Data Visualization

## Project Description

This project provides a data visualization tool for Spotify's top artists. It fetches data from the Spotify API and displays it in a user-friendly interface. The project is containerized using Docker to ensure a consistent and reproducible environment.

# File Structure
✅.cache/: Cache directory used for storing temporary data during the development process.
✅.env: Environment file that contains configuration variables required by the application, such as API keys and secrets.
✅Dockerfile: Defines the Docker image for the application, including the necessary dependencies and setup instructions.
✅docker-compose.yaml: Docker Compose file to manage multi-container Docker applications, simplifying the setup of the development and production environment.
✅app.py: The main application script that handles data fetching from the Spotify API and serves the data for visualization.
✅requirements.txt: Lists the Python dependencies required by the application.
✅spotify_top_data.csv: A CSV file that contains the fetched data of the top artists from Spotify.

## Installation and Setup
# Prerequisites
✅Docker
✅Docker Compose

## Steps
# Clone the repository:

✅git clone <repository-url>
✅cd <repository-directory>
✅Set up environment variables:

# Create a .env file in the root directory and add the necessary configuration variables. Example:

✅makefile

SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret

# Build and run the Docker containers:

✅docker-compose up --build

✅ the application:
Once the containers are up and running, access the application at http://localhost:5000.

# Usage
Fetching Data:
The application fetches the top artists' data from the Spotify API based on the market specified.

# Visualizing Data:
The data is visualized in a user-friendly format, displaying various metrics and insights about the top artists.

# API Reference
GET /top-artists
Fetches the top artists from Spotify for a specified market.

# Parameters:
✅market (required): The market for which to fetch the top artists.
✅limit (optional): The number of top artists to fetch. Default is 10.

# Contributing
✅Fork the repository.
✅Create a new branch (git checkout -b feature-branch).
✅Commit your changes (git commit -m 'Add some feature').
✅Push to the branch (git push origin feature-branch).
✅Open a Pull Request.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgments
✅Spotify API
✅Docker for containerization
