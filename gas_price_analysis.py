# Robert Propheter
# Gas Price Analysis

'''
This program will read the contents of the GasPrices.txt file, which contains
the weekly average price of a gallon of gas. The format is mm-dd-yyyy:price.
The program then promts a menu asking for user input on what they would like to 
do with the program/data. The following will be performed by the program:

1) Average Price Per Year: 
     - For every year in the file
     
2) Average Price per Month: 
     - For each month in the file
     
3) Highest and Lowest Prices per year

4) List of Prices, Lowest to Highest: 
     - Will generate a txt file that list the dates and prices, sorted from 
       lowest to highest
       
5) List of Prices, Highest to Lowest:
     - Will generate a txt file that list the dates and prices, sorted from 
       highest to lowest
'''
import math

# ====================  Main function to run program  ==========================
print('\n---------------------------  Gas Prices  --------------------------')
print('                                                                 ')
print('  This program will prompt a menu for you to choose between five ')
print('  options. This program uses data for gas prices for every week  ')
print('  between the years 1993-2013.                                   ')
print('                                                                 ')


def main():
    again = True
    while again == True:    
        try:
            file = open('GasPrices.txt', 'r')   # Open the file to read 
            contents = file.readlines()         # Creating file object
            file.close()                        # Close file
        
            # Stripping the Newline
            for i in range(len(contents)):
                contents[i] = contents[i].rstrip('\n') 
        
        
            # Presenting the Main Menu to the User   
            print('\t  ---------------- Main Menu -------------------- ')
            print('\t      [1] Average Gas Prices Per Year            ')
            print('\t      [2] Average Gas Prices Per Month           ')
            print('\t      [3] Highest and Lowest Gas Prices Per Year ')
            print('\t      [4] List of Gas Prices Lowest - Highest    ')
            print('\t      [5] List of Gas Prices Highest - Lowest    ')
            print('\t                                                 ')
            
            choice = int(input('\n\t\tYour Choice: '))            

            if choice == 1:
                avg_per_year(contents)
            
            elif choice == 2:
                # Presenting the Average Monthly Price Menu to the User   
                print('\n\t  -------------------- Menu ---------------------- ')
                print('\t  Choose a year to view monthly average gas prices   ')
                print('\n\t      [1]   1993                                   ')
                print('\t      [2]   1994                                   ')
                print('\t      [3]   1995                                   ')
                print('\t      [4]   1996                                   ')
                print('\t      [5]   1997                                   ')
                print('\t      [6]   1998                                   ')
                print('\t      [7]   1999                                   ')
                print('\t      [8]   2000                                   ')
                print('\t      [9]   2001                                   ')
                print('\t      [10]  2002                                   ')
                print('\t      [11]  2003                                   ')
                print('\t      [12]  2004                                   ')
                print('\t      [13]  2005                                   ')
                print('\t      [14]  2006                                   ')
                print('\t      [15]  2007                                   ')
                print('\t      [16]  2008                                   ')
                print('\t      [17]  2009                                   ')
                print('\t      [18]  2010                                   ')
                print('\t      [19]  2011                                   ')
                print('\t      [20]  2012                                   ')
                print('\t      [21]  2013                                   ')
                
                choice = int(input('\n\t  Your Choice: '))
                
                if choice == 1:
                    avg_per_month_1993(contents)
                elif choice == 2:
                    avg_per_month_1994(contents)
                elif choice == 3:
                    avg_per_month_1995(contents)
                elif choice == 4:
                    avg_per_month_1996(contents)
                elif choice == 5:
                    avg_per_month_1997(contents) 
                elif choice == 6:
                    avg_per_month_1998(contents)
                elif choice == 7:
                    avg_per_month_1999(contents) 
                elif choice == 8:
                    avg_per_month_2000(contents)
                elif choice == 9:
                    avg_per_month_2001(contents) 
                elif choice == 10:
                    avg_per_month_2002(contents)
                elif choice == 11:
                    avg_per_month_2003(contents) 
                elif choice == 12:
                    avg_per_month_2004(contents)
                elif choice == 13:
                    avg_per_month_2005(contents) 
                elif choice == 14:
                    avg_per_month_2006(contents)
                elif choice == 15:
                    avg_per_month_2007(contents) 
                elif choice == 16:
                    avg_per_month_2008(contents)
                elif choice == 17:
                    avg_per_month_2009(contents) 
                elif choice == 18:
                    avg_per_month_2010(contents)
                elif choice == 19:
                    avg_per_month_2011(contents) 
                elif choice == 20:
                    avg_per_month_2012(contents)
                elif choice == 21:
                    avg_per_month_2013(contents)
                elif choice > 5 or choice < 1:
                    print('\n------------------------- E R R O R --------------------------')  
                    print('You did not choose one of the Menu options. Review your')
                    print('choice, make sure you are choosing the menu option and')
                    print('not the year, and try again!.                         ')
                    print()
                    print()
                    main()                
            
            elif choice == 3:
                high_and_low_per_year(contents)     
            elif choice == 4:
                list_low_to_high(contents)   
            elif choice == 5:
                list_high_to_low(contents)          
            elif choice > 5 or choice < 1:
                print('\n------------------------- E R R O R --------------------------')  
                print('You did not choose one of the Menu options. Review your')
                print('choice, make sure you are choosing a menu option, and  ')
                print('try again!.                                            ')
                print()
                print()
                main()
        
            # Asking the user if they want to run program again
            print('\n\t  ---------------------------------------------- ')
            print('\n\t     Would you like to run the program again?')
            again = input('\t     Yes or No: ')
          
            if again.lower() == 'yes' or again.lower() == 'y':
                again = True
                print()
            elif again.lower() == 'no' or again.lower() == 'n':
                print('\n------------------------------------------------------------------')
                print('\n\t\tThank You! Have a Great Day!')
                print('\n------------------------------------------------------------------')
                again = False 
            else:
                print('\nYou did not enter either Yes or No. The program' +
                    ' will now end.')
                print('------------------------------------------------------------------')
                again = False             
                       
        except IOError:
            print('\n------------------------- E R R O R --------------------------')  
            print('An error occurred while trying to read the file.')
            print('Check the spelling of the file you are trying to open.')
        #except: 
            #print('An error occurred.')   
        
 
 
            
#                            ---  FUNCTIONS  ---

# ======  Converting the gas prices to floats and finding AVERAGE PER YEAR  ====

def avg_per_year(contents):
    print('\n---------------  The Average Price of Gas Per Year  ---------------')
    
    # 1993
    total = 0
    prices93 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1993': # slicing the string to match substring
            prices93.append(float(contents[i][11:])) # converting the price to float
    for i in range(len(prices93)): # adding all prices for total
        total += prices93[i]
    avg = total / len(prices93) # finding average
    print('1993 = $' + format(avg, ',.3f'))

    # 1994
    total = 0
    prices94 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1994':
            prices94.append(float(contents[i][11:]))
    for i in range(len(prices94)):
        total += prices94[i]
    avg = total / len(prices94)
    print('1994 = $' + format(avg, ',.3f'))       

    # 1995
    total = 0
    prices95 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1995':
            prices95.append(float(contents[i][11:]))
    for i in range(len(prices95)):
        total += prices95[i]
    avg = total / len(prices95)
    print('1995 = $' + format(avg, ',.3f')) 

    # 1996
    total = 0
    prices96 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1996':
            prices96.append(float(contents[i][11:]))
    for i in range(len(prices96)):
        total += prices96[i]
    avg = total / len(prices96)
    print('1996 = $' + format(avg, ',.3f'))
    
    # 1997
    total = 0
    prices97 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1997':
            prices97.append(float(contents[i][11:]))
    for i in range(len(prices97)):
        total += prices97[i]
    avg = total / len(prices97)
    print('1997 = $' + format(avg, ',.3f'))  
    
    # 1998
    total = 0
    prices98 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1998':
            prices98.append(float(contents[i][11:]))
    for i in range(len(prices98)):
        total += prices98[i]
    avg = total / len(prices98)
    print('1998 = $' + format(avg, ',.3f'))   

    # 1999
    total = 0
    prices99 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1999':
            prices99.append(float(contents[i][11:]))
    for i in range(len(prices99)):
        total += prices99[i]
    avg = total / len(prices99)
    print('1999 = $' + format(avg, ',.3f'))   

    # 2000
    total = 0
    prices00 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2000':
            prices00.append(float(contents[i][11:]))
    for i in range(len(prices00)):
        total += prices00[i]
    avg = total / len(prices00)
    print('2000 = $' + format(avg, ',.3f'))    

    # 2001
    total = 0
    prices01 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2001':
            prices01.append(float(contents[i][11:]))
    for i in range(len(prices01)):
        total += prices01[i]
    avg = total / len(prices01)
    print('2001 = $' + format(avg, ',.3f'))  

    # 2002
    total = 0
    prices02 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2002':
            prices02.append(float(contents[i][11:]))
    for i in range(len(prices02)):
        total += prices02[i]
    avg = total / len(prices02)
    print('2002 = $' + format(avg, ',.3f'))
    
    # 2003
    total = 0
    prices03 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2003':
            prices03.append(float(contents[i][11:]))
    for i in range(len(prices03)):
        total += prices03[i]
    avg = total / len(prices03)
    print('2003 = $' + format(avg, ',.3f'))    

    # 2004
    total = 0
    prices04 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2004':
            prices04.append(float(contents[i][11:]))
    for i in range(len(prices04)):
        total += prices04[i]
    avg = total / len(prices04)
    print('2004 = $' + format(avg, ',.3f')) 

    # 2005
    total = 0
    prices05 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2005':
            prices05.append(float(contents[i][11:]))
    for i in range(len(prices05)):
        total += prices05[i]
    avg = total / len(prices05)
    print('2005 = $' + format(avg, ',.3f'))
    
    # 2006
    total = 0
    prices06 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2006':
            prices06.append(float(contents[i][11:]))
    for i in range(len(prices06)):
        total += prices06[i]
    avg = total / len(prices06)
    print('2006 = $' + format(avg, ',.3f'))    

    # 2007
    total = 0
    prices07 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2007':
            prices07.append(float(contents[i][11:]))
    for i in range(len(prices07)):
        total += prices07[i]
    avg = total / len(prices07)
    print('2007 = $' + format(avg, ',.3f'))   

    # 2008
    total = 0
    prices08 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2008':
            prices08.append(float(contents[i][11:]))
    for i in range(len(prices08)):
        total += prices08[i]
    avg = total / len(prices08)
    print('2008 = $' + format(avg, ',.3f'))  

    # 2009
    total = 0
    prices09 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2009':
            prices09.append(float(contents[i][11:]))
    for i in range(len(prices09)):
        total += prices09[i]
    avg = total / len(prices09)
    print('2009 = $' + format(avg, ',.3f'))    

    # 2010
    total = 0
    prices10 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2010':
            prices10.append(float(contents[i][11:]))
    for i in range(len(prices10)):
        total += prices10[i]
    avg = total / len(prices10)
    print('2010 = $' + format(avg, ',.3f'))   

    # 2011
    total = 0
    prices11 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2011':
            prices11.append(float(contents[i][11:]))
    for i in range(len(prices11)):
        total += prices11[i]
    avg = total / len(prices11)
    print('2011 = $' + format(avg, ',.3f')) 

    # 2012
    total = 0
    prices12 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2012':
            prices12.append(float(contents[i][11:]))
    for i in range(len(prices12)):
        total += prices12[i]
    avg = total / len(prices12)
    print('2012 = $' + format(avg, ',.3f'))    

    # 2013
    total = 0
    prices13 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2013':
            prices13.append(float(contents[i][11:]))
    for i in range(len(prices13)):
        total += prices13[i]
    avg = total / len(prices13)
    print('2013 = $' + format(avg, ',.3f'))     


# ==========================  Average Per Month 1993 ===========================

