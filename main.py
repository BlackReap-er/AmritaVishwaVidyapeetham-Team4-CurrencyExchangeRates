from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
import pandas as pd
import plotly.express as px
#importing all required libraries
class main:
    # import pdb; pdb.set_trace() ##Testing
    # Destroy the toplevel tkinter pane
    def ded():
        top.destroy()
    #Function to convert the amount 
    def convert(self):
        print(self.amount)
        self.data = {}
        final = pd.DataFrame()
        #Range of files to add to dataframe
        to_year_int = int(self.n3.get())
        from_year_int = int(self.n1.get())
        self.end_date = str(self.to_date) + '-' + str(self.to_month) + '-' + str(self.n3.get())
        #Appending all dataframes in the given data range to one dataframe for plotting and conversion
        for i in range(from_year_int, to_year_int+1):
            path = r"D:\\Amrita\\NT\\NTRS-Hackathon\\Cur_Conv_Dat\\Exchange_Rate_Report_" + str(i) + '.csv'
            self.data["year{}".format(i)] = pd.read_csv(path)
            var = 'year' + str(i)
            final = final.append(self.data[var], ignore_index=True)
        final.rename(columns={'Date':'Date', 'Algerian dinar   (DZD)                     ':'DZD',
        'Australian dollar   (AUD)                     ':'AUD',
        'Bahrain dinar   (BHD)                     ':'BHD',
        'Bolivar Fuerte   (VEF)                     ':'VEF',
        'Botswana pula   (BWP)                     ':'BWP',
        'Brazilian real   (BRL)                     ':'BRL',
        'Brunei dollar   (BND)                     ':'BND', 
        'Canadian dollar   (CAD)                     ':'CAD', 
        'Chilean peso   (CLP)                     ':'CLP', 
        'Chinese yuan   (CNY)                     ':'CNY', 
        'Colombian peso   (COP)                     ':'COP', 
        'Czech koruna   (CZK)                     ':'CZK', 
        'Danish krone   (DKK)                     ':'DKK', 
        'Euro   (EUR)                     ':'EUR', 
        'Hungarian forint   (HUF)                     ':'HUF', 
        'Icelandic krona   (ISK)                     ':'ISK', 
        'Indian rupee   (INR)                     ':'INR', 
        'Indonesian rupiah   (IDR)                     ':'IDR', 
        'Iranian rial   (IRR)                     ':'IRR', 
        'Israeli New Shekel   (ILS)                     ':'ILS', 
        'Japanese yen   (JPY)                     ':'JPY', 
        'Kazakhstani tenge   (KZT)                     ':'KZT', 
        'Korean won   (KRW)                     ':'KRW', 
        'Kuwaiti dinar   (KWD)                     ':'KWD', 
        'Libyan dinar   (LYD)                     ':'LYD', 
        'Malaysian ringgit   (MYR)                     ':'MYR', 
        'Mauritian rupee   (MUR)                     ':'MUR', 
        'Mexican peso   (MXN)                     ':'MXN', 
        'Nepalese rupee   (NPR)                     ':'NPR', 
        'New Zealand dollar   (NZD)                     ':'NZD', 
        'Norwegian krone   (NOK)                     ':'NOK', 
        'Omani rial   (OMR)                     ':'OMR', 
        'Pakistani rupee   (PKR)                     ':'PKR', 
        'Peruvian sol   (PEN)                     ':'PEN', 
        'Philippine peso   (PHP)                     ':'PHP', 
        'Polish zloty   (PLN)                     ':'PLN', 
        'Qatari riyal   (QAR)                     ':'QAR', 
        'Russian ruble   (RUB)                     ':'RUB', 
        'Saudi Arabian riyal   (SAR)                     ':'SAR', 
        'Singapore dollar   (SGD)                     ':'SGD',
        'South African rand   (ZAR)                     ':'ZAR', 
        'Sri Lankan rupee   (LKR)                     ':'LKR', 
        'Swedish krona   (SEK)                     ':'SEK', 
        'Swiss franc   (CHF)                     ':'CHF', 
        'Thai baht   (THB)                     ':'THB', 
        'Trinidadian dollar   (TTD)                     ':'TTD', 
        'Tunisian dinar   (TND)                     ':'TND', 
        'U.A.E. dirham   (AED)                     ':'AED', 
        'U.K. pound   (GBP)                     ':'GBP', 
        'U.S. dollar   (USD)                     ':'USD', 
        'Uruguayan peso   (UYU)                     ':'UYU', 
        'Bolivar Soberano   (VES)                     ':'VES'}, inplace=True)

        value = final.at[self.end_date,self.n2.get()]
        converted_amount = int(self.amount) * int(value)
        text = 'Converted Amount=' + str(converted_amount) + '  On:' + str(self.end_date)
        top= Toplevel(self.window)
        top.geometry("250x250")
        top.title("Converted Amount")
        Label(top, text= text, font=('Mistral 18 bold')).place(x=150,y=80)
        exit = del_button = Button(top, text="Close", font=('Poppins 10 bold'),command=self.ded)
        exit.place(x=150, y=150)
        
    def data_fetch(self):
        self.data = {}
        final = pd.DataFrame()
        #Range of files to add to dataframe
        to_year_int = int(self.n3.get())
        from_year_int = int(self.n1.get())
        #Appending all dataframes in the given data range to one dataframe for plotting and conversion
        for i in range(from_year_int, to_year_int+1):
            path = r"D:\\Amrita\\NT\\NTRS-Hackathon\\Cur_Conv_Dat\\Exchange_Rate_Report_" + str(i) + '.csv'
            self.data["year{}".format(i)] = pd.read_csv(path)
            var = 'year' + str(i)
            final = final.append(self.data[var], ignore_index=True)
        # Clearing up unnecessary dataframes to free memory
        del self.data
        #Finding index of the currency selected
        currency_index = final.columns.str.find(self.n2.get())
        for i in range(0, len(currency_index)):
            if(currency_index[i] != (-1)):
                currency_index_true = i
                break
        print(currency_index_true)
        #Start and End Date conversion
        self.start_date = str(self.date) + '-' + str(self.month) + '-' + str(self.n1.get())
        self.end_date = str(self.to_date) + '-' + str(self.to_month) + '-' + str(self.n3.get())

        #Currency Dictionary
        final.rename(columns={'Date':'Date', 'Algerian dinar   (DZD)                     ':'DZD',
        'Australian dollar   (AUD)                     ':'AUD',
        'Bahrain dinar   (BHD)                     ':'BHD',
        'Bolivar Fuerte   (VEF)                     ':'VEF',
        'Botswana pula   (BWP)                     ':'BWP',
        'Brazilian real   (BRL)                     ':'BRL',
        'Brunei dollar   (BND)                     ':'BND', 
        'Canadian dollar   (CAD)                     ':'CAD', 
        'Chilean peso   (CLP)                     ':'CLP', 
        'Chinese yuan   (CNY)                     ':'CNY', 
        'Colombian peso   (COP)                     ':'COP', 
        'Czech koruna   (CZK)                     ':'CZK', 
        'Danish krone   (DKK)                     ':'DKK', 
        'Euro   (EUR)                     ':'EUR', 
        'Hungarian forint   (HUF)                     ':'HUF', 
        'Icelandic krona   (ISK)                     ':'ISK', 
        'Indian rupee   (INR)                     ':'INR', 
        'Indonesian rupiah   (IDR)                     ':'IDR', 
        'Iranian rial   (IRR)                     ':'IRR', 
        'Israeli New Shekel   (ILS)                     ':'ILS', 
        'Japanese yen   (JPY)                     ':'JPY', 
        'Kazakhstani tenge   (KZT)                     ':'KZT', 
        'Korean won   (KRW)                     ':'KRW', 
        'Kuwaiti dinar   (KWD)                     ':'KWD', 
        'Libyan dinar   (LYD)                     ':'LYD', 
        'Malaysian ringgit   (MYR)                     ':'MYR', 
        'Mauritian rupee   (MUR)                     ':'MUR', 
        'Mexican peso   (MXN)                     ':'MXN', 
        'Nepalese rupee   (NPR)                     ':'NPR', 
        'New Zealand dollar   (NZD)                     ':'NZD', 
        'Norwegian krone   (NOK)                     ':'NOK', 
        'Omani rial   (OMR)                     ':'OMR', 
        'Pakistani rupee   (PKR)                     ':'PKR', 
        'Peruvian sol   (PEN)                     ':'PEN', 
        'Philippine peso   (PHP)                     ':'PHP', 
        'Polish zloty   (PLN)                     ':'PLN', 
        'Qatari riyal   (QAR)                     ':'QAR', 
        'Russian ruble   (RUB)                     ':'RUB', 
        'Saudi Arabian riyal   (SAR)                     ':'SAR', 
        'Singapore dollar   (SGD)                     ':'SGD',
        'South African rand   (ZAR)                     ':'ZAR', 
        'Sri Lankan rupee   (LKR)                     ':'LKR', 
        'Swedish krona   (SEK)                     ':'SEK', 
        'Swiss franc   (CHF)                     ':'CHF', 
        'Thai baht   (THB)                     ':'THB', 
        'Trinidadian dollar   (TTD)                     ':'TTD', 
        'Tunisian dinar   (TND)                     ':'TND', 
        'U.A.E. dirham   (AED)                     ':'AED', 
        'U.K. pound   (GBP)                     ':'GBP', 
        'U.S. dollar   (USD)                     ':'USD', 
        'Uruguayan peso   (UYU)                     ':'UYU', 
        'Bolivar Soberano   (VES)                     ':'VES'}, inplace=True)
        #Plotting the chart
        final['Date'] = pd.to_datetime(final['Date'])  
        # start_date = '2015-01-01'
        # end_date = '2016-01-02'
        mask = (final['Date'] > self.start_date) & (final['Date'] <= self.end_date)
        df = final.loc[mask]
        hallo = 'USD VS ' + self.n2.get()
        fig = px.line(df, x="Date", y=self.n2.get(), title=hallo)
        # Providing option for selecting weekly, monthly and yearly timeframes
        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all")
                ])
            )
        )
        # Displaying maximum and minimum value of currency in given timeframe
        max_val = final.iloc[:,currency_index_true].max()
        min_val = final.iloc[:,currency_index_true].min()
        text = '<b>MAX:' + str(max_val) + '  MIN:' + str(min_val) + '</b>'
        fig.add_annotation(dict(font=dict(color="black",size=12),
                            x=1.06,
                            y=1.06,
                            showarrow=False,
                            text=text,
                            textangle=0,
                            xref="paper",
                            yref="paper"
                           ))
        fig.show()
                
    # Main tkinter page
    def window(self):
        # creating the main self.window
        self.window = Tk()
        self.window.geometry('410x440+500+200')
        self.window.title('Currency Grapher')
        self.window.resizable(height=FALSE, width=FALSE)
        primary = '#081F4D'
        secondary = '#0083FF'
        white = '#FFFFFF'

        # the top frame
        top_frame = Frame(self.window, bg=primary, width=450, height=80)
        top_frame.grid(row=0, column=0)

        # label for the text Currency Converter
        name_label = Label(top_frame, text='Currency Converter with graph', bg=primary, fg=white, pady=30, padx=60, justify=CENTER, font=('Poppins 15 bold'))
        name_label.grid(row=0, column=0)
        ##########################################
        # the bottom frame
        bottom_frame = Frame(self.window, width=400, height=450)
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
        'TND', 'AED', 'GBP', 'USD', 'UYU', 'VES']

        ##Testing 
        # def check(*args):
        #     print(f"the variable has changed to '{self.n.get()}' \n '{self.n1.get()}' \n '{self.n2.get()}' \n '{self.n3.get()}'")
        # self.n.trace('w', check)
        # self.n1.trace('w', check)
        # self.n2.trace('w', check)
        # self.n3.trace('w', check)

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

        # the clickable button for converting the currency
        main_button = Button(bottom_frame, text="GRAPH IT!", bg=secondary, fg=white, font=('Poppins 10 bold'),command=self.data_fetch)
        main_button.place(x=5, y=165)

        # entry for amount
        amount_label = Label(bottom_frame,text = 'Enter Amount to convert', font=('Poppins 10 bold'))
        amount_label.place(x=5,y=200)
        amount_entry = Entry(bottom_frame, width=25, font=('Poppins 15 bold'))
        amount_entry.place(x=5, y=220)
        self.amount = amount_entry.get()
        convert_button = Button(bottom_frame, text="CONVERT IT!", bg=secondary, fg=white, font=('Poppins 10 bold'),command=self.convert)
        convert_button.place(x=5,y=260)
        self.window.mainloop()

        

if __name__ == '__main__':
    top = main()
    top.window()