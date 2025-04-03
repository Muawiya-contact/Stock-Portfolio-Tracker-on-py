# Stock Portfolio Tracker

This is a Stock Portfolio Tracker application that allows users to track, manage, and monitor the performance of their stock investments in real time. The tool integrates with the Alpha Vantage API to fetch real-time stock prices, making it a robust solution for individual investors.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [How to Use](#how-to-use)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Stock Portfolio Tracker allows users to:

- Add stocks to their portfolio with quantity and price information.
- Remove stocks from the portfolio.
- View current portfolio status, including the stock's price, quantity, and total value.
- Fetch real-time stock data via the Alpha Vantage API.

This project was created as a task for my internship at **@CodeAlpha**, aiming to develop a useful tool for stock investors while practicing good coding practices and API integration.

## Features

- **Real-Time Stock Price Fetching**: Fetches real-time stock prices using the Alpha Vantage API.
- **Portfolio Management**: Users can add, remove, and view their stock portfolio.
- **Total Portfolio Value**: Displays the total value of the user's portfolio by calculating the stock's current value.
- **Error Handling**: Proper error messages in case of incorrect stock symbols, missing API keys, or network issues.

## Technologies Used

- **Python**: Core programming language used for backend logic.
- **Requests**: Python HTTP library used to make API calls to Alpha Vantage.
- **Alpha Vantage API**: Provides real-time stock price data (free API key required).
- **Text Files**: Used for securely storing the API key (`api_keys.txt`).

## Setup Instructions

To get started with this project on your local machine, follow the steps below:

### Prerequisites

1. **Python 3.6+**: Ensure you have Python 3.6 or later installed on your system.
   
2. **Required Libraries**: Install the required libraries using `pip` by running the following command:

   ```bash
   pip install requests