def avg_per_month_1993(contents):
    print('\n---------------  The Average Price of Gas Per Month in 1993  ---------------')
    print('\nNOTE: 1993\'s data starts the week of April 5th.')
    # April 
    total = 0
    prices93 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1993' and contents[i][0:2] == '04': # slicing the string to match substrings
            prices93.append(float(contents[i][11:])) # converting the price to float
    for i in range(len(prices93)): # adding all prices for total
        total += prices93[i]
    avg = total / len(prices93) # finding average
    print('\nApril = $' + format(avg, ',.3f'))
    
    # May 
    total = 0
    prices93 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1993' and contents[i][0:2] == '05': 
            prices93.append(float(contents[i][11:])) 
    for i in range(len(prices93)): 
        total += prices93[i]
    avg = total / len(prices93) 
    print('May = $' + format(avg, ',.3f'))
    
    # June 
    total = 0
    prices93 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1993' and contents[i][0:2] == '06': 
            prices93.append(float(contents[i][11:])) 
    for i in range(len(prices93)): 
        total += prices93[i]
    avg = total / len(prices93) 
    print('June = $' + format(avg, ',.3f'))
    
    # July 
    total = 0
    prices93 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1993' and contents[i][0:2] == '07': 
            prices93.append(float(contents[i][11:])) 
    for i in range(len(prices93)): 
        total += prices93[i]
    avg = total / len(prices93) 
    print('July = $' + format(avg, ',.3f'))
    
    # August
    total = 0
    prices93 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1993' and contents[i][0:2] == '08': 
            prices93.append(float(contents[i][11:])) 
    for i in range(len(prices93)): 
        total += prices93[i]
    avg = total / len(prices93) 
    print('August = $' + format(avg, ',.3f'))
    
    # September 
    total = 0
    prices93 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1993' and contents[i][0:2] == '09': 
            prices93.append(float(contents[i][11:])) 
    for i in range(len(prices93)):
        total += prices93[i]
    avg = total / len(prices93) 
    print('September = $' + format(avg, ',.3f'))     
    
    # October 
    total = 0
    prices93 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1993' and contents[i][0:2] == '10':
            prices93.append(float(contents[i][11:])) 
    for i in range(len(prices93)): 
        total += prices93[i]
    avg = total / len(prices93) 
    print('October = $' + format(avg, ',.3f'))
    
    # November 
    total = 0
    prices93 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1993' and contents[i][0:2] == '11': 
            prices93.append(float(contents[i][11:])) 
    for i in range(len(prices93)): 
        total += prices93[i]
    avg = total / len(prices93) 
    print('November = $' + format(avg, ',.3f'))
    
    # December 
    total = 0
    prices93 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1993' and contents[i][0:2] == '12': 
            prices93.append(float(contents[i][11:])) 
    for i in range(len(prices93)): 
        total += prices93[i]
    avg = total / len(prices93) 
    print('December = $' + format(avg, ',.3f'))     

# ==========================  Average Per Month 1994 ===========================

def avg_per_month_1994(contents):
    print('\n---------------  The Average Price of Gas Per Month in 1994  ---------------')
    # January 
    total = 0
    prices94 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1994' and contents[i][0:2] == '01': 
            prices94.append(float(contents[i][11:])) 
    for i in range(len(prices94)): 
        total += prices94[i]
    avg = total / len(prices94) 
    print('January = $' + format(avg, ',.3f'))
    
    # February 
    total = 0
    prices94 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1994' and contents[i][0:2] == '02': 
            prices94.append(float(contents[i][11:])) 
    for i in range(len(prices94)): 
        total += prices94[i]
    avg = total / len(prices94) 
    print('February = $' + format(avg, ',.3f'))
    
    # March 
    total = 0
    prices94 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1994' and contents[i][0:2] == '03':
            prices94.append(float(contents[i][11:])) 
    for i in range(len(prices94)): 
        total += prices94[i]
    avg = total / len(prices94) 
    print('March = $' + format(avg, ',.3f'))
    
    # April 
    total = 0
    prices94 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1994' and contents[i][0:2] == '04': 
            prices94.append(float(contents[i][11:])) 
    for i in range(len(prices94)): 
        total += prices94[i]
    avg = total / len(prices94) 
    print('April = $' + format(avg, ',.3f'))
    
    # May 
    total = 0
    prices94 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1994' and contents[i][0:2] == '05': 
            prices94.append(float(contents[i][11:])) 
    for i in range(len(prices94)): 
        total += prices94[i]
    avg = total / len(prices94) 
    print('May = $' + format(avg, ',.3f'))
    
    # June 
    total = 0
    prices94 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1994' and contents[i][0:2] == '06': 
            prices94.append(float(contents[i][11:])) 
    for i in range(len(prices94)): 
        total += prices94[i]
    avg = total / len(prices94) 
    print('June = $' + format(avg, ',.3f'))     
    
    # July 
    total = 0
    prices94 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1994' and contents[i][0:2] == '07': 
            prices94.append(float(contents[i][11:])) 
    for i in range(len(prices94)): 
        total += prices94[i]
    avg = total / len(prices94) 
    print('July = $' + format(avg, ',.3f'))     

    # August 
    total = 0
    prices94 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1994' and contents[i][0:2] == '08': 
            prices94.append(float(contents[i][11:])) 
    for i in range(len(prices94)): 
        total += prices94[i]
    avg = total / len(prices94) 
    print('August = $' + format(avg, ',.3f'))     
    
    # September 
    total = 0
    prices94 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1994' and contents[i][0:2] == '05': 
            prices94.append(float(contents[i][11:])) 
    for i in range(len(prices94)): 
        total += prices94[i]
    avg = total / len(prices94) 
    print('September = $' + format(avg, ',.3f')) 
    
    # October 
    total = 0
    prices94 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1994' and contents[i][0:2] == '10': 
            prices94.append(float(contents[i][11:])) 
    for i in range(len(prices94)): 
        total += prices94[i]
    avg = total / len(prices94) 
    print('October = $' + format(avg, ',.3f'))
    
    # November 
    total = 0
    prices94 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1994' and contents[i][0:2] == '11': 
            prices94.append(float(contents[i][11:])) 
    for i in range(len(prices94)): 
        total += prices94[i]
    avg = total / len(prices94) 
    print('November = $' + format(avg, ',.3f')) 
    
    # December
    total = 0
    prices94 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1994' and contents[i][0:2] == '12': 
            prices94.append(float(contents[i][11:])) 
    for i in range(len(prices94)): 
        total += prices94[i]
    avg = total / len(prices94) 
    print('December = $' + format(avg, ',.3f'))

# ==========================  Average Per Month 1995 ===========================

def avg_per_month_1995(contents):
    print('\n---------------  The Average Price of Gas Per Month in 1995  ---------------')
    # January 
    total = 0
    prices95= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1995' and contents[i][0:2] == '01': 
            prices95.append(float(contents[i][11:])) 
    for i in range(len(prices95)): 
        total += prices95[i]
    avg = total / len(prices95) 
    print('January = $' + format(avg, ',.3f'))
    
    # February
    total = 0
    prices95 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1995' and contents[i][0:2] == '02': 
            prices95.append(float(contents[i][11:])) 
    for i in range(len(prices95)): 
        total += prices95[i]
    avg = total / len(prices95) 
    print('February = $' + format(avg, ',.3f'))
    
    # March 
    total = 0
    prices95 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1995' and contents[i][0:2] == '03': 
            prices95.append(float(contents[i][11:])) 
    for i in range(len(prices95)): 
        total += prices95[i]
    avg = total / len(prices95) 
    print('March = $' + format(avg, ',.3f'))
    
    # April
    total = 0
    prices95 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1995' and contents[i][0:2] == '04': 
            prices95.append(float(contents[i][11:])) 
    for i in range(len(prices95)): 
        total += prices95[i]
    avg = total / len(prices95) 
    print('April = $' + format(avg, ',.3f'))
    
    # May 
    total = 0
    prices95 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1995' and contents[i][0:2] == '05': 
            prices95.append(float(contents[i][11:])) 
    for i in range(len(prices95)): 
        total += prices95[i]
    avg = total / len(prices95) 
    print('May = $' + format(avg, ',.3f'))
    
    # June 
    total = 0
    prices95 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1995' and contents[i][0:2] == '06': 
            prices95.append(float(contents[i][11:])) 
    for i in range(len(prices95)): 
        total += prices95[i]
    avg = total / len(prices95) 
    print('June = $' + format(avg, ',.3f'))     
    
    # July 
    total = 0
    prices95 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1995' and contents[i][0:2] == '07': 
            prices95.append(float(contents[i][11:])) 
    for i in range(len(prices95)): 
        total += prices95[i]
    avg = total / len(prices95) 
    print('July = $' + format(avg, ',.3f'))     

    # August
    total = 0
    prices95 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1995' and contents[i][0:2] == '08': 
            prices95.append(float(contents[i][11:])) 
    for i in range(len(prices95)): 
        total += prices95[i]
    avg = total / len(prices95) 
    print('August = $' + format(avg, ',.3f'))     
    
    # September
    total = 0
    prices95 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1995' and contents[i][0:2] == '09': 
            prices95.append(float(contents[i][11:])) 
    for i in range(len(prices95)): 
        total += prices95[i]
    avg = total / len(prices95) 
    print('September = $' + format(avg, ',.3f')) 
    
    # October
    total = 0
    prices95 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1995' and contents[i][0:2] == '10': 
            prices95.append(float(contents[i][11:])) 
    for i in range(len(prices95)): 
        total += prices95[i]
    avg = total / len(prices95) 
    print('October = $' + format(avg, ',.3f'))
    
    # November
    total = 0
    prices95 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1995' and contents[i][0:2] == '11': 
            prices95.append(float(contents[i][11:])) 
    for i in range(len(prices95)): 
        total += prices95[i]
    avg = total / len(prices95) 
    print('November = $' + format(avg, ',.3f')) 
    
    # December 
    total = 0
    prices95 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1995' and contents[i][0:2] == '12': 
            prices95.append(float(contents[i][11:])) 
    for i in range(len(prices95)): 
        total += prices95[i]
    avg = total / len(prices95) 
    print('December = $' + format(avg, ',.3f'))

# ==========================  Average Per Month 1996 ===========================

def avg_per_month_1996(contents):
    print('\n---------------  The Average Price of Gas Per Month in 1996  ---------------')
    # January 
    total = 0
    prices96= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1996' and contents[i][0:2] == '01': 
            prices96.append(float(contents[i][11:])) 
    for i in range(len(prices96)): 
        total += prices96[i]
    avg = total / len(prices96) 
    print('January = $' + format(avg, ',.3f'))
    
    # February
    total = 0
    prices96= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1996' and contents[i][0:2] == '02': 
            prices96.append(float(contents[i][11:])) 
    for i in range(len(prices96)): 
        total += prices96[i]
    avg = total / len(prices96) 
    print('February = $' + format(avg, ',.3f'))
    
    # March 
    total = 0
    prices96= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1996' and contents[i][0:2] == '03': 
            prices96.append(float(contents[i][11:])) 
    for i in range(len(prices96)): 
        total += prices96[i]
    avg = total / len(prices96) 
    print('March = $' + format(avg, ',.3f'))
    
    # April
    total = 0
    prices96= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1996' and contents[i][0:2] == '04': 
            prices96.append(float(contents[i][11:])) 
    for i in range(len(prices96)): 
        total += prices96[i]
    avg = total / len(prices96) 
    print('April = $' + format(avg, ',.3f'))
    
    # May 
    total = 0
    prices96= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1996' and contents[i][0:2] == '05': 
            prices96.append(float(contents[i][11:])) 
    for i in range(len(prices96)): 
        total += prices96[i]
    avg = total / len(prices96) 
    print('May = $' + format(avg, ',.3f'))
    
    # June 
    total = 0
    prices96= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1996' and contents[i][0:2] == '06': 
            prices96.append(float(contents[i][11:])) 
    for i in range(len(prices96)): 
        total += prices96[i]
    avg = total / len(prices96) 
    print('June = $' + format(avg, ',.3f'))     
    
    # July 
    total = 0
    prices96= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1996' and contents[i][0:2] == '07': 
            prices96.append(float(contents[i][11:])) 
    for i in range(len(prices96)): 
        total += prices96[i]
    avg = total / len(prices96) 
    print('July = $' + format(avg, ',.3f'))     

    # August
    total = 0
    prices96= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1996' and contents[i][0:2] == '08': 
            prices96.append(float(contents[i][11:])) 
    for i in range(len(prices96)): 
        total += prices96[i]
    avg = total / len(prices96) 
    print('August = $' + format(avg, ',.3f'))     
    
    # September
    total = 0
    prices96= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1996' and contents[i][0:2] == '09': 
            prices96.append(float(contents[i][11:])) 
    for i in range(len(prices96)): 
        total += prices96[i]
    avg = total / len(prices96) 
    print('September = $' + format(avg, ',.3f')) 
    
    # October
    total = 0
    prices96= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1996' and contents[i][0:2] == '10': 
            prices96.append(float(contents[i][11:])) 
    for i in range(len(prices96)): 
        total += prices96[i]
    avg = total / len(prices96) 
    print('October = $' + format(avg, ',.3f'))
    
    # November
    total = 0
    prices96= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1996' and contents[i][0:2] == '11': 
            prices96.append(float(contents[i][11:])) 
    for i in range(len(prices96)): 
        total += prices96[i]
    avg = total / len(prices96) 
    print('November = $' + format(avg, ',.3f')) 
    
    # December 
    total = 0
    prices96= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1996' and contents[i][0:2] == '12': 
            prices96.append(float(contents[i][11:])) 
    for i in range(len(prices96)): 
        total += prices96[i]
    avg = total / len(prices96) 
    print('December = $' + format(avg, ',.3f'))

