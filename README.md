# Stock Analysis of Pharma Companies: Pfizer, Johnson & Johnson, and Eli Lilly

## Overview

This project analyzes the stock performance of three major pharmaceutical companies: Pfizer, Johnson & Johnson, and Eli Lilly, over the past 5 years. Using stock data from Yahoo Finance (Yfinance), we perform an in-depth analysis that includes:

- **Stock closing price analysis**
- **Daily growth percentage**
- **Market capitalization trends**
- **Correlation analysis between the three companies**
- **Real-world scenarios and storytelling**
- **Conclusion and matching analysis with real-world articles**

## Introduction

In this project, we dive into the stock performance of **Pfizer**, **Johnson & Johnson (J&J)**, and **Eli Lilly** to evaluate their market behavior, daily growth, and overall trends over the last 5 years. We aim to uncover patterns in stock prices, assess how these companies compare, and explore possible reasons behind their stock market performance. Additionally, we tie our findings with real-world events and articles that may have affected the companies' stock prices during the analyzed period.

## Data Acquisition

The data for this analysis was acquired using **Yfinance**, a Python library that allows users to pull historical stock market data from Yahoo Finance. We collected the following data for each company over a 5-year period:

- **Closing Prices**: Daily closing stock prices of Pfizer, Johnson & Johnson, and Eli Lilly.
- **Market Capitalization**: Total market value of the companies at the end of each trading day.
- **Date Range**: 2019-2024

Data was retrieved and stored in CSV format for further processing and analysis.

## Analysis

### Closing Price Analysis

The closing price of a stock is a key metric in understanding its historical performance. We plot the closing prices of Pfizer, Johnson & Johnson, and Eli Lilly over the 5-year period to observe trends, volatility, and price movements.

Key insights from this analysis include:
- **Growth Patterns**: Which company had the most consistent upward trajectory?
- **Volatility**: How much fluctuation occurred in stock prices over time?

### Daily Growth

We calculate the daily growth (percentage change) in the stock prices to identify trends and patterns in daily performance.

- **Positive/Negative Growth**: Analyzing how frequently each stock experienced positive vs. negative growth.
- **Patterns**: Are there certain time periods where all companies performed similarly or differently?

### Market Capitalization

Market capitalization is a valuable indicator of a company’s overall size and economic standing. By analyzing the market cap of each company, we examine:

- **Growth of Market Capitalization**: Tracking the increase or decrease in market cap over time.
- **Comparison between Companies**: How do Pfizer, J&J, and Eli Lilly compare in terms of market cap growth?

### Correlation Analysis

We analyze the correlation between the stock prices of the three companies. This helps to identify if their stock movements are related, independent, or if they share common trends.

- **Pearson Correlation**: Determines the strength and direction of the relationship between the stock prices of the three companies.
- **Insights**: Does a major event like the approval of a drug or a global health crisis like the COVID-19 pandemic affect all companies in the same way?

## Real-World Scenarios & Storytelling

Stock market performance is often influenced by real-world events. In this section, we correlate significant real-world events with the stock movements of Pfizer, J&J, and Eli Lilly.

- **Pfizer and COVID-19**: Pfizer’s stock surged significantly after announcing its COVID-19 vaccine, and we analyze how this event affected its stock price trajectory.
- **J&J Legal Issues**: Johnson & Johnson faced several legal challenges over the past 5 years, which likely impacted its stock price. We analyze these events and their market impact.
- **Eli Lilly's Breakthrough Drugs**: Eli Lilly has made strides in developing new diabetes and cancer treatments. We examine how these developments influenced its stock price.

The goal is to create a narrative that connects stock market behavior with real-world events.

By comparing our analysis with published articles and reports, we gain a deeper understanding of how stock market trends align with real-world events.

## Installation and Requirements

To run the analysis on your local machine, you will need to install the following Python packages:

- `yfinance`
- `matplotlib`
- `pandas`
- `numpy`
- `seaborn`

You can install them using pip:

```bash
pip install yfinance matplotlib pandas numpy scipy seaborn
