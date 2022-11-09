from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
import pandas as pd
class main:
    # import pdb; pdb.set_trace()
    def data_fetch(self):
        self.data = {}
        final = pd.DataFrame()
        to_year_int = int(self.n3.get())
        from_year_int = int(self.n1.get())
        print(to_year_int)
        print(from_year_int)
        for i in range(from_year_int, to_year_int+1):
            path = r"D:\\Amrita\\NT\\NTRS-Hackathon\\Cur_Conv_Dat\\Exchange_Rate_Report_" + str(i) + '.csv'
            self.data["year{}".format(i)] = pd.read_csv(path)
            var = 'year' + str(i)
            final = final.append(self.data[var], ignore_index=True)
        # Clearning up unnecessary dataframes
        del self.data
        currency_index = final.columns.str.find(self.n2.get())
        for i in range(0, len(currency_index)):
            if(currency_index[i] != (-1)):
                currency_index_true = i
                break
        print(currency_index_true)
        if self.to_currency != 'USD':
            min_val = final.iloc[:,currency_index_true].min()
            min_val_index =  final.iloc[:,currency_index_true].idxmin()
            max_val_index = final.iloc[:,currency_index_true].idxmax()
            max_val = final.iloc[:,currency_index_true].max()
            print(min_val)
            print(min_val_index)
            print(max_val_index)
            pd.get_option('plotting.backend') # default: matplotlib
            # df = pd.DataFrame(dict(a=[1,3,2], b=[3,2,1]))
            final.iloc[:,currency_index_true].plot(backend='plotly') # backend exception only for this one plot.
            pd.set_option('plotting.backend', 'plotly') # or
            pd.options.plotting.backend = "plotly"
            fig = final.iloc[:,currency_index_true].plot() # uses backend set in options else default.
            fig.show()
        
    
    def window(self):
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
        self.n = tk.StringVar(bottom_frame) 
        # n.set(self.currencies[0])
        self.n1 = tk.StringVar(bottom_frame) 
        # n1.set(self.years[0])
        self.n2 = tk.StringVar(bottom_frame) 
        # n2.set(self.currencies[0])
        self.n3 = tk.StringVar(bottom_frame) 
        # n3.set(self.years[0])
        # widgets inside the bottom frame
        from_label = Label(bottom_frame,text='FROM', font=('Poppins 9 bold'), justify=RIGHT, fg=primary)
        from_label.place(x=5, y=10)

        to_currency_label = Label(bottom_frame, text='CURRENCY', font=('Poppins 9 bold'), justify=RIGHT)
        to_currency_label.place(x=200, y=40)

        # CURRENCY LIST
        self.currencies = ['DZD','AUD', 'BHD', 'VEF', 'BWP', 'BRL', 'BND', 'CAD', 'CLP', 'CNY',
        'COP', 'CZK', 'DKK', 'EUR', 'HUF', 'ISK', 'INR', 'IDR', 'IRR', 'ILS', 'JPY', 'KZT',
        'KRW', 'KWD', 'LYD', 'MYR', 'MUR', 'MXN', 'NPR', 'NZD', 'NOK', 'OMR', 'PKR', 'PEN', 
        'PHP', 'PLN', 'QAR', 'RUB', 'SAR', 'SGD', 'ZAR', 'LKR', 'SEK', 'CHF', 'THB', 'TTD', 
        'TND', 'AED', 'GBP', 'USD', 'UYU']
        ##Testing
        def check(*args):
            print(f"the variable has changed to '{self.n.get()}' \n '{self.n1.get()}' \n '{self.n2.get()}' \n '{self.n3.get()}'")
        self.n.trace('w', check)
        self.n1.trace('w', check)
        self.n2.trace('w', check)
        self.n3.trace('w', check)
        # this is the combobox for holding from_currencies
        from_currency_combo = ttk.OptionMenu(bottom_frame,self.n,self.currencies[49], *self.currencies)
        from_currency_combo.width = 10
        from_currency_combo.font = ('Poppins 10 bold')
        self.from_currency = self.n.get()
        from_currency_combo.place(x=200, y=58)

        # YEARS LIST
        self.years = ['2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022']
        # this is the combobox for holding years
        years_label = Label(bottom_frame, text='YEAR', font=('Poppins 9 bold'), justify=RIGHT)
        years_label.place(x=120, y=40)
        years_combo = ttk.OptionMenu(bottom_frame,self.n1, *self.years)
        years_combo.width=6
        years_combo.font=('Poppins 10 bold')
        years_combo.place(x=120, y=58)
        self.from_year = self.n1.get()

        # Month entry
        month_label = Label(bottom_frame, text='MONTH', font=('Poppins 9 bold'), justify=RIGHT)
        month_label.place(x=55, y=40)
        month_entry = Entry(bottom_frame, width=3, font=('Poppins 10 bold'))
        month_entry.place(x=55, y=60)
        self.month = month_entry.get()

        # Date entry
        date_label = Label(bottom_frame, text='DATE', font=('Poppins 9 bold'), justify=RIGHT)
        date_label.place(x=5, y=40)
        date_entry = Entry(bottom_frame, width=3, font=('Poppins 10 bold'))
        date_entry.place(x=8, y=60)
        self.date = date_entry.get()
        ##########################################
        # TO section
        to_label = Label(bottom_frame, text='TO', font=('Poppins 9 bold'), justify=RIGHT, fg=primary)
        to_label.place(x=5, y=88)

        # to_Currency
        to_currency_combo_2 = ttk.OptionMenu(bottom_frame,self.n2,self.currencies[49], *self.currencies)
        to_currency_combo_2.width=10
        to_currency_combo_2.font=('Poppins 10 bold')
        to_currency_combo_2.place(x=200, y=130)
        self.to_currency = self.n2.get()

        to_currency_label_2 = Label(bottom_frame, text='CURRENCY', font=('Poppins 9 bold'), justify=RIGHT)
        to_currency_label_2.place(x=200, y=109)

        # to_year
        to_years_label = Label(bottom_frame, text='YEAR', font=('Poppins 9 bold'), justify=RIGHT)
        to_years_label.place(x=120, y=109)
        to_years_combo = ttk.OptionMenu(bottom_frame,self.n3, *self.years)
        to_years_combo.width=6 
        to_years_combo.font=('Poppins 10 bold')
        to_years_combo.place(x=120, y=130)
        self.to_year = self.n3.get()

        # Month entry
        to_month_label = Label(bottom_frame, text='MONTH', font=('Poppins 9 bold'), justify=RIGHT)
        to_month_label.place(x=55, y=109)
        to_month_entry = Entry(bottom_frame, width=3, font=('Poppins 10 bold'))
        to_month_entry.place(x=55, y=130)
        self.to_month = month_entry.get()

        # Date entry
        to_date_label = Label(bottom_frame, text='DATE', font=('Poppins 9 bold'), justify=RIGHT)
        to_date_label.place(x=5, y=109)
        to_date_entry = Entry(bottom_frame, width=4, font=('Poppins 10 bold'))
        to_date_entry.place(x=5, y=131)
        self.to_date = date_entry.get()
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
        main_button = Button(bottom_frame, text="CONVERT", bg=secondary, fg=white, font=('Poppins 10 bold'),command=self.data_fetch)
        main_button.place(x=5, y=165)
        window.mainloop()

        

if __name__ == '__main__':
    top = main()
    top.window()