# ==========================  Average Per Month 1997 ===========================

def avg_per_month_1997(contents):
    print('\n---------------  The Average Price of Gas Per Month in 1997  ---------------')
    # January 
    total = 0
    prices97= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1997' and contents[i][0:2] == '01': 
            prices97.append(float(contents[i][11:])) 
    for i in range(len(prices97)): 
        total += prices97[i]
    avg = total / len(prices97) 
    print('January = $' + format(avg, ',.3f'))
    
    # February
    total = 0
    prices97= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1997' and contents[i][0:2] == '02': 
            prices97.append(float(contents[i][11:])) 
    for i in range(len(prices97)): 
        total += prices97[i]
    avg = total / len(prices97) 
    print('February = $' + format(avg, ',.3f'))
    
    # March 
    total = 0
    prices97= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1997' and contents[i][0:2] == '03': 
            prices97.append(float(contents[i][11:])) 
    for i in range(len(prices97)): 
        total += prices97[i]
    avg = total / len(prices97) 
    print('March = $' + format(avg, ',.3f'))
    
    # April
    total = 0
    prices97= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1997' and contents[i][0:2] == '04': 
            prices97.append(float(contents[i][11:])) 
    for i in range(len(prices97)): 
        total += prices97[i]
    avg = total / len(prices97) 
    print('April = $' + format(avg, ',.3f'))
    
    # May 
    total = 0
    prices97= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1997' and contents[i][0:2] == '05': 
            prices97.append(float(contents[i][11:])) 
    for i in range(len(prices97)): 
        total += prices97[i]
    avg = total / len(prices97) 
    print('May = $' + format(avg, ',.3f'))
    
    # June 
    total = 0
    prices97= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1997' and contents[i][0:2] == '06': 
            prices97.append(float(contents[i][11:])) 
    for i in range(len(prices97)): 
        total += prices97[i]
    avg = total / len(prices97) 
    print('June = $' + format(avg, ',.3f'))     
    
    # July 
    total = 0
    prices97= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1997' and contents[i][0:2] == '07': 
            prices97.append(float(contents[i][11:])) 
    for i in range(len(prices97)): 
        total += prices97[i]
    avg = total / len(prices97) 
    print('July = $' + format(avg, ',.3f'))     

    # August
    total = 0
    prices97= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1997' and contents[i][0:2] == '08': 
            prices97.append(float(contents[i][11:])) 
    for i in range(len(prices97)): 
        total += prices97[i]
    avg = total / len(prices97) 
    print('August = $' + format(avg, ',.3f'))     
    
    # September
    total = 0
    prices97= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1997' and contents[i][0:2] == '09': 
            prices97.append(float(contents[i][11:])) 
    for i in range(len(prices97)): 
        total += prices97[i]
    avg = total / len(prices97) 
    print('September = $' + format(avg, ',.3f')) 
    
    # October
    total = 0
    prices97= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1997' and contents[i][0:2] == '10': 
            prices97.append(float(contents[i][11:])) 
    for i in range(len(prices97)): 
        total += prices97[i]
    avg = total / len(prices97) 
    print('October = $' + format(avg, ',.3f'))
    
    # November
    total = 0
    prices97= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1997' and contents[i][0:2] == '11': 
            prices97.append(float(contents[i][11:])) 
    for i in range(len(prices97)): 
        total += prices97[i]
    avg = total / len(prices97) 
    print('November = $' + format(avg, ',.3f')) 
    
    # December 
    total = 0
    prices97= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1997' and contents[i][0:2] == '12': 
            prices97.append(float(contents[i][11:])) 
    for i in range(len(prices97)): 
        total += prices97[i]
    avg = total / len(prices97) 
    print('December = $' + format(avg, ',.3f'))

# ==========================  Average Per Month 1998 ===========================

def avg_per_month_1998(contents):
    print('\n---------------  The Average Price of Gas Per Month in 1998  ---------------')
    # January 
    total = 0
    prices98= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1998' and contents[i][0:2] == '01': 
            prices98.append(float(contents[i][11:])) 
    for i in range(len(prices98)): 
        total += prices98[i]
    avg = total / len(prices98) 
    print('January = $' + format(avg, ',.3f'))
    
    # February
    total = 0
    prices98= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1998' and contents[i][0:2] == '02': 
            prices98.append(float(contents[i][11:])) 
    for i in range(len(prices98)): 
        total += prices98[i]
    avg = total / len(prices98) 
    print('February = $' + format(avg, ',.3f'))
    
    # March 
    total = 0
    prices98= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1998' and contents[i][0:2] == '03': 
            prices98.append(float(contents[i][11:])) 
    for i in range(len(prices98)): 
        total += prices98[i]
    avg = total / len(prices98) 
    print('March = $' + format(avg, ',.3f'))
    
    # April
    total = 0
    prices98= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1998' and contents[i][0:2] == '04': 
            prices98.append(float(contents[i][11:])) 
    for i in range(len(prices98)): 
        total += prices98[i]
    avg = total / len(prices98) 
    print('April = $' + format(avg, ',.3f'))
    
    # May 
    total = 0
    prices98= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1998' and contents[i][0:2] == '05': 
            prices98.append(float(contents[i][11:])) 
    for i in range(len(prices98)): 
        total += prices98[i]
    avg = total / len(prices98) 
    print('May = $' + format(avg, ',.3f'))
    
    # June 
    total = 0
    prices98= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1998' and contents[i][0:2] == '06': 
            prices98.append(float(contents[i][11:])) 
    for i in range(len(prices98)): 
        total += prices98[i]
    avg = total / len(prices98) 
    print('June = $' + format(avg, ',.3f'))     
    
    # July 
    total = 0
    prices98= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1998' and contents[i][0:2] == '07': 
            prices98.append(float(contents[i][11:])) 
    for i in range(len(prices98)): 
        total += prices98[i]
    avg = total / len(prices98) 
    print('July = $' + format(avg, ',.3f'))     

    # August
    total = 0
    prices98= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1998' and contents[i][0:2] == '08': 
            prices98.append(float(contents[i][11:])) 
    for i in range(len(prices98)): 
        total += prices98[i]
    avg = total / len(prices98) 
    print('August = $' + format(avg, ',.3f'))     
    
    # September
    total = 0
    prices98= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1998' and contents[i][0:2] == '09': 
            prices98.append(float(contents[i][11:])) 
    for i in range(len(prices98)): 
        total += prices98[i]
    avg = total / len(prices98) 
    print('September = $' + format(avg, ',.3f')) 
    
    # October
    total = 0
    prices98= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1998' and contents[i][0:2] == '10': 
            prices98.append(float(contents[i][11:])) 
    for i in range(len(prices98)): 
        total += prices98[i]
    avg = total / len(prices98) 
    print('October = $' + format(avg, ',.3f'))
    
    # November
    total = 0
    prices98= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1998' and contents[i][0:2] == '11': 
            prices98.append(float(contents[i][11:])) 
    for i in range(len(prices98)): 
        total += prices98[i]
    avg = total / len(prices98) 
    print('November = $' + format(avg, ',.3f')) 
    
    # December 
    total = 0
    prices98= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1998' and contents[i][0:2] == '12': 
            prices98.append(float(contents[i][11:])) 
    for i in range(len(prices98)): 
        total += prices98[i]
    avg = total / len(prices98) 
    print('December = $' + format(avg, ',.3f'))
    
# ==========================  Average Per Month 1999 ===========================

def avg_per_month_1999(contents):
    print('\n---------------  The Average Price of Gas Per Month in 1999  ---------------')
    # January 
    total = 0
    prices99= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1999' and contents[i][0:2] == '01': 
            prices99.append(float(contents[i][11:])) 
    for i in range(len(prices99)): 
        total += prices99[i]
    avg = total / len(prices99) 
    print('January = $' + format(avg, ',.3f'))
    
    # February
    total = 0
    prices99= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1999' and contents[i][0:2] == '02': 
            prices99.append(float(contents[i][11:])) 
    for i in range(len(prices99)): 
        total += prices99[i]
    avg = total / len(prices99) 
    print('February = $' + format(avg, ',.3f'))
    
    # March 
    total = 0
    prices99= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1999' and contents[i][0:2] == '03': 
            prices99.append(float(contents[i][11:])) 
    for i in range(len(prices99)): 
        total += prices99[i]
    avg = total / len(prices99) 
    print('March = $' + format(avg, ',.3f'))
    
    # April
    total = 0
    prices99= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1999' and contents[i][0:2] == '04': 
            prices99.append(float(contents[i][11:])) 
    for i in range(len(prices99)): 
        total += prices99[i]
    avg = total / len(prices99) 
    print('April = $' + format(avg, ',.3f'))
    
    # May 
    total = 0
    prices99= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1999' and contents[i][0:2] == '05': 
            prices99.append(float(contents[i][11:])) 
    for i in range(len(prices99)): 
        total += prices99[i]
    avg = total / len(prices99) 
    print('May = $' + format(avg, ',.3f'))
    
    # June 
    total = 0
    prices99= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1999' and contents[i][0:2] == '06': 
            prices99.append(float(contents[i][11:])) 
    for i in range(len(prices99)): 
        total += prices99[i]
    avg = total / len(prices99) 
    print('June = $' + format(avg, ',.3f'))     
    
    # July 
    total = 0
    prices99= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1999' and contents[i][0:2] == '07': 
            prices99.append(float(contents[i][11:])) 
    for i in range(len(prices99)): 
        total += prices99[i]
    avg = total / len(prices99) 
    print('July = $' + format(avg, ',.3f'))     

    # August
    total = 0
    prices99= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1999' and contents[i][0:2] == '08': 
            prices99.append(float(contents[i][11:])) 
    for i in range(len(prices99)): 
        total += prices99[i]
    avg = total / len(prices99) 
    print('August = $' + format(avg, ',.3f'))     
    
    # September
    total = 0
    prices99= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1999' and contents[i][0:2] == '09': 
            prices99.append(float(contents[i][11:])) 
    for i in range(len(prices99)): 
        total += prices99[i]
    avg = total / len(prices99) 
    print('September = $' + format(avg, ',.3f')) 
    
    # October
    total = 0
    prices99= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1999' and contents[i][0:2] == '10': 
            prices99.append(float(contents[i][11:])) 
    for i in range(len(prices99)): 
        total += prices99[i]
    avg = total / len(prices99) 
    print('October = $' + format(avg, ',.3f'))
    
    # November
    total = 0
    prices99= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1999' and contents[i][0:2] == '11': 
            prices99.append(float(contents[i][11:])) 
    for i in range(len(prices99)): 
        total += prices99[i]
    avg = total / len(prices99)  
    print('November = $' + format(avg, ',.3f')) 
    
    # December 
    total = 0
    prices99= []
    for i in range(len(contents)):
        if contents[i][6:10] == '1999' and contents[i][0:2] == '12': 
            prices99.append(float(contents[i][11:])) 
    for i in range(len(prices99)): 
        total += prices99[i]
    avg = total / len(prices99) 
    print('December = $' + format(avg, ',.3f'))
    
