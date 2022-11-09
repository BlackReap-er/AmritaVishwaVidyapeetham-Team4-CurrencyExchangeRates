from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
import pandas as pd
class main:

    def data_fetch(self):
        self.data = {}
        final = pd.DataFrame()
        for i in range(self.from_year, self.to_year+1):
            path = r"D:\Amrita\NT\Cur_Conv_Dat\Exchange_Rate_Report_" + str(i) + '.csv'
            self.data["year{}".format(i)] = pd.read_csv(path)
            var = 'year' + str(i)
            final = final.append(self.data[var], ignore_index=True)
        # Clearning up unnecessary dataframes
        del self.data
        

        
    
    # creating the main window
    window = Tk()
    window.geometry('410x440+500+200')
    window.title('Currency Grapher')
    window.resizable(height=FALSE, width=FALSE)
    primary = '#081F4D'
    secondary = '#0083FF'
    white = '#FFFFFF'

    # the top frame
    top_frame = Frame(window, bg=primary, width=450, height=80)
    top_frame.grid(row=0, column=0)

    # label for the text Currency Converter
    name_label = Label(top_frame, text='Currency Converter with graph', bg=primary, fg=white, pady=30, padx=60, justify=CENTER, font=('Poppins 15 bold'))
    name_label.grid(row=0, column=0)
    ##########################################
    # the bottom frame
    bottom_frame = Frame(window, width=400, height=450)
    bottom_frame.grid(row=1, column=0)

    # widgets inside the bottom frame
    from_label = Label(bottom_frame,text='FROM', font=('Poppins 9 bold'), justify=RIGHT, fg=primary)
    from_label.place(x=5, y=10)

    to_currency_label = Label(bottom_frame, text='CURRENCY', font=('Poppins 9 bold'), justify=RIGHT)
    to_currency_label.place(x=200, y=40)

    # CURRENCY LIST
    currencies = ['DZD','AUD', 'BHD', 'VEF', 'BWP', 'BRL', 'BND', 'CAD', 'CLP', 'CNY',
    'COP', 'CZK', 'DKK', 'EUR', 'HUF', 'ISK', 'INR', 'IDR', 'IRR', 'ILS', 'JPY', 'KZT',
    'KRW', 'KWD', 'LYD', 'MYR', 'MUR', 'MXN', 'NPR', 'NZD', 'NOK', 'OMR', 'PKR', 'PEN', 
    'PHP', 'PLN', 'QAR', 'RUB', 'SAR', 'SGD', 'ZAR', 'LKR', 'SEK', 'CHF', 'THB', 'TTD', 
    'TND', 'AED', 'GBP', 'USD', 'UYU']

    # this is the combobox for holding to_currencies
    to_currency_combo = ttk.Combobox(bottom_frame, values=currencies, width=10, font=('Poppins 10 bold'))
    from_currency = to_currency_combo.get()
    to_currency_combo.place(x=200, y=58)
    # YEARS LIST
    years = [2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
    # this is the combobox for holding years
    years_label = Label(bottom_frame, text='YEAR', font=('Poppins 9 bold'), justify=RIGHT)
    years_label.place(x=120, y=40)
    years_combo = ttk.Combobox(bottom_frame, values=years, width=6, font=('Poppins 10 bold'))
    years_combo.place(x=120, y=58)
    from_year = years_combo.get()

    # Month entry
    month_label = Label(bottom_frame, text='MONTH', font=('Poppins 9 bold'), justify=RIGHT)
    month_label.place(x=55, y=40)
    month_entry = Entry(bottom_frame, width=3, font=('Poppins 10 bold'))
    month_entry.place(x=55, y=60)
    month = month_entry.get()

    # Date entry
    date_label = Label(bottom_frame, text='DATE', font=('Poppins 9 bold'), justify=RIGHT)
    date_label.place(x=5, y=40)
    date_entry = Entry(bottom_frame, width=3, font=('Poppins 10 bold'))
    date_entry.place(x=8, y=60)
    date = date_entry.get()
    ##########################################
    # TO section
    to_label = Label(bottom_frame, text='TO', font=('Poppins 9 bold'), justify=RIGHT, fg=primary)
    to_label.place(x=5, y=88)

    # to_Currency
    to_currency_combo_2 = ttk.Combobox(bottom_frame, values=currencies, width=10, font=('Poppins 10 bold'))
    to_currency_combo_2.place(x=200, y=130)
    to_currency = to_currency_combo_2.get()

    to_currency_label_2 = Label(bottom_frame, text='CURRENCY', font=('Poppins 9 bold'), justify=RIGHT)
    to_currency_label_2.place(x=200, y=109)

    # to_year
    to_years_label = Label(bottom_frame, text='YEAR', font=('Poppins 9 bold'), justify=RIGHT)
    to_years_label.place(x=120, y=109)
    to_years_combo = ttk.Combobox(bottom_frame, values=years, width=6, font=('Poppins 10 bold'))
    to_years_combo.place(x=120, y=130)
    to_year = to_years_combo.get()

    # Month entry
    to_month_label = Label(bottom_frame, text='MONTH', font=('Poppins 9 bold'), justify=RIGHT)
    to_month_label.place(x=55, y=109)
    to_month_entry = Entry(bottom_frame, width=3, font=('Poppins 10 bold'))
    to_month_entry.place(x=55, y=130)
    to_month = month_entry.get()

    # Date entry
    to_date_label = Label(bottom_frame, text='DATE', font=('Poppins 9 bold'), justify=RIGHT)
    to_date_label.place(x=5, y=109)
    to_date_entry = Entry(bottom_frame, width=4, font=('Poppins 10 bold'))
    to_date_entry.place(x=5, y=131)
    to_date = date_entry.get()
    # # the label for AMOUNT
    # amount_label = Label(bottom_frame, text='AMOUNT:', font=('Poppins 10 bold'))
    # amount_label.place(x=5, y=75)

    # # entry for amount
    # amount_entry = Entry(bottom_frame, width=25, font=('Poppins 15 bold'))
    # amount_entry.place(x=5, y=100)

    # an empty label for displaying the result
    result_label = Label(bottom_frame, text='', font=('Poppins 10 bold'))
    result_label.place(x=5, y=135)

    # an empty label for displaying the time
    time_label = Label(bottom_frame, text='', font=('Poppins 10 bold'))
    time_label.place(x=5, y=155)

    # the clickable button for converting the currency
    main_button = Button(bottom_frame, text="CONVERT", bg=secondary, fg=white, font=('Poppins 10 bold'), command=data_fetch)
    main_button.place(x=5, y=165)
    window.mainloop()

        

