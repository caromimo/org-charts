# Automated Org Charts

This project fully automates the data capture and generation of organizational charts.

## Description

The program processes a YAML file containing a series of actions, such as creating, updating, or deleting positions, as well as staffing actions like hiring, promotions, and departures. It then generates an interactive HTML-based organization chart visualizing the structure.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd automatedOrgCharts
    ```

2.  **Install dependencies using PDM:**
    ```bash
    pip install pdm
    pdm install
    ```

## Usage

1.  **Provide data:**
    The program reads data from `data/raw/data.yaml`. This file should contain a list of actions in YAML format. See the `data/raw/data.yaml` file for an example of the data structure.

2.  **Run the program:**
    ```bash
    pdm run main
    ```
    This will process the data and generate an `org_chart.html` file in the project's root directory.

3.  **View the org chart:**
    Open the `org_chart.html` file in your web browser to view the interactive organization chart.

## Project Structure

```
├── automatedorgcharts/
│   ├── Organization.py       # Defines the Organization class to process actions.
│   └── visualisation.py      # Generates the HTML org chart.
├── data/
│   └── raw/
│       └── data.yaml         # Input data file.
├── main.py                   # Main script to run the program.
├── org_chart.html            # Output HTML file.
├── pyproject.toml            # Project metadata and dependencies.
└── tests/
    ├── test_convert_to_date.py # Tests for date conversion utility.
    └── test_Organization.py    # Tests for the Organization class.
```

## How it Works

1.  **Data Processing:** The `main.py` script reads the `data.yaml` file, which contains a series of actions.
2.  **Organization Class:** The `Organization` class in `automatedorgcharts/Organization.py` processes these actions, updating the state of the organization's employees and positions.
3.  **Visualization:** The `visualize_org_chart` function in `automatedorgcharts/visualisation.py` takes the organization data and uses the Google Charts API to generate an interactive HTML organization chart.

## Running Tests

To run the automated tests, use the following command:

```bash
pdm run test
```