# ==========================  Average Per Month 2000 ===========================

def avg_per_month_2000(contents):
    print('\n---------------  The Average Price of Gas Per Month in 2000  ---------------')
    # January 
    total = 0
    prices00= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2000' and contents[i][0:2] == '01': 
            prices00.append(float(contents[i][11:])) 
    for i in range(len(prices00)): 
        total += prices00[i]
    avg = total / len(prices00) 
    print('January = $' + format(avg, ',.3f'))
    
    # February
    total = 0
    prices00= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2000' and contents[i][0:2] == '02': 
            prices00.append(float(contents[i][11:])) 
    for i in range(len(prices00)): 
        total += prices00[i]
    avg = total / len(prices00) 
    print('February = $' + format(avg, ',.3f'))
    
    # March 
    total = 0
    prices00= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2000' and contents[i][0:2] == '03': 
            prices00.append(float(contents[i][11:])) 
    for i in range(len(prices00)): 
        total += prices00[i]
    avg = total / len(prices00) 
    print('March = $' + format(avg, ',.3f'))
    
    # April
    total = 0
    prices00= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2000' and contents[i][0:2] == '04': 
            prices00.append(float(contents[i][11:])) 
    for i in range(len(prices00)): 
        total += prices00[i]
    avg = total / len(prices00) 
    print('April = $' + format(avg, ',.3f'))
    
    # May 
    total = 0
    prices00= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2000' and contents[i][0:2] == '05': 
            prices00.append(float(contents[i][11:])) 
    for i in range(len(prices00)): 
        total += prices00[i]
    avg = total / len(prices00) 
    print('May = $' + format(avg, ',.3f'))
    
    # June 
    total = 0
    prices00= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2000' and contents[i][0:2] == '06': 
            prices00.append(float(contents[i][11:])) 
    for i in range(len(prices00)): 
        total += prices00[i]
    avg = total / len(prices00) 
    print('June = $' + format(avg, ',.3f'))     
    
    # July 
    total = 0
    prices00= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2000' and contents[i][0:2] == '07': 
            prices00.append(float(contents[i][11:])) 
    for i in range(len(prices00)): 
        total += prices00[i]
    avg = total / len(prices00) 
    print('July = $' + format(avg, ',.3f'))     

    # August
    total = 0
    prices00= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2000' and contents[i][0:2] == '08': 
            prices00.append(float(contents[i][11:])) 
    for i in range(len(prices00)): 
        total += prices00[i]
    avg = total / len(prices00) 
    print('August = $' + format(avg, ',.3f'))     
    
    # September
    total = 0
    prices00= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2000' and contents[i][0:2] == '09': 
            prices00.append(float(contents[i][11:])) 
    for i in range(len(prices00)): 
        total += prices00[i]
    avg = total / len(prices00) 
    print('September = $' + format(avg, ',.3f')) 
    
    # October
    total = 0
    prices00= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2000' and contents[i][0:2] == '10': 
            prices00.append(float(contents[i][11:])) 
    for i in range(len(prices00)): 
        total += prices00[i]
    avg = total / len(prices00) 
    print('October = $' + format(avg, ',.3f'))
    
    # November
    total = 0
    prices00= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2000' and contents[i][0:2] == '11': 
            prices00.append(float(contents[i][11:])) 
    for i in range(len(prices00)): 
        total += prices00[i]
    avg = total / len(prices00) 
    print('November = $' + format(avg, ',.3f'))    
    
    # December 
    total = 0
    prices00= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2000' and contents[i][0:2] == '12': 
            prices00.append(float(contents[i][11:])) 
    for i in range(len(prices00)): 
        total += prices00[i]
    avg = total / len(prices00) 
    print('December = $' + format(avg, ',.3f'))
    
# ==========================  Average Per Month 2001 ===========================

def avg_per_month_2001(contents):
    print('\n---------------  The Average Price of Gas Per Month in 2001  ---------------')
    # January 
    total = 0
    prices01= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2001' and contents[i][0:2] == '01': 
            prices01.append(float(contents[i][11:])) 
    for i in range(len(prices01)): 
        total += prices01[i]
    avg = total / len(prices01) 
    print('January = $' + format(avg, ',.3f'))
    
    # February
    total = 0
    prices01= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2001' and contents[i][0:2] == '02': 
            prices01.append(float(contents[i][11:])) 
    for i in range(len(prices01)): 
        total += prices01[i]
    avg = total / len(prices01) 
    print('February = $' + format(avg, ',.3f'))
    
    # March 
    total = 0
    prices01= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2001' and contents[i][0:2] == '03': 
            prices01.append(float(contents[i][11:])) 
    for i in range(len(prices01)): 
        total += prices01[i]
    avg = total / len(prices01) 
    print('March = $' + format(avg, ',.3f'))
    
    # April
    total = 0
    prices01= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2001' and contents[i][0:2] == '04': 
            prices01.append(float(contents[i][11:])) 
    for i in range(len(prices01)): 
        total += prices01[i]
    avg = total / len(prices01) 
    print('April = $' + format(avg, ',.3f'))
    
    # May 
    total = 0
    prices01= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2001' and contents[i][0:2] == '05': 
            prices01.append(float(contents[i][11:])) 
    for i in range(len(prices01)): 
        total += prices01[i]
    avg = total / len(prices01) 
    print('May = $' + format(avg, ',.3f'))
    
    # June 
    total = 0
    prices01= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2001' and contents[i][0:2] == '06': 
            prices01.append(float(contents[i][11:])) 
    for i in range(len(prices01)): 
        total += prices01[i]
    avg = total / len(prices01) 
    print('June = $' + format(avg, ',.3f'))     
    
    # July 
    total = 0
    prices01= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2001' and contents[i][0:2] == '07': 
            prices01.append(float(contents[i][11:])) 
    for i in range(len(prices01)): 
        total += prices01[i]
    avg = total / len(prices01) 
    print('July = $' + format(avg, ',.3f'))     

    # August
    total = 0
    prices01= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2001' and contents[i][0:2] == '08': 
            prices01.append(float(contents[i][11:])) 
    for i in range(len(prices01)): 
        total += prices01[i]
    avg = total / len(prices01)  
    print('August = $' + format(avg, ',.3f'))     
    
    # September
    total = 0
    prices01= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2001' and contents[i][0:2] == '09': 
            prices01.append(float(contents[i][11:])) 
    for i in range(len(prices01)): 
        total += prices01[i]
    avg = total / len(prices01) 
    print('September = $' + format(avg, ',.3f')) 
    
    # October
    total = 0
    prices01= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2001' and contents[i][0:2] == '10': 
            prices01.append(float(contents[i][11:])) 
    for i in range(len(prices01)): 
        total += prices01[i]
    avg = total / len(prices01) 
    print('October = $' + format(avg, ',.3f'))
    
    # November
    total = 0
    prices01= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2001' and contents[i][0:2] == '11': 
            prices01.append(float(contents[i][11:])) 
    for i in range(len(prices01)): 
        total += prices01[i]
    avg = total / len(prices01) 
    print('November = $' + format(avg, ',.3f'))    
    
    # December 
    total = 0
    prices01= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2001' and contents[i][0:2] == '12': 
            prices01.append(float(contents[i][11:])) 
    for i in range(len(prices01)): 
        total += prices01[i]
    avg = total / len(prices01) 
    print('December = $' + format(avg, ',.3f'))

# ==========================  Average Per Month 2002 ===========================

def avg_per_month_2002(contents):
    print('\n---------------  The Average Price of Gas Per Month in 2002  ---------------')
    # January 
    total = 0
    prices02= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2002' and contents[i][0:2] == '01': 
            prices02.append(float(contents[i][11:])) 
    for i in range(len(prices02)): 
        total += prices02[i]
    avg = total / len(prices02) 
    print('January = $' + format(avg, ',.3f'))
    
    # February
    total = 0
    prices02= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2002' and contents[i][0:2] == '02': 
            prices02.append(float(contents[i][11:])) 
    for i in range(len(prices02)): 
        total += prices02[i]
    avg = total / len(prices02) 
    print('February = $' + format(avg, ',.3f'))
    
    # March 
    total = 0
    prices02= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2002' and contents[i][0:2] == '03': 
            prices02.append(float(contents[i][11:])) 
    for i in range(len(prices02)): 
        total += prices02[i]
    avg = total / len(prices02) 
    print('March = $' + format(avg, ',.3f'))
    
    # April
    total = 0
    prices02= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2002' and contents[i][0:2] == '04': 
            prices02.append(float(contents[i][11:])) 
    for i in range(len(prices02)): 
        total += prices02[i]
    avg = total / len(prices02)  
    print('April = $' + format(avg, ',.3f'))
    
    # May 
    total = 0
    prices02= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2002' and contents[i][0:2] == '05': 
            prices02.append(float(contents[i][11:])) 
    for i in range(len(prices02)): 
        total += prices02[i]
    avg = total / len(prices02) 
    print('May = $' + format(avg, ',.3f'))
    
    # June 
    total = 0
    prices02= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2002' and contents[i][0:2] == '06': 
            prices02.append(float(contents[i][11:])) 
    for i in range(len(prices02)): 
        total += prices02[i]
    avg = total / len(prices02)  
    print('June = $' + format(avg, ',.3f'))     
    
    # July 
    total = 0
    prices02= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2002' and contents[i][0:2] == '07': 
            prices02.append(float(contents[i][11:])) 
    for i in range(len(prices02)): 
        total += prices02[i]
    avg = total / len(prices02) 
    print('July = $' + format(avg, ',.3f'))     

    # August
    total = 0
    prices02= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2002' and contents[i][0:2] == '08': 
            prices02.append(float(contents[i][11:])) 
    for i in range(len(prices02)): 
        total += prices02[i]
    avg = total / len(prices02)   
    print('August = $' + format(avg, ',.3f'))     
    
    # September
    total = 0
    prices02= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2002' and contents[i][0:2] == '09': 
            prices02.append(float(contents[i][11:])) 
    for i in range(len(prices02)): 
        total += prices02[i]
    avg = total / len(prices02)
    print('September = $' + format(avg, ',.3f')) 
    
    # October
    total = 0
    prices02= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2002' and contents[i][0:2] == '10': 
            prices02.append(float(contents[i][11:])) 
    for i in range(len(prices02)): 
        total += prices02[i]
    avg = total / len(prices02) 
    print('October = $' + format(avg, ',.3f'))
    
    # November
    total = 0
    prices02= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2002' and contents[i][0:2] == '11': 
            prices02.append(float(contents[i][11:])) 
    for i in range(len(prices02)): 
        total += prices02[i]
    avg = total / len(prices02) 
    print('November = $' + format(avg, ',.3f'))    
    
    # December 
    total = 0
    prices02= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2002' and contents[i][0:2] == '12': 
            prices02.append(float(contents[i][11:])) 
    for i in range(len(prices02)): 
        total += prices02[i]
    avg = total / len(prices02)  
    print('December = $' + format(avg, ',.3f'))

# ==========================  Average Per Month 2003 ===========================

