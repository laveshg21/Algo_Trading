import pandas as pd
import yfinance as yf
    
def hilo(s):
    W1=yf.download(s,'2022-09-28','2022-10-06')
    W2=yf.download(s,'2022-09-21','2022-10-06')
    W4=yf.download(s,'2022-09-07','2022-10-06')
    W8=yf.download(s,'2022-08-10','2022-10-06')
    W16=yf.download(s,'2022-06-15','2022-10-06')
    M6=yf.download(s,'2021-04-06','2022-10-06')
    Y1=yf.download(s,'2021-10-06','2022-10-06')
    Y2=yf.download(s,'2020-10-06','2022-10-06')
  
#############################################################
#DEFINING WEIGHT FUNCTION:

    def weight(k,W1,W2,W4,W8,W16,M6,Y1,Y2):
        hilo_W1 = pd.DataFrame(columns=['Lord'])
        hilo_W1['Lord'] = (((W1['High']-W1['Low'])*100 )/W1['High'])
        true_W1 = hilo_W1[hilo_W1.Lord > k]
        freq_W1 = (true_W1.size*100)/(W1.size)

        hilo_W2 = pd.DataFrame(columns=['Lord'])
        hilo_W2['Lord'] = (((W2['High']-W2['Low'])*100 )/W2['High'])
        true_W2 = hilo_W2[hilo_W2.Lord > k]
        freq_W2 = (true_W2.size*100)/(W2.size)
    
        hilo_W4 = pd.DataFrame(columns=['Lord'])
        hilo_W4['Lord'] = (((W4['High']-W4['Low'])*100 )/W4['High'])
        true_W4 = hilo_W4[hilo_W4.Lord > k]
        freq_W4 = (true_W4.size*100)/(W4.size)
    
        hilo_W8 = pd.DataFrame(columns=['Lord'])
        hilo_W8['Lord'] = (((W8['High']-W8['Low'])*100 )/W8['High'])
        true_W8=hilo_W8[hilo_W8.Lord > k]
        freq_W8 = (true_W8.size*100)/(W8.size)

        hilo_W16 = pd.DataFrame(columns=['Lord'])
        hilo_W16['Lord'] = (((W16['High']-W16['Low'])*100 )/W16['High'])
        true_W16=hilo_W16[hilo_W16.Lord > k]
        freq_W16 = (true_W16.size*100)/(W16.size)

        hilo_M6 = pd.DataFrame(columns=['Lord'])
        hilo_M6['Lord'] = (((M6['High']-M6['Low'])*100 )/M6['High'])
        true_M6=hilo_M6[hilo_M6.Lord > k]
        freq_M6 = (true_M6.size*100)/(M6.size)

        hilo_Y1 = pd.DataFrame(columns=['Lord'])
        hilo_Y1['Lord'] = (((Y1['High']-Y1['Low'])*100 )/Y1['High'])
        true_Y1=hilo_Y1[hilo_Y1.Lord > k]
        freq_Y1 = (true_Y1.size*100)/(Y1.size)

        hilo_Y2 = pd.DataFrame(columns=['Lord'])
        hilo_Y2['Lord'] = (((Y2['High']-Y2['Low'])*100 )/Y2['High'])
        true_Y2=hilo_Y2[hilo_Y2.Lord > k]
        freq_Y2 = (true_Y2.size*100)/(Y2.size)

        return ((256*(freq_W1))+ (128*(freq_W2))+ (64*(freq_W4)) + (32*(freq_W8))+ (16*(freq_W16)) + (8*(freq_M6))+ (4*(freq_Y1))+ (2*(freq_Y2)))
    
    # k = 0.35
    P035 = weight(0.35,W1,W2,W4,W8,W16,M6,Y1,Y2)
    
    # k = 0.5
    P05 = weight(0.50,W1,W2,W4,W8,W16,M6,Y1,Y2)
    
    # k = 1
    P1  = weight(1,W1,W2,W4,W8,W16,M6,Y1,Y2)
    
    # k = 2
    P2  = weight(2,W1,W2,W4,W8,W16,M6,Y1,Y2)
    
    # k = 3.5
    P35  = weight(3.5,W1,W2,W4,W8,W16,M6,Y1,Y2)

