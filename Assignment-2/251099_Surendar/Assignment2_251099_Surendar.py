import numpy as np
import matplotlib.pyplot as plt

def call_option(strike_price,premium):
    spot_prices=np.arange(strike_price-50,strike_price+31) #RANGE OF SPOT PRICES

    if premium>0:      ##BUYING THE CALL
        payoff=np.maximum(spot_prices-strike_price,0)-premium
        title="Buying a Call Option(Long Call)"
        call_status='Call long'

    else:             ##SELLING THE CALL
        payoff= -(premium)-np.maximum(spot_prices-strike_price,0)
        title="Selling a Call Option(Short Call)"
        call_status="Call short"

    plt.plot(spot_prices,payoff,color='green',lw=2,label=call_status)

    plt.axhline(y=0,color='grey',lw=2,ls='--',label='Break-Even')##BREAK-EVEN LINE
    plt.axvline(x=strike_price+abs(premium),lw=2,ls='--',color='grey')

    plt.axvline(x=strike_price,lw=2,ls='--',color='red',label='strike_price')## STRIKE PRICE
    plt.title(title,fontsize=16,color='darkblue',fontweight="bold")
    plt.xlabel("SPOT PRICES",fontsize=12,color='red',fontweight='bold')
    plt.ylabel("P/L",fontsize=12,color='black',fontweight='bold')
    plt.grid(alpha=0.2)
    plt.legend()
    plt.show()

def put_option(strike_price,premium):
    spot_prices=np.arange(strike_price-50,strike_price+31) #RANGE OF SPOT PRICES

    if premium>0:      ##BUYING THE PUT
        payoff=np.maximum(strike_price-spot_prices,0)-premium
        title="Buying a Put Option(Long Put)"
        call_status='Long Put'

    else:             ##SELLING THE CALL
        payoff= -(premium)-np.maximum(strike_price-spot_prices,0)
        title="Selling a Put Option(Short Put)"
        call_status="Short Put"

    plt.plot(spot_prices,payoff,color='green',lw=2,label=call_status)

    plt.axhline(y=0,color='grey',lw=2,ls='--',label='Break-Even')##BREAK-EVEN LINE
    plt.axvline(x=strike_price+abs(premium),lw=2,ls='--',color='grey')

    plt.axvline(x=strike_price,lw=2,ls='--',color='red',label='strike_price')## STRIKE PRICE
    plt.title(title,fontsize=16,color='darkblue',fontweight="bold")
    plt.xlabel("SPOT PRICES",fontsize=12,color='red',fontweight='bold')
    plt.ylabel("P/L",fontsize=12,color='black',fontweight='bold')
    plt.grid(alpha=0.2)
    plt.legend()
    plt.show()

###GETTING INPUT FROM USER
opt=input("Enter Option type(Call or Put): ") #CHOICE CALL/PUT
sp=int(input("Enter Strike Price: ")) ## STRIKE PRICE
pr=int(input("Enter Premium amount: ")) ##PREMIUM

if(opt.lower()=='call'):
    call_option(sp,pr)
elif(opt.lower()=='put'):
    put_option(sp,pr)
else:
    print("Enter Valid Choice")