import matplotlib.pyplot as plt
import numpy as np

strike_price = int(input('Enter Strike Price : '))
premium = int(input('Enter Premium : '))
lower_bound = int(input('Enter the lower bound of stock price : '))
upper_bound = int(input('Enter the upper bound of stock price : '))


# Making a numpy array within bounds
stock_range = np.arange(lower_bound,upper_bound+1,1)

#Using the payoff formulas for each case
buy_call_payoff = np.maximum(0,stock_range - strike_price) - premium
buy_put_payoff = np.maximum(0,strike_price - stock_range) - premium
sell_call_payoff = -np.maximum(0,stock_range - strike_price) + premium
sell_put_payoff = -np.maximum(0,strike_price - stock_range) + premium

fig1, ax1 = plt.subplots()
fig1, ax2 = plt.subplots()



ax1.plot(stock_range,buy_call_payoff,label = 'Buy Call')
ax1.plot(stock_range,buy_put_payoff,label = 'Buy Put')

ax1.set_xlabel("Stock Price")
ax1.set_ylabel("Payoff")
ax1.set_title("Payoff vs Stock Price for Buyer")

ax1.legend()

ax2.plot(stock_range,sell_call_payoff,label = 'Sell Call')
ax2.plot(stock_range,sell_put_payoff,label = 'Sell Put')

ax2.set_xlabel("Stock Price")
ax2.set_ylabel("Payoff")
ax2.set_title("Payoff vs Stock Price for Seller")

ax2.legend()

plt.show()


'''
Delta - Delta represents the change in option premium with respect to the stock price.
        Moneyness of an option can be inferred through delta. For a call option when delta > 0.5
        it is in the money and when < 0.5 out of the money and = 0.5 is at the money.
        For a call option the range of delta is 0 to 1 and for a put option it is -1 to 0.

Gamma - Gamma represents the change in delta with respect to the stock price.
        Gamma is maximum at in the money and decreases along in the money and out of the money.
        Gamma is always positive.

Theta - Theta represents the time decay of an option. As the expiration date of an option nears 
        the premium of an option decreases making it a depreciating asset.
        For sellers theta is positive and for buyers theta is negative.

Vega - Vega represents the volatility in an option price. With increase in volatility the price
       of both put and call options increase. For sellers vega is negative and for buyers 
       vega is positive.


'''
