# Forex Trading Bot

## Overview

The Forex Trading Bot is a Python-based project that allows users to implement and run custom trading strategies in the foreign exchange (forex) market. The project includes a trading bot written in Python, a Flask web server for displaying trading information, and a simple frontend for visualizing data.

## Steps to complete (My plan for the project)

-   ->(current step) **Display currency quotes on website:** Create simple HTML and JS files that take in the data using the IG markets API.
-   **Feature Breakdown:**
-   **Begin Testing Procedure:** write usint tests, automate testing using a testing framework
-   **Configure Continuous Integration (CI):** Configure CI to run tests automatically
-   **Implement Bot logic**
-   **Add Custom Strategies**
-   **Build Flask Web Server**
-   **Create API Endpoints**
-   **Design Standard Frontend**
-   **Integrate Backend with Frontend**

## Features

-   **Customizable Trading Strategies:** Users can implement and deploy their custom trading strategies based on market conditions, indicators, or other criteria.

-   **Web Interface:** The project includes a web interface that displays real-time and historical trading data, providing insights into the bot's performance.

-   **Modular Structure:** The project is organized into modular components, making it easy to extend and customize. The backend and frontend are separate, allowing flexibility in technology choices.

## Folder Structure

The project follows a structured organization for clarity and maintainability. Here's an overview of the main directories:

-   **backend/:** Contains the main trading bot logic and the Flask API for serving trading data.

-   **frontend/:** Holds the frontend code, including HTML templates, CSS stylesheets, and JavaScript files.

-   **web/:** Includes a simple Flask web application that serves as an alternative to the more complex frontend.

-   **.gitignore:** Specifies which files and directories should be ignored by Git.

-   **.env:** Stores environment variables for local development.

## Getting Started

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/iam-micah/forex-trading-bot-v1.git
    cd forex-trading-bot
    ```

````

2. **Install Dependencies:**

    - For the backend:
        ```bash
        cd backend
        pip install -r requirements.txt
        ```
    - For the frontend:
        ```bash
        cd frontend
        npm install
        ```

3. **Run the Flask Web App:**

    ```bash
    cd web
    python app.py
    ```

4. **Access the Web App:**
    <!-- Open your web browser and go to [http://localhost:5000](http://localhost:5000). -->

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.

2. Create a new branch:

    ```bash
    git checkout -b feature/new-feature
    ```

3. Make your changes and commit them:

    ```bash
    git commit -m "Add new feature"
    ```

4. Push your changes to your fork:

    ```bash
    git push origin feature/new-feature
    ```

5. Open a pull request.

## License

This project has no license yet.

## Acknowledgments

-   Thanks to the Flask and Python communities for creating excellent frameworks and tools.
-   **IG Markets API:**
    The Forex Trading Bot utilizes the [IG Markets API](https://developer.ig.com/) to access financial market data and execute trades. Special thanks to IG Markets for providing this API.

```

```
````
