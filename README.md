# NTRS-Hackathon
## Installation
```run pip install -r requirements.txt```
## How to run
run ```python main.py``` on your terminal inside the folder and change the location of pd.read_csv location inside main.py with the local dataset file path.
## What it does
After entering the required from and to dates into the Tkinter GUI console, clicking on ```GRAPH IT!``` will redirect the user to a webpage on localhost where plotly has hosted the data along with information on it and various views.
## How was it built?
The main GUI was built using Tkinter on Python, the graph was plotted using plotly library and data is being referenced in the form of a dataframe using pandas library.
## How it works
After the user has entered the details of the from and to dates along with the currency, the backend creates a dataframe that contains all the currencies in the timeframe by merging all the required years from the csv files. We then index the ```final``` dataframe and perform an all out operation on it, where the data is visualized using plotly.
## Challenges
Honestly the main challenge was coordinating with other students and completeing this project within 24 hours. The teamwork lacked in several parts, yet we pulled off the best we could do, given the situation.
