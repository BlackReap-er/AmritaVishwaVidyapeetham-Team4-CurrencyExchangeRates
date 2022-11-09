# NTRS-Hackathon
## Installation
```run pip install -r requirements.txt```
## How to run
run ```python main.py``` on your terminal inside the folder and change the location of pd.read_csv location inside main.py
## What it does
After entering the required from and to dates into the tkinter GUI console, clicking on ```GRAPH IT!``` will redirect the user to a webpage on localhost where plotly has hosted the data along with information on it and various views.
## How have i built it
The main GUI was built using tkinter on python, the graph was plotted using plotly library and data is being referenced in the form of a dataframe using pandas library.
## How it works
After the user has entered the details of the from and to dates along with the currency, the backend creates a dataframe that contains all the currencies in the timeframe by merging all the required years csv files. We then index the ```final``` dataframe and perform all out operation on it and we finally plot the data using plotly.
## Challenges
Honestly the main challenge was coordinating with other students as only 1 other student was active other than me and rest were all uninterested and this added a lot of pressure on me while doing the project as i am not that great with front end. 