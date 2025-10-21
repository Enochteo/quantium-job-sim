## Interactive Pricing Strategy & Sales Analysis Tool
An interactive Dash web application built during the Quantium Software Engineering Job Simulation (Forage). This tool allows stakeholders to model price changes and instantly visualize their impact on sales and profitability, enabling faster, data-driven pricing decisions

**Features**
Scenario Simulation: Adjust price parameters to instantly see the effect on sales and profit.

Real-Time Visualizations: Interactive charts powered by Plotly for clear insights.

Automated Testing Pipeline: Built with Pytest and a bash script for quick verification of app performance.

User-Friendly UI: Intuitive, engaging, and responsive design for non-technical users.

**Tech Stack**
Frontend & Backend: Dash (Python)

Data Manipulation: Pandas

Visualization: Plotly

Testing: Pytest

Automation: Bash scripting

Data Validation: Python

**Screenshots**
![demo_1](demo1.png) ![demo_2](demo2.png)

## Project Structure

```bash
.
├── README.md           # Project documentation
├── app.py              # Main Dash application
├── data                # Datasets
│   ├── daily_sales_data_0.csv
│   ├── daily_sales_data_1.csv
│   └── daily_sales_data_2.csv
├── data-script.py
├── demo1.png
├── demo2.png
├── requirements.txt      # Project dependencies
├── run.sh
├── tasks.sh              # Bash script to run tests
├── test_app.py            # Pytest test suite
└── valuable-data.csv
```

**Expected Impacts**
- Reduce pricing analysis time from hours to minutes.

- Improve decision-making accuracy by providing instant feedback on pricing changes.

- Increase reliability through automated testing before deployment.

