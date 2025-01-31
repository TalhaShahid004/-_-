# CodeAlpha_Tasks

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/TalhaShahid004/CodeAlpha_Tasks)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

</div>

This repository contains a collection of Python-based projects completed during the CodeAlpha February Internship 2024. It showcases implementations of a text-based Hangman game, a real-time stock portfolio tracker, and an automated file organizer. These tasks highlight practical applications of Python programming, demonstrating skills in algorithm design, file handling, and data manipulation.

## Features

* **Hangman Game:** A classic word-guessing game with user interaction and visual feedback.
* **Portfolio Tracker:** A system that fetches real-time stock prices and calculates portfolio value.
* **Automated File Organizer:** A script that categorizes files into specified folders based on their extensions.
* **Clear Documentation:** Each project includes a README file with usage instructions and project details.
* **Well-Structured Code:** Each task is implemented in a logical manner with descriptive comments.
* **CSV Data Storage:** The portfolio tracker uses CSV files to store data, showcasing basic data management skills.

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/TalhaShahid004/CodeAlpha_Tasks.git
    cd CodeAlpha_Tasks
    ```
2. Navigate into each project directory to run individual scripts.

## Running the Projects

### Hangman Game

1. Navigate to the `Hangman` directory:
    ```bash
    cd Hangman
    ```
2. Run the game:
    ```bash
    python main.py
    ```
3. Follow the on-screen prompts to play.

### File Organizer

1. Navigate to the `fileMover` directory:
    ```bash
    cd fileMover
    ```
2. Modify the `downloads_folder_path` variable in `main.py` to point to your downloads directory
3. Run the script:
    ```bash
    python main.py
    ```
    This script will organize your download files by extension type.

### Portfolio Tracker

1. Navigate to the `portfolioTracker` directory:
    ```bash
    cd portfolioTracker
    ```
2. Modify the `assets.csv` file to reflect your stock holdings with one row for the names and one for quantities (separated by commas).
3. Run the script:
    ```bash
    python main.py
    ```
4. Follow the on-screen prompts to view the portfolio valuation and add new stock data.

## Dependencies

* **Python 3.x:** The core programming language for all projects.
* **yfinance:** Used in the portfolio tracker to fetch real-time stock data.
    ```bash
    pip install yfinance
    ```
* **pandas:** Used in the portfolio tracker for CSV data manipulation.
    ```bash
    pip install pandas
    ```

## Contribution

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them
4. Push your branch to your forked repository
5. Submit a pull request to the original repository

## License

This project is licensed under the MIT License.