def avg_per_month_2003(contents):
    print('\n---------------  The Average Price of Gas Per Month in 2003  ---------------')
    # January 
    total = 0
    prices03= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2003' and contents[i][0:2] == '01': 
            prices03.append(float(contents[i][11:])) 
    for i in range(len(prices03)): 
        total += prices03[i]
    avg = total / len(prices03) 
    print('January = $' + format(avg, ',.3f'))
    
    # February
    total = 0
    prices03= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2003' and contents[i][0:2] == '02': 
            prices03.append(float(contents[i][11:])) 
    for i in range(len(prices03)): 
        total += prices03[i]
    avg = total / len(prices03)
    print('February = $' + format(avg, ',.3f'))
    
    # March 
    total = 0
    prices03= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2003' and contents[i][0:2] == '03': 
            prices03.append(float(contents[i][11:])) 
    for i in range(len(prices03)): 
        total += prices03[i]
    avg = total / len(prices03)
    print('March = $' + format(avg, ',.3f'))
    
    # April
    total = 0
    prices03= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2003' and contents[i][0:2] == '04': 
            prices03.append(float(contents[i][11:])) 
    for i in range(len(prices03)): 
        total += prices03[i]
    avg = total / len(prices03) 
    print('April = $' + format(avg, ',.3f'))
    
    # May 
    total = 0
    prices03= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2003' and contents[i][0:2] == '05': 
            prices03.append(float(contents[i][11:])) 
    for i in range(len(prices03)): 
        total += prices03[i]
    avg = total / len(prices03) 
    print('May = $' + format(avg, ',.3f'))
    
    # June 
    total = 0
    prices03= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2003' and contents[i][0:2] == '06': 
            prices03.append(float(contents[i][11:])) 
    for i in range(len(prices03)): 
        total += prices03[i]
    avg = total / len(prices03) 
    print('June = $' + format(avg, ',.3f'))     
    
    # July 
    total = 0
    prices03= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2003' and contents[i][0:2] == '07': 
            prices03.append(float(contents[i][11:])) 
    for i in range(len(prices03)): 
        total += prices03[i]
    avg = total / len(prices03)
    print('July = $' + format(avg, ',.3f'))     

    # August
    total = 0
    prices03= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2003' and contents[i][0:2] == '08': 
            prices03.append(float(contents[i][11:])) 
    for i in range(len(prices03)): 
        total += prices03[i]
    avg = total / len(prices03)  
    print('August = $' + format(avg, ',.3f'))     
    
    # September
    total = 0
    prices03= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2003' and contents[i][0:2] == '09': 
            prices03.append(float(contents[i][11:])) 
    for i in range(len(prices03)): 
        total += prices03[i]
    avg = total / len(prices03)
    print('September = $' + format(avg, ',.3f')) 
    
    # October
    total = 0
    prices03= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2003' and contents[i][0:2] == '10': 
            prices03.append(float(contents[i][11:])) 
    for i in range(len(prices03)): 
        total += prices03[i]
    avg = total / len(prices03)
    print('October = $' + format(avg, ',.3f'))
    
    # November
    total = 0
    prices03= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2003' and contents[i][0:2] == '11': 
            prices03.append(float(contents[i][11:])) 
    for i in range(len(prices03)): 
        total += prices03[i]
    avg = total / len(prices03)
    print('November = $' + format(avg, ',.3f'))    
    
    # December 
    total = 0
    prices03= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2003' and contents[i][0:2] == '12': 
            prices03.append(float(contents[i][11:])) 
    for i in range(len(prices03)): 
        total += prices03[i]
    avg = total / len(prices03) 
    print('December = $' + format(avg, ',.3f'))    

# ==========================  Average Per Month 2004 ===========================

def avg_per_month_2004(contents):
    print('\n---------------  The Average Price of Gas Per Month in 2004  ---------------')
    # January 
    total = 0
    prices04= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2004' and contents[i][0:2] == '01': 
            prices04.append(float(contents[i][11:])) 
    for i in range(len(prices04)): 
        total += prices04[i]
    avg = total / len(prices04) 
    print('January = $' + format(avg, ',.3f'))
    
    # February
    total = 0
    prices04= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2004' and contents[i][0:2] == '02': 
            prices04.append(float(contents[i][11:])) 
    for i in range(len(prices04)): 
        total += prices04[i]
    avg = total / len(prices04) 
    print('February = $' + format(avg, ',.3f'))
    
    # March 
    total = 0
    prices04= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2004' and contents[i][0:2] == '03': 
            prices04.append(float(contents[i][11:])) 
    for i in range(len(prices04)): 
        total += prices04[i]
    avg = total / len(prices04) 
    print('March = $' + format(avg, ',.3f'))
    
    # April
    total = 0
    prices04= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2004' and contents[i][0:2] == '04': 
            prices04.append(float(contents[i][11:])) 
    for i in range(len(prices04)): 
        total += prices04[i]
    avg = total / len(prices04) 
    print('April = $' + format(avg, ',.3f'))
    
    # May 
    total = 0
    prices04= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2004' and contents[i][0:2] == '05': 
            prices04.append(float(contents[i][11:])) 
    for i in range(len(prices04)): 
        total += prices04[i]
    avg = total / len(prices04) 
    print('May = $' + format(avg, ',.3f'))
    
    # June 
    total = 0
    prices04= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2004' and contents[i][0:2] == '06': 
            prices04.append(float(contents[i][11:])) 
    for i in range(len(prices04)): 
        total += prices04[i]
    avg = total / len(prices04) 
    print('June = $' + format(avg, ',.3f'))     
    
    # July 
    total = 0
    prices04= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2004' and contents[i][0:2] == '07': 
            prices04.append(float(contents[i][11:])) 
    for i in range(len(prices04)): 
        total += prices04[i]
    avg = total / len(prices04) 
    print('July = $' + format(avg, ',.3f'))     

    # August
    total = 0
    prices04= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2004' and contents[i][0:2] == '08': 
            prices04.append(float(contents[i][11:])) 
    for i in range(len(prices04)): 
        total += prices04[i]
    avg = total / len(prices04)  
    print('August = $' + format(avg, ',.3f'))     
    
    # September
    total = 0
    prices04= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2004' and contents[i][0:2] == '09': 
            prices04.append(float(contents[i][11:])) 
    for i in range(len(prices04)): 
        total += prices04[i]
    avg = total / len(prices04) 
    print('September = $' + format(avg, ',.3f')) 
    
    # October
    total = 0
    prices04= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2004' and contents[i][0:2] == '10': 
            prices04.append(float(contents[i][11:])) 
    for i in range(len(prices04)): 
        total += prices04[i]
    avg = total / len(prices04) 
    print('October = $' + format(avg, ',.3f'))
    
    # November
    total = 0
    prices04= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2004' and contents[i][0:2] == '11': 
            prices04.append(float(contents[i][11:])) 
    for i in range(len(prices04)): 
        total += prices04[i]
    avg = total / len(prices04) 
    print('November = $' + format(avg, ',.3f'))    
    
    # December 
    total = 0
    prices04= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2004' and contents[i][0:2] == '12': 
            prices04.append(float(contents[i][11:])) 
    for i in range(len(prices04)): 
        total += prices04[i]
    avg = total / len(prices04)  
    print('December = $' + format(avg, ',.3f'))   
    
# ==========================  Average Per Month 2005 ===========================

def avg_per_month_2005(contents):
    print('\n---------------  The Average Price of Gas Per Month in 2005  ---------------')
    # January 
    total = 0
    prices05= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2005' and contents[i][0:2] == '01': 
            prices05.append(float(contents[i][11:])) 
    for i in range(len(prices05)): 
        total += prices05[i]
    avg = total / len(prices05) 
    print('January = $' + format(avg, ',.3f'))
    
    # February
    total = 0
    prices05= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2005' and contents[i][0:2] == '02': 
            prices05.append(float(contents[i][11:])) 
    for i in range(len(prices05)): 
        total += prices05[i]
    avg = total / len(prices05) 
    print('February = $' + format(avg, ',.3f'))
    
    # March 
    total = 0
    prices05= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2005' and contents[i][0:2] == '03': 
            prices05.append(float(contents[i][11:])) 
    for i in range(len(prices05)): 
        total += prices05[i]
    avg = total / len(prices05) 
    print('March = $' + format(avg, ',.3f'))
    
    # April
    total = 0
    prices05= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2005' and contents[i][0:2] == '04': 
            prices05.append(float(contents[i][11:])) 
    for i in range(len(prices05)): 
        total += prices05[i]
    avg = total / len(prices05) 
    print('April = $' + format(avg, ',.3f'))
    
    # May 
    total = 0
    prices05= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2005' and contents[i][0:2] == '05': 
            prices05.append(float(contents[i][11:])) 
    for i in range(len(prices05)): 
        total += prices05[i]
    avg = total / len(prices05) 
    print('May = $' + format(avg, ',.3f'))
    
    # June 
    total = 0
    prices05= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2005' and contents[i][0:2] == '06': 
            prices05.append(float(contents[i][11:])) 
    for i in range(len(prices05)): 
        total += prices05[i]
    avg = total / len(prices05) 
    print('June = $' + format(avg, ',.3f'))     
    
    # July 
    total = 0
    prices05= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2005' and contents[i][0:2] == '07': 
            prices05.append(float(contents[i][11:])) 
    for i in range(len(prices05)): 
        total += prices05[i]
    avg = total / len(prices05) 
    print('July = $' + format(avg, ',.3f'))     

    # August
    total = 0
    prices05= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2005' and contents[i][0:2] == '08': 
            prices05.append(float(contents[i][11:])) 
    for i in range(len(prices05)): 
        total += prices05[i]
    avg = total / len(prices05)   
    print('August = $' + format(avg, ',.3f'))     
    
    # September
    total = 0
    prices05= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2005' and contents[i][0:2] == '09': 
            prices05.append(float(contents[i][11:])) 
    for i in range(len(prices05)): 
        total += prices05[i]
    avg = total / len(prices05) 
    print('September = $' + format(avg, ',.3f')) 
    
    # October
    total = 0
    prices05= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2005' and contents[i][0:2] == '10': 
            prices05.append(float(contents[i][11:])) 
    for i in range(len(prices05)): 
        total += prices05[i]
    avg = total / len(prices05) 
    print('October = $' + format(avg, ',.3f'))
    
    # November
    total = 0
    prices05= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2005' and contents[i][0:2] == '11': 
            prices05.append(float(contents[i][11:])) 
    for i in range(len(prices05)): 
        total += prices05[i]
    avg = total / len(prices05) 
    print('November = $' + format(avg, ',.3f'))    
    
    # December 
    total = 0
    prices05= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2005' and contents[i][0:2] == '12': 
            prices05.append(float(contents[i][11:])) 
    for i in range(len(prices05)): 
        total += prices05[i]
    avg = total / len(prices05)   
    print('December = $' + format(avg, ',.3f'))

# ==========================  Average Per Month 2006 ===========================

