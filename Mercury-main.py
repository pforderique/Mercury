###############################################################################################
###                                      PROJECT MERCURY                                    ###
###                                                                                         ###
### @author Piero Orderique                                                                 ###
###############################################################################################

from selenium import webdriver 
import pandas as pd
import backendFunctions as bf
from time import sleep

CHROME_DRIVER_PATH = "C:\\Users\\fabri\\miniconda3\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe"
PORTFOLIO_DATA_STORE_LOC = "C:/Users/fabri/OneDrive/Documents/DasText/csvFiles/myPortofilo.csv"
TRADING_VIEW_URL = "https://www.tradingview.com/"
YAHOO_FINANCE_URL = "https://finance.yahoo.com/"
DIVIDER = "-----------------------------------------------------------"
driver = webdriver.Chrome(CHROME_DRIVER_PATH) #main driver

#USER INPUT
usersWebsite = YAHOO_FINANCE_URL
username = "jakeowens107@gmail.com"
password = "Swimming1!"
#portfolio = "Primary"

if bf.user_signed_in(driver,usersWebsite,username,password):
    print(DIVIDER+"\nCollecting Data...")
    dict_main = bf.readDataToDictionary(driver) #stores the dictionary returned for testing purposes
    
    df_main = pd.DataFrame(dict_main)
    df_main.to_csv(PORTFOLIO_DATA_STORE_LOC)
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    print(df_main)  # makes data frame and diplays it 
    df_main.head()
else:
    print(DIVIDER+"\nSign In Error: Check internet connection and speed.")
    print("Use previously downloaded data? (y/n)") #if no connection, ask if they want to use stock list loaded in past instead. 

#TODO Have the names of the stocks that users written on a file so that it is stored and read from there 
        #Have loaded stocks displayed and ask if they want to remove/add stocks to their list