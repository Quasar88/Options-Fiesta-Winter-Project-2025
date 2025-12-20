import numpy as np
import matplotlib.pyplot as plt
#taking inputs
K=float(input("Enter strike price: "))
P=float(input("Enter premium (positive for buy, negative for sell): "))
lower, upper = map(float, input("Enter spot price range (start-end): ").split('-'))
option=input("Call or Put: ").lower()
#the function "profit" returns the profit and label(type of option)
def profit(option, K, S, P):
    if (option=="call"):
        if (P>0):
            label="Buy Call"
            return np.maximum(0, S-K)-abs(P), label
        elif (P<0):
            label="Sell Call"
            return abs(P) - np.maximum(0, S-K), label
    elif (option=="put"):
        if (P>0):
            label="Buy Put"
            return np.maximum(0, K-S)-abs(P), label
        elif (P<0):
            label="Sell Put"
            return abs(P) - np.maximum(0, K-S), label
    raise ValueError("Invalid option type or premium cannot be zero")
#creating an array of spot prices in the given range for plotting the payoff curve
spot_prices = np.linspace(lower, upper, 300)
#storing the values returned from the function
payoff, label = profit(option, K, spot_prices, P)
#plotting graph
plt.figure(figsize=(8,6))
plt.plot(spot_prices, payoff, label=label)
plt.axhline(0, linewidth=1)
plt.axvline(K, linestyle='--', label="Strike Price")
plt.xlabel("Spot Price at Expiry")
plt.ylabel("Profit / Loss")
plt.title(f"Payoff Diagram: {label}")
plt.legend()
plt.grid(True)
plt.show()

"""The payoff diagrams show that the payoff of an option buyer and seller are mirror images of each other.
The buyer's maximum loss equals the seller's maximum profit and vice versa.
The call option buyer and put option seller both benefit when the market moves higher,
while the put option buyer and call option seller benefit when the market moves lower."""
"""
1. Delta
Delta is the rate of change of premium w.r.t. price of underlying. 
Call Options: 0 to 1. Put Options: -1 to 0.
For European options: Delta ≈ probability that option will expire ITM
2. Gamma
Gamma is the rate of change of Delta with respect to the underlying price.
Gamma is highest when the option is ATM because a small price move can flip the option from OTM to ITM or from ITM back to OTM which means delta changes rapidly i.e. gamma is high.
3. Theta
Theta measures the change in option premium as the time passes.
It is negative for option buyers because as the time passes, value of premium decreases because the uncertainity decreases.
4. Vega
Vega measures the rate of change of premium with respect to volatility.
Volatility means how much the price can move. It is estimated by standard deviation.
Higher volatility increases the probability of large favorable moves.
Hence, Vega is positive for both call and put options.
5. Rho
Rho is the rate of change of option premium w.r.t. risk free interest rate.
Suppose risk-free interest rate increases.
Money today can be invested and earn risk-free interest.
This means ₹1 today is worth more than ₹1 in the future.
Hence rho is positive for call option buyer as it is more valuable to delay money in the future.
Similarly, rho is negative for put option buyer.
"""