def avg_per_month_2006(contents):
    print('\n---------------  The Average Price of Gas Per Month in 2006  ---------------')
    # January 
    total = 0
    prices06= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2006' and contents[i][0:2] == '01': 
            prices06.append(float(contents[i][11:])) 
    for i in range(len(prices06)): 
        total += prices06[i]
    avg = total / len(prices06) 
    print('January = $' + format(avg, ',.3f'))
    
    # February
    total = 0
    prices06= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2006' and contents[i][0:2] == '02': 
            prices06.append(float(contents[i][11:])) 
    for i in range(len(prices06)): 
        total += prices06[i]
    avg = total / len(prices06) 
    print('February = $' + format(avg, ',.3f'))
    
    # March 
    total = 0
    prices06= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2006' and contents[i][0:2] == '03': 
            prices06.append(float(contents[i][11:])) 
    for i in range(len(prices06)): 
        total += prices06[i]
    avg = total / len(prices06)  
    print('March = $' + format(avg, ',.3f'))
    
    # April
    total = 0
    prices06= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2006' and contents[i][0:2] == '04': 
            prices06.append(float(contents[i][11:])) 
    for i in range(len(prices06)): 
        total += prices06[i]
    avg = total / len(prices06) 
    print('April = $' + format(avg, ',.3f'))
    
    # May 
    total = 0
    prices06= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2006' and contents[i][0:2] == '05': 
            prices06.append(float(contents[i][11:])) 
    for i in range(len(prices06)): 
        total += prices06[i]
    avg = total / len(prices06) 
    print('May = $' + format(avg, ',.3f'))
    
    # June 
    total = 0
    prices06= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2006' and contents[i][0:2] == '06': 
            prices06.append(float(contents[i][11:])) 
    for i in range(len(prices06)): 
        total += prices06[i]
    avg = total / len(prices06) 
    print('June = $' + format(avg, ',.3f'))     
    
    # July 
    total = 0
    prices06= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2006' and contents[i][0:2] == '07': 
            prices06.append(float(contents[i][11:])) 
    for i in range(len(prices06)): 
        total += prices06[i]
    avg = total / len(prices06) 
    print('July = $' + format(avg, ',.3f'))     

    # August
    total = 0
    prices06= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2006' and contents[i][0:2] == '08': 
            prices06.append(float(contents[i][11:])) 
    for i in range(len(prices06)): 
        total += prices06[i]
    avg = total / len(prices06)   
    print('August = $' + format(avg, ',.3f'))     
    
    # September
    total = 0
    prices06= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2006' and contents[i][0:2] == '09': 
            prices06.append(float(contents[i][11:])) 
    for i in range(len(prices06)): 
        total += prices06[i]
    avg = total / len(prices06) 
    print('September = $' + format(avg, ',.3f')) 
    
    # October
    total = 0
    prices06= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2006' and contents[i][0:2] == '10': 
            prices06.append(float(contents[i][11:])) 
    for i in range(len(prices06)): 
        total += prices06[i]
    avg = total / len(prices06)  
    print('October = $' + format(avg, ',.3f'))
    
    # November
    total = 0
    prices06= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2006' and contents[i][0:2] == '11': 
            prices06.append(float(contents[i][11:])) 
    for i in range(len(prices06)): 
        total += prices06[i]
    avg = total / len(prices06) 
    print('November = $' + format(avg, ',.3f'))    
    
    # December 
    total = 0
    prices06= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2006' and contents[i][0:2] == '12': 
            prices06.append(float(contents[i][11:])) 
    for i in range(len(prices06)): 
        total += prices06[i]
    avg = total / len(prices06)   
    print('December = $' + format(avg, ',.3f'))
    
# ==========================  Average Per Month 2007 ===========================

def avg_per_month_2007(contents):
    print('\n---------------  The Average Price of Gas Per Month in 2007  ---------------')
    # January 
    total = 0
    prices07= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2007' and contents[i][0:2] == '01': 
            prices07.append(float(contents[i][11:])) 
    for i in range(len(prices07)): 
        total += prices07[i]
    avg = total / len(prices07) 
    print('January = $' + format(avg, ',.3f'))
    
    # February
    total = 0
    prices07= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2007' and contents[i][0:2] == '02': 
            prices07.append(float(contents[i][11:])) 
    for i in range(len(prices07)): 
        total += prices07[i]
    avg = total / len(prices07) 
    print('February = $' + format(avg, ',.3f'))
    
    # March 
    total = 0
    prices07= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2007' and contents[i][0:2] == '03': 
            prices07.append(float(contents[i][11:])) 
    for i in range(len(prices07)): 
        total += prices07[i]
    avg = total / len(prices07)  
    print('March = $' + format(avg, ',.3f'))
    
    # April
    total = 0
    prices07= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2007' and contents[i][0:2] == '04': 
            prices07.append(float(contents[i][11:])) 
    for i in range(len(prices07)): 
        total += prices07[i]
    avg = total / len(prices07) 
    print('April = $' + format(avg, ',.3f'))
    
    # May 
    total = 0
    prices07= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2007' and contents[i][0:2] == '05': 
            prices07.append(float(contents[i][11:])) 
    for i in range(len(prices07)): 
        total += prices07[i]
    avg = total / len(prices07) 
    print('May = $' + format(avg, ',.3f'))
    
    # June 
    total = 0
    prices07= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2007' and contents[i][0:2] == '06': 
            prices07.append(float(contents[i][11:])) 
    for i in range(len(prices07)): 
        total += prices07[i]
    avg = total / len(prices07) 
    print('June = $' + format(avg, ',.3f'))     
    
    # July 
    total = 0
    prices07= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2007' and contents[i][0:2] == '07': 
            prices07.append(float(contents[i][11:])) 
    for i in range(len(prices07)): 
        total += prices07[i]
    avg = total / len(prices07)  
    print('July = $' + format(avg, ',.3f'))     

    # August
    total = 0
    prices07= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2007' and contents[i][0:2] == '08': 
            prices07.append(float(contents[i][11:])) 
    for i in range(len(prices07)): 
        total += prices07[i]
    avg = total / len(prices07)   
    print('August = $' + format(avg, ',.3f'))     
    
    # September
    total = 0
    prices07= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2007' and contents[i][0:2] == '09': 
            prices07.append(float(contents[i][11:])) 
    for i in range(len(prices07)): 
        total += prices07[i]
    avg = total / len(prices07)  
    print('September = $' + format(avg, ',.3f')) 
    
    # October
    total = 0
    prices07= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2007' and contents[i][0:2] == '10': 
            prices07.append(float(contents[i][11:])) 
    for i in range(len(prices07)): 
        total += prices07[i]
    avg = total / len(prices07)  
    print('October = $' + format(avg, ',.3f'))
    
    # November
    total = 0
    prices07= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2007' and contents[i][0:2] == '11': 
            prices07.append(float(contents[i][11:])) 
    for i in range(len(prices07)): 
        total += prices07[i]
    avg = total / len(prices07) 
    print('November = $' + format(avg, ',.3f'))    
    
    # December 
    total = 0
    prices07= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2007' and contents[i][0:2] == '12': 
            prices07.append(float(contents[i][11:])) 
    for i in range(len(prices07)): 
        total += prices07[i]
    avg = total / len(prices07)   
    print('December = $' + format(avg, ',.3f'))
    
# ==========================  Average Per Month 2008 ===========================

def avg_per_month_2008(contents):
    print('\n---------------  The Average Price of Gas Per Month in 2008  ---------------')
    # January 
    total = 0
    prices08= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2008' and contents[i][0:2] == '01': 
            prices08.append(float(contents[i][11:])) 
    for i in range(len(prices08)): 
        total += prices08[i]
    avg = total / len(prices08) 
    print('January = $' + format(avg, ',.3f'))
    
    # February
    total = 0
    prices08= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2008' and contents[i][0:2] == '02': 
            prices08.append(float(contents[i][11:])) 
    for i in range(len(prices08)): 
        total += prices08[i]
    avg = total / len(prices08) 
    print('February = $' + format(avg, ',.3f'))
    
    # March 
    total = 0
    prices08= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2008' and contents[i][0:2] == '03': 
            prices08.append(float(contents[i][11:])) 
    for i in range(len(prices08)): 
        total += prices08[i]
    avg = total / len(prices08)  
    print('March = $' + format(avg, ',.3f'))
    
    # April
    total = 0
    prices08= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2008' and contents[i][0:2] == '04': 
            prices08.append(float(contents[i][11:])) 
    for i in range(len(prices08)): 
        total += prices08[i]
    avg = total / len(prices08) 
    print('April = $' + format(avg, ',.3f'))
    
    # May 
    total = 0
    prices08= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2008' and contents[i][0:2] == '05': 
            prices08.append(float(contents[i][11:])) 
    for i in range(len(prices08)): 
        total += prices08[i]
    avg = total / len(prices08) 
    print('May = $' + format(avg, ',.3f'))
    
    # June 
    total = 0
    prices08= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2008' and contents[i][0:2] == '06': 
            prices08.append(float(contents[i][11:])) 
    for i in range(len(prices08)): 
        total += prices08[i]
    avg = total / len(prices08) 
    print('June = $' + format(avg, ',.3f'))     
    
    # July 
    total = 0
    prices08= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2008' and contents[i][0:2] == '07': 
            prices08.append(float(contents[i][11:])) 
    for i in range(len(prices08)): 
        total += prices08[i]
    avg = total / len(prices08) 
    print('July = $' + format(avg, ',.3f'))     

    # August
    total = 0
    prices08= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2008' and contents[i][0:2] == '08': 
            prices08.append(float(contents[i][11:])) 
    for i in range(len(prices08)): 
        total += prices08[i]
    avg = total / len(prices08)   
    print('August = $' + format(avg, ',.3f'))     
    
    # September
    total = 0
    prices08= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2008' and contents[i][0:2] == '09': 
            prices08.append(float(contents[i][11:])) 
    for i in range(len(prices08)): 
        total += prices08[i]
    avg = total / len(prices08)   
    print('September = $' + format(avg, ',.3f')) 
    
    # October
    total = 0
    prices08= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2008' and contents[i][0:2] == '10': 
            prices08.append(float(contents[i][11:])) 
    for i in range(len(prices08)): 
        total += prices08[i]
    avg = total / len(prices08)   
    print('October = $' + format(avg, ',.3f'))
    
    # November
    total = 0
    prices08= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2008' and contents[i][0:2] == '11': 
            prices08.append(float(contents[i][11:])) 
    for i in range(len(prices08)): 
        total += prices08[i]
    avg = total / len(prices08) 
    print('November = $' + format(avg, ',.3f'))    
    
    # December 
    total = 0
    prices08= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2008' and contents[i][0:2] == '12': 
            prices08.append(float(contents[i][11:])) 
    for i in range(len(prices08)): 
        total += prices08[i]
    avg = total / len(prices08)   
    print('December = $' + format(avg, ',.3f'))

# ==========================  Average Per Month 2009 ===========================

def avg_per_month_2009(contents):
    print('\n---------------  The Average Price of Gas Per Month in 2009  ---------------')
    # January 
    total = 0
    prices09= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2009' and contents[i][0:2] == '01': 
            prices09.append(float(contents[i][11:])) 
    for i in range(len(prices09)): 
        total += prices09[i]
    avg = total / len(prices09) 
    print('January = $' + format(avg, ',.3f'))
    
    # February
    total = 0
    prices09= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2009' and contents[i][0:2] == '02': 
            prices09.append(float(contents[i][11:])) 
    for i in range(len(prices09)): 
        total += prices09[i]
    avg = total / len(prices09) 
    print('February = $' + format(avg, ',.3f'))
    
    # March 
    total = 0
    prices09= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2009' and contents[i][0:2] == '03': 
            prices09.append(float(contents[i][11:])) 
    for i in range(len(prices09)): 
        total += prices09[i]
    avg = total / len(prices09)  
    print('March = $' + format(avg, ',.3f'))
    
    # April
    total = 0
    prices09= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2009' and contents[i][0:2] == '04': 
            prices09.append(float(contents[i][11:])) 
    for i in range(len(prices09)): 
        total += prices09[i]
    avg = total / len(prices09) 
    print('April = $' + format(avg, ',.3f'))
    
    # May 
    total = 0
    prices09= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2009' and contents[i][0:2] == '05': 
            prices09.append(float(contents[i][11:])) 
    for i in range(len(prices09)): 
        total += prices09[i]
    avg = total / len(prices09) 
    print('May = $' + format(avg, ',.3f'))
    
    # June 
    total = 0
    prices09= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2009' and contents[i][0:2] == '06': 
            prices09.append(float(contents[i][11:])) 
    for i in range(len(prices09)): 
        total += prices09[i]
    avg = total / len(prices09) 
    print('June = $' + format(avg, ',.3f'))     
    
    # July 
    total = 0
    prices09= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2009' and contents[i][0:2] == '07': 
            prices09.append(float(contents[i][11:])) 
    for i in range(len(prices09)): 
        total += prices09[i]
    avg = total / len(prices09) 
    print('July = $' + format(avg, ',.3f'))     

    # August
    total = 0
    prices09= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2009' and contents[i][0:2] == '08': 
            prices09.append(float(contents[i][11:])) 
    for i in range(len(prices09)): 
        total += prices09[i]
    avg = total / len(prices09)    
    print('August = $' + format(avg, ',.3f'))     
    
    # September
    total = 0
    prices09= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2009' and contents[i][0:2] == '09': 
            prices09.append(float(contents[i][11:])) 
    for i in range(len(prices09)): 
        total += prices09[i]
    avg = total / len(prices09)    
    print('September = $' + format(avg, ',.3f')) 
    
    # October
    total = 0
    prices09= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2009' and contents[i][0:2] == '10': 
            prices09.append(float(contents[i][11:])) 
    for i in range(len(prices09)): 
        total += prices09[i]
    avg = total / len(prices09)   
    print('October = $' + format(avg, ',.3f'))
    
    # November
    total = 0
    prices09= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2009' and contents[i][0:2] == '11': 
            prices09.append(float(contents[i][11:])) 
    for i in range(len(prices09)): 
        total += prices09[i]
    avg = total / len(prices09) 
    print('November = $' + format(avg, ',.3f'))    
    
    # December 
    total = 0
    prices09= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2009' and contents[i][0:2] == '12': 
            prices09.append(float(contents[i][11:])) 
    for i in range(len(prices09)): 
        total += prices09[i]
    avg = total / len(prices09)   
    print('December = $' + format(avg, ',.3f'))