########################## RISK ############################## 

    def rweight(k,W1,W2,W4,W8,W16,M6,Y1,Y2):
        hilo_W1 = pd.DataFrame(columns=['Lord'])
        hilo_W1['Lord'] = (((W1['Open']-W1['Low'])*100 )/W1['Open'])
        true_W1=hilo_W1[hilo_W1.Lord < k]
        freq_W1 = (true_W1.size*100)/(W1.size)
        
        hilo_W2 = pd.DataFrame(columns=['Lord'])
        hilo_W2['Lord'] = (((W2['Open']-W2['Low'])*100 )/W2['Open'])
        true_W2=hilo_W2[hilo_W2.Lord < k]
        freq_W2 = (true_W2.size*100)/(W2.size)

        hilo_W4 = pd.DataFrame(columns=['Lord'])
        hilo_W4['Lord'] = (((W4['Open']-W4['Low'])*100 )/W4['Open'])
        true_W4=hilo_W4[hilo_W4.Lord < k]
        freq_W4 = (true_W4.size*100)/(W4.size)

        hilo_W8 = pd.DataFrame(columns=['Lord'])
        hilo_W8['Lord'] = (((W8['Open']-W8['Low'])*100 )/W8['Open'])
        true_W8=hilo_W8[hilo_W8.Lord < k]
        freq_W8 = (true_W8.size*100)/(W8.size)

        hilo_W16 = pd.DataFrame(columns=['Lord'])
        hilo_W16['Lord'] = (((W16['Open']-W16['Low'])*100 )/W16['Open'])
        true_W16=hilo_W16[hilo_W16.Lord < k]
        freq_W16 = (true_W16.size*100)/(W16.size)

        hilo_M6 = pd.DataFrame(columns=['Lord'])
        hilo_M6['Lord'] = (((M6['Open']-M6['Low'])*100 )/M6['Open'])
        true_M6=hilo_M6[hilo_M6.Lord < k]
        freq_M6 = (true_M6.size*100)/(M6.size)

        hilo_Y1 = pd.DataFrame(columns=['Lord'])
        hilo_Y1['Lord'] = (((Y1['Open']-Y1['Low'])*100 )/Y1['Open'])
        true_Y1=hilo_Y1[hilo_Y1.Lord < k]
        freq_Y1 = (true_Y1.size*100)/(Y1.size)

        hilo_Y2 = pd.DataFrame(columns=['Lord'])
        hilo_Y2['Lord'] = (((Y2['Open']-Y2['Low'])*100 )/Y2['Open'])
        true_Y2=hilo_Y2[hilo_Y2.Lord < k]
        freq_Y2 = (true_Y2.size*100)/(Y2.size)
  
        return ((256*(freq_W1))+ (128*(freq_W2))+ (64*(freq_W4)) + (32*(freq_W8))+ (16*(freq_W16)) + (8*(freq_M6))+ (4*(freq_Y1))+ (2*(freq_Y2)))
    
    # k = 1 
    R1 = rweight(1,W1,W2,W4,W8,W16,M6,Y1,Y2)
    
    # k = 0.5
    R05 = rweight(0.5,W1,W2,W4,W8,W16,M6,Y1,Y2)
    
    # k = 0.3
    R03 = rweight(0.3,W1,W2,W4,W8,W16,M6,Y1,Y2)
    
    # For most negative case k = 0 
    R0 = rweight(0,W1,W2,W4,W8,W16,M6,Y1,Y2)

    df2 = {'Stock': s, 'P035':P035, 'P05': P05, 'P1': P1, 'P2':P2, 'P35':P35, 'R05':R05, 'R1':R1, 'R03' :R03, 'R0' : R0}
    return df2