# ==========================  Average Per Month 2010 ===========================  

def avg_per_month_2010(contents):
    print('\n---------------  The Average Price of Gas Per Month in 2010  ---------------')
    # January 
    total = 0
    prices10= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2010' and contents[i][0:2] == '01': 
            prices10.append(float(contents[i][11:])) 
    for i in range(len(prices10)): 
        total += prices10[i]
    avg = total / len(prices10) 
    print('January = $' + format(avg, ',.3f'))
    
    # February
    total = 0
    prices10= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2010' and contents[i][0:2] == '02': 
            prices10.append(float(contents[i][11:])) 
    for i in range(len(prices10)): 
        total += prices10[i]
    avg = total / len(prices10) 
    print('February = $' + format(avg, ',.3f'))
    
    # March 
    total = 0
    prices10= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2010' and contents[i][0:2] == '03': 
            prices10.append(float(contents[i][11:])) 
    for i in range(len(prices10)): 
        total += prices10[i]
    avg = total / len(prices10)  
    print('March = $' + format(avg, ',.3f'))
    
    # April
    total = 0
    prices10= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2010' and contents[i][0:2] == '04': 
            prices10.append(float(contents[i][11:])) 
    for i in range(len(prices10)): 
        total += prices10[i]
    avg = total / len(prices10)  
    print('April = $' + format(avg, ',.3f'))
    
    # May 
    total = 0
    prices10= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2010' and contents[i][0:2] == '05': 
            prices10.append(float(contents[i][11:])) 
    for i in range(len(prices10)): 
        total += prices10[i]
    avg = total / len(prices10) 
    print('May = $' + format(avg, ',.3f'))
    
    # June 
    total = 0
    prices10= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2010' and contents[i][0:2] == '06': 
            prices10.append(float(contents[i][11:])) 
    for i in range(len(prices10)): 
        total += prices10[i]
    avg = total / len(prices10) 
    print('June = $' + format(avg, ',.3f'))     
    
    # July 
    total = 0
    prices10= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2010' and contents[i][0:2] == '07': 
            prices10.append(float(contents[i][11:])) 
    for i in range(len(prices10)): 
        total += prices10[i]
    avg = total / len(prices10) 
    print('July = $' + format(avg, ',.3f'))     

    # August
    total = 0
    prices10= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2010' and contents[i][0:2] == '08': 
            prices10.append(float(contents[i][11:])) 
    for i in range(len(prices10)): 
        total += prices10[i]
    avg = total / len(prices10)    
    print('August = $' + format(avg, ',.3f'))     
    
    # September
    total = 0
    prices10= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2010' and contents[i][0:2] == '09': 
            prices10.append(float(contents[i][11:])) 
    for i in range(len(prices10)): 
        total += prices10[i]
    avg = total / len(prices10)     
    print('September = $' + format(avg, ',.3f')) 
    
    # October
    total = 0
    prices10= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2010' and contents[i][0:2] == '10': 
            prices10.append(float(contents[i][11:])) 
    for i in range(len(prices10)): 
        total += prices10[i]
    avg = total / len(prices10)  
    print('October = $' + format(avg, ',.3f'))
    
    # November
    total = 0
    prices10= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2010' and contents[i][0:2] == '11': 
            prices10.append(float(contents[i][11:])) 
    for i in range(len(prices10)): 
        total += prices10[i]
    avg = total / len(prices10) 
    print('November = $' + format(avg, ',.3f'))    
    
    # December 
    total = 0
    prices10= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2010' and contents[i][0:2] == '12': 
            prices10.append(float(contents[i][11:])) 
    for i in range(len(prices10)): 
        total += prices10[i]
    avg = total / len(prices10)   
    print('December = $' + format(avg, ',.3f'))

# ==========================  Average Per Month 2011 =========================== 

def avg_per_month_2011(contents):
    print('\n---------------  The Average Price of Gas Per Month in 2011  ---------------')
    # January 
    total = 0
    prices11= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2011' and contents[i][0:2] == '01': 
            prices11.append(float(contents[i][11:])) 
    for i in range(len(prices11)): 
        total += prices11[i]
    avg = total / len(prices11) 
    print('January = $' + format(avg, ',.3f'))
    
    # February
    total = 0
    prices11= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2011' and contents[i][0:2] == '02': 
            prices11.append(float(contents[i][11:])) 
    for i in range(len(prices11)): 
        total += prices11[i]
    avg = total / len(prices11) 
    print('February = $' + format(avg, ',.3f'))
    
    # March 
    total = 0
    prices11= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2011' and contents[i][0:2] == '03': 
            prices11.append(float(contents[i][11:])) 
    for i in range(len(prices11)): 
        total += prices11[i]
    avg = total / len(prices11) 
    print('March = $' + format(avg, ',.3f'))
    
    # April
    total = 0
    prices11= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2011' and contents[i][0:2] == '04': 
            prices11.append(float(contents[i][11:])) 
    for i in range(len(prices11)): 
        total += prices11[i]
    avg = total / len(prices11)  
    print('April = $' + format(avg, ',.3f'))
    
    # May 
    total = 0
    prices11= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2011' and contents[i][0:2] == '05': 
            prices11.append(float(contents[i][11:])) 
    for i in range(len(prices11)): 
        total += prices11[i]
    avg = total / len(prices11) 
    print('May = $' + format(avg, ',.3f'))
    
    # June 
    total = 0
    prices11= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2011' and contents[i][0:2] == '06': 
            prices11.append(float(contents[i][11:])) 
    for i in range(len(prices11)): 
        total += prices11[i]
    avg = total / len(prices11) 
    print('June = $' + format(avg, ',.3f'))     
    
    # July 
    total = 0
    prices11= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2011' and contents[i][0:2] == '07': 
            prices11.append(float(contents[i][11:])) 
    for i in range(len(prices11)): 
        total += prices11[i]
    avg = total / len(prices11) 
    print('July = $' + format(avg, ',.3f'))     

    # August
    total = 0
    prices11= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2011' and contents[i][0:2] == '08': 
            prices11.append(float(contents[i][11:])) 
    for i in range(len(prices11)): 
        total += prices11[i]
    avg = total / len(prices11)   
    print('August = $' + format(avg, ',.3f'))     
    
    # September
    total = 0
    prices11= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2011' and contents[i][0:2] == '09': 
            prices11.append(float(contents[i][11:])) 
    for i in range(len(prices11)): 
        total += prices11[i]
    avg = total / len(prices11)     
    print('September = $' + format(avg, ',.3f')) 
    
    # October
    total = 0
    prices11= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2011' and contents[i][0:2] == '10': 
            prices11.append(float(contents[i][11:])) 
    for i in range(len(prices11)): 
        total += prices11[i]
    avg = total / len(prices11)  
    print('October = $' + format(avg, ',.3f'))
    
    # November
    total = 0
    prices11= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2011' and contents[i][0:2] == '11': 
            prices11.append(float(contents[i][11:])) 
    for i in range(len(prices11)): 
        total += prices11[i]
    avg = total / len(prices11) 
    print('November = $' + format(avg, ',.3f'))    
    
    # December 
    total = 0
    prices11= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2011' and contents[i][0:2] == '12': 
            prices11.append(float(contents[i][11:])) 
    for i in range(len(prices11)): 
        total += prices11[i]
    avg = total / len(prices11)    
    print('December = $' + format(avg, ',.3f'))

# ==========================  Average Per Month 2012 ===========================

def avg_per_month_2012(contents):
    print('\n---------------  The Average Price of Gas Per Month in 2012  ---------------')
    # January 
    total = 0
    prices12= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2012' and contents[i][0:2] == '01': 
            prices12.append(float(contents[i][11:])) 
    for i in range(len(prices12)): 
        total += prices12[i]
    avg = total / len(prices12) 
    print('January = $' + format(avg, ',.3f'))
    
    # February
    total = 0
    prices12= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2012' and contents[i][0:2] == '02': 
            prices12.append(float(contents[i][11:])) 
    for i in range(len(prices12)): 
        total += prices12[i]
    avg = total / len(prices12) 
    print('February = $' + format(avg, ',.3f'))
    
    # March 
    total = 0
    prices12= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2012' and contents[i][0:2] == '03': 
            prices12.append(float(contents[i][11:])) 
    for i in range(len(prices12)): 
        total += prices12[i]
    avg = total / len(prices12) 
    print('March = $' + format(avg, ',.3f'))
    
    # April
    total = 0
    prices12= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2012' and contents[i][0:2] == '04': 
            prices12.append(float(contents[i][11:])) 
    for i in range(len(prices12)): 
        total += prices12[i]
    avg = total / len(prices12)  
    print('April = $' + format(avg, ',.3f'))
    
    # May 
    total = 0
    prices12= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2012' and contents[i][0:2] == '05': 
            prices12.append(float(contents[i][11:])) 
    for i in range(len(prices12)): 
        total += prices12[i]
    avg = total / len(prices12) 
    print('May = $' + format(avg, ',.3f'))
    
    # June 
    total = 0
    prices12= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2012' and contents[i][0:2] == '06': 
            prices12.append(float(contents[i][11:])) 
    for i in range(len(prices12)): 
        total += prices12[i]
    avg = total / len(prices12)  
    print('June = $' + format(avg, ',.3f'))     
    
    # July 
    total = 0
    prices12= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2012' and contents[i][0:2] == '07': 
            prices12.append(float(contents[i][11:])) 
    for i in range(len(prices12)): 
        total += prices12[i]
    avg = total / len(prices12)  
    print('July = $' + format(avg, ',.3f'))     

    # August
    total = 0
    prices12= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2012' and contents[i][0:2] == '08': 
            prices12.append(float(contents[i][11:])) 
    for i in range(len(prices12)): 
        total += prices12[i]
    avg = total / len(prices12)   
    print('August = $' + format(avg, ',.3f'))     
    
    # September
    total = 0
    prices12= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2012' and contents[i][0:2] == '09': 
            prices12.append(float(contents[i][11:])) 
    for i in range(len(prices12)): 
        total += prices12[i]
    avg = total / len(prices12)     
    print('September = $' + format(avg, ',.3f')) 
    
    # October
    total = 0
    prices12= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2012' and contents[i][0:2] == '10': 
            prices12.append(float(contents[i][11:])) 
    for i in range(len(prices12)): 
        total += prices12[i]
    avg = total / len(prices12)  
    print('October = $' + format(avg, ',.3f'))
    
    # November
    total = 0
    prices12= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2012' and contents[i][0:2] == '11': 
            prices12.append(float(contents[i][11:])) 
    for i in range(len(prices12)): 
        total += prices12[i]
    avg = total / len(prices12) 
    print('November = $' + format(avg, ',.3f'))    
    
    # December 
    total = 0
    prices12= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2012' and contents[i][0:2] == '12': 
            prices12.append(float(contents[i][11:])) 
    for i in range(len(prices12)): 
        total += prices12[i]
    avg = total / len(prices12)    
    print('December = $' + format(avg, ',.3f'))
    
# ==========================  Average Per Month 2013 =========================== 

def avg_per_month_2013(contents):
    print('\n---------------  The Average Price of Gas Per Month in 2013  ---------------')
    print('\nNOTE: 2013\'s data ends the week of August 26th.')
    # January 
    total = 0
    prices13= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2013' and contents[i][0:2] == '01': 
            prices13.append(float(contents[i][11:])) 
    for i in range(len(prices13)): 
        total += prices13[i]
    avg = total / len(prices13) 
    print('\nJanuary = $' + format(avg, ',.3f'))
    
    # February
    total = 0
    prices13= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2013' and contents[i][0:2] == '02': 
            prices13.append(float(contents[i][11:])) 
    for i in range(len(prices13)): 
        total += prices13[i]
    avg = total / len(prices13) 
    print('February = $' + format(avg, ',.3f'))
    
    # March 
    total = 0
    prices13= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2013' and contents[i][0:2] == '03': 
            prices13.append(float(contents[i][11:])) 
    for i in range(len(prices13)): 
        total += prices13[i]
    avg = total / len(prices13) 
    print('March = $' + format(avg, ',.3f'))
    
    # April
    total = 0
    prices13= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2013' and contents[i][0:2] == '04': 
            prices13.append(float(contents[i][11:])) 
    for i in range(len(prices13)): 
        total += prices13[i]
    avg = total / len(prices13)   
    print('April = $' + format(avg, ',.3f'))
    
    # May 
    total = 0
    prices13= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2013' and contents[i][0:2] == '05': 
            prices13.append(float(contents[i][11:])) 
    for i in range(len(prices13)): 
        total += prices13[i]
    avg = total / len(prices13) 
    print('May = $' + format(avg, ',.3f'))
    
    # June 
    total = 0
    prices13= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2013' and contents[i][0:2] == '06': 
            prices13.append(float(contents[i][11:])) 
    for i in range(len(prices13)): 
        total += prices13[i]
    avg = total / len(prices13)  
    print('June = $' + format(avg, ',.3f'))     
    
    # July 
    total = 0
    prices13= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2013' and contents[i][0:2] == '07': 
            prices13.append(float(contents[i][11:])) 
    for i in range(len(prices13)): 
        total += prices13[i]
    avg = total / len(prices13)  
    print('July = $' + format(avg, ',.3f'))     

    # August
    total = 0
    prices13= []
    for i in range(len(contents)):
        if contents[i][6:10] == '2013' and contents[i][0:2] == '08': 
            prices13.append(float(contents[i][11:])) 
    for i in range(len(prices13)): 
        total += prices13[i]
    avg = total / len(prices13)   
    print('August = $' + format(avg, ',.3f'))

# =================== Listing Highest to Lowest Prices Per Year ================

def high_and_low_per_year(contents):
    print('\n---------------  The Highest and Lowest Prices of Gas Per Year  ---------------')
    # 1993
    prices93 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1993':
            prices93.append(float(contents[i][11:])) 
    low = min(prices93)
    high = max(prices93)
    print('\n1993\tLowest Price = $' + format(low, ',.3f'))
    print('\tHighest Price = $' + format(high, ',.3f'))
    print('-------------------------------')
    
    # 1994
    prices94 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1994':
            prices94.append(float(contents[i][11:])) 
    low = min(prices94)
    high = max(prices94)
    print('\n1994\tLowest Price = $' + format(low, ',.3f'))
    print('\tHighest Price = $' + format(high, ',.3f'))
    print('-------------------------------')
    
    # 1995
    prices95 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1995':
            prices95.append(float(contents[i][11:])) 
    low = min(prices95)
    high = max(prices95)
    print('\n1995\tLowest Price = $' + format(low, ',.3f'))
    print('\tHighest Price = $' + format(high, ',.3f'))
    print('-------------------------------')
    
    # 1996
    prices96 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1996':
            prices96.append(float(contents[i][11:])) 
    low = min(prices96)
    high = max(prices96)
    print('\n1996\tLowest Price = $' + format(low, ',.3f'))
    print('\tHighest Price = $' + format(high, ',.3f'))
    print('-------------------------------')
    
    # 1997
    prices97 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1997':
            prices97.append(float(contents[i][11:])) 
    low = min(prices97)
    high = max(prices97)
    print('\n1997\tLowest Price = $' + format(low, ',.3f'))
    print('\tHighest Price = $' + format(high, ',.3f'))
    print('-------------------------------') 
    
    # 1998
    prices98 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1998':
            prices98.append(float(contents[i][11:])) 
    low = min(prices98)
    high = max(prices98)
    print('\n1998\tLowest Price = $' + format(low, ',.3f'))
    print('\tHighest Price = $' + format(high, ',.3f'))
    print('-------------------------------')
    
    # 1999
    prices99 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '1999':
            prices99.append(float(contents[i][11:])) 
    low = min(prices99)
    high = max(prices99)
    print('\n1999\tLowest Price = $' + format(low, ',.3f'))
    print('\tHighest Price = $' + format(high, ',.3f'))
    print('-------------------------------') 
    
    # 2000
    prices00 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2000':
            prices00.append(float(contents[i][11:])) 
    low = min(prices00)
    high = max(prices00)
    print('\n2000\tLowest Price = $' + format(low, ',.3f'))
    print('\tHighest Price = $' + format(high, ',.3f'))
    print('-------------------------------') 
    
    # 2001
    prices01 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2001':
            prices01.append(float(contents[i][11:])) 
    low = min(prices01)
    high = max(prices01)
    print('\n2001\tLowest Price = $' + format(low, ',.3f'))
    print('\tHighest Price = $' + format(high, ',.3f'))
    print('-------------------------------')
    
    # 2002
    prices02 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2002':
            prices02.append(float(contents[i][11:])) 
    low = min(prices02)
    high = max(prices02)
    print('\n2002\tLowest Price = $' + format(low, ',.3f'))
    print('\tHighest Price = $' + format(high, ',.3f'))
    print('-------------------------------')
    
    # 2003
    prices03 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2003':
            prices03.append(float(contents[i][11:])) 
    low = min(prices03)
    high = max(prices03)
    print('\n2003\tLowest Price = $' + format(low, ',.3f'))
    print('\tHighest Price = $' + format(high, ',.3f'))
    print('-------------------------------')
    
    # 2004
    prices04 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2004':
            prices04.append(float(contents[i][11:])) 
    low = min(prices04)
    high = max(prices04)
    print('\n2004\tLowest Price = $' + format(low, ',.3f'))
    print('\tHighest Price = $' + format(high, ',.3f'))
    print('-------------------------------') 
    
    # 2005
    prices05 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2005':
            prices05.append(float(contents[i][11:])) 
    low = min(prices05)
    high = max(prices05)
    print('\n2005\tLowest Price = $' + format(low, ',.3f'))
    print('\tHighest Price = $' + format(high, ',.3f')) 
    print('-------------------------------')
    
    # 2006
    prices06 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2006':
            prices06.append(float(contents[i][11:])) 
    low = min(prices06)
    high = max(prices06)
    print('\n2006\tLowest Price = $' + format(low, ',.3f'))
    print('\tHighest Price = $' + format(high, ',.3f')) 
    print('-------------------------------')
    
    # 2007
    prices07 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2007':
            prices07.append(float(contents[i][11:])) 
    low = min(prices07)
    high = max(prices07)
    print('\n2007\tLowest Price = $' + format(low, ',.3f'))
    print('\tHighest Price = $' + format(high, ',.3f')) 
    print('-------------------------------')
    
    # 2008
    prices08 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2008':
            prices08.append(float(contents[i][11:])) 
    low = min(prices08)
    high = max(prices08)
    print('\n2008\tLowest Price = $' + format(low, ',.3f'))
    print('\tHighest Price = $' + format(high, ',.3f')) 
    print('-------------------------------')
    
    # 2009
    prices09 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2009':
            prices09.append(float(contents[i][11:])) 
    low = min(prices09)
    high = max(prices09)
    print('\n2009\tLowest Price = $' + format(low, ',.3f'))
    print('\tHighest Price = $' + format(high, ',.3f')) 
    print('-------------------------------')
    
    # 2010
    prices10 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2010':
            prices10.append(float(contents[i][11:])) 
    low = min(prices10)
    high = max(prices10)
    print('\n2010\tLowest Price = $' + format(low, ',.3f'))
    print('\tHighest Price = $' + format(high, ',.3f')) 
    print('-------------------------------') 
    
    # 2011
    prices11 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2011':
            prices11.append(float(contents[i][11:])) 
    low = min(prices11)
    high = max(prices11)
    print('\n2011\tLowest Price = $' + format(low, ',.3f'))
    print('\tHighest Price = $' + format(high, ',.3f')) 
    print('-------------------------------')
    
    # 2012
    prices12 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2012':
            prices12.append(float(contents[i][11:])) 
    low = min(prices12)
    high = max(prices12)
    print('\n2012\tLowest Price = $' + format(low, ',.3f'))
    print('\tHighest Price = $' + format(high, ',.3f')) 
    print('-------------------------------') 
    
    # 2013
    prices13 = []
    for i in range(len(contents)):
        if contents[i][6:10] == '2013':
            prices13.append(float(contents[i][11:])) 
    low = min(prices13)
    high = max(prices13)
    print('\n2013\tLowest Price = $' + format(low, ',.3f'))
    print('\tHighest Price = $' + format(high, ',.3f'))     
    print('-------------------------------') 


# ============  Making text file for sorted list lowest to highest  ============

def list_low_to_high(contents):
    print('\n------  List of Dates and Prices Sorted from Lowest to Highest  ------')
    print('\nA text file named lowest_to_highest_prices.txt was created in the same')
    print('folder as this program. The text file list the dates and prices of gas')
    print('sorted from lowest to highest by price.')
    print('\nThe format in the text file is as follows: ')
    print('Price : MM - DD - YYYY')
    print('\nYou can view the data by opening the file that was created.')    
    
    list_ = []
    new_list = []
    s = ':'
    
    low_2_high_file = open('lowest_to_highest_prices.txt', 'w')
    
    for i in range(len(contents)):
        new = contents[i].split(':')
        list_.append(new) 
    for i in range(len(list_)):
        new_list.append(list_[i][1] + ':' + list_[i][0])
    
    # Sorting the list
    new_list = sorted(new_list)    
    
    # Writing the data to the file
    for i in range(len(new_list)):
        low_2_high_file.write(str(new_list[i]) + '\n')
    
 
    # Close the file
    low_2_high_file.close()
    print('\nData written to lowest_to_highest_prices.txt ')
   
# ============  Making text file for sorted list highest to lowest  ============

def list_high_to_low(contents):
    print('\n------  List of Dates and Prices Sorted from Highest to Lowest  ------')
    print('\nA text file named highest_to_lowest_prices.txt was created in the same')
    print('folder as this program. The text file list the dates and prices of gas')
    print('sorted from the highest to lowest prices of gas.')
    print('\nThe format in the text file is as follows: ')
    print('Price : MM - DD - YYYY')
    print('\nYou can view the data by opening the file that was created.')

    list_ = []
    new_list = []
    
    high_2_low_file = open('highest_to_lowest_prices.txt', 'w')
    
    # Separating and rearranging the data to sort it
    for i in range(len(contents)):
        new = contents[i].split(':')
        list_.append(new) 
    for i in range(len(list_)):
        new_list.append(list_[i][1] + ':' + list_[i][0])
    
    # Sorting the list
    new_list = sorted(new_list, reverse=True)
       
    # Writing the data to the file
    for i in range(len(new_list)):
        high_2_low_file.write(str(new_list[i]) + '\n')
    
 
    # Close the file
    high_2_low_file.close()
    
    print('\nData has been written to highest_to_lowest_prices.txt ')    
    
# ===================  Call main to run program  ===============================
main()