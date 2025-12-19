import numpy as np
import matplotlib.pyplot as plt

def calculate_payoff(spot_prices, strike_price, premium, option_type, position):
    # Calculate intrinsic value based on Option Type
    if option_type == 'Call':
        # Call value = max(0, S - K)
        intrinsic_value = np.maximum(0, spot_prices - strike_price)
    elif option_type == 'Put':
        # Put value = max(0, K - S)
        intrinsic_value = np.maximum(0, strike_price - spot_prices)
    else:
        raise ValueError("Option type must be 'Call' or 'Put'")

    # Calculate Profit/Loss based on Position (Buy vs Sell)
    if position == 'Buy':
        # Buy: Profit = Intrinsic Value - Premium
        return intrinsic_value - premium
    elif position == 'Sell':
        # Sell: Profit = Premium - Intrinsic Value
        return premium - intrinsic_value
    else:
        raise ValueError("Position must be 'Buy' or 'Sell'")

def plot_payoffs(K, P, spot_range_buffer=50):
    """
    Generates the 2x2 plot for all 4 strategies.
    """
    # Define range of Spot Prices (S)
    # Range from K - 50 to K + 50
    S = np.arange(K - spot_range_buffer, K + spot_range_buffer, 1)

    # 4 cases
    scenarios = [
        ('Call', 'Buy', 'Long Call (Bullish)'),
        ('Call', 'Sell', 'Short Call (Bearish)'),
        ('Put', 'Buy', 'Long Put (Bearish)'),
        ('Put', 'Sell', 'Short Put (Bullish)')
    ]

    #intial plot
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(f'Vanilla Option Payoffs (Strike K={K}, Premium P={P})', fontsize=16)
    
    # Flatten axes array for easy iteration
    axes_flat = axes.flatten()

    for i, (opt_type, pos, title) in enumerate(scenarios):
        # P/L calc
        pl = calculate_payoff(S, K, P, opt_type, pos)
        
        # plotting
        ax = axes_flat[i]
        ax.plot(S, pl, label=f'{pos} {opt_type}', linewidth=2, 
                color='green' if pos == 'Buy' else 'red')
        
        # graph formatting
        ax.set_title(title)
        ax.set_xlabel('Spot Price (S) at Expiry')
        ax.set_ylabel('Profit / Loss')
        ax.axhline(0, color='black', linewidth=1, linestyle='--') # Zero line
        ax.axvline(K, color='gray', linestyle=':', label='Strike Price') # Strike line
        
        # breakeven points
        if opt_type == 'Call':
            be = K + P if pos == 'Buy' else K + P
        else:
            be = K - P if pos == 'Buy' else K - P
            
        ax.plot(be, 0, 'bo', label=f'Breakeven ({be})')
        
        ax.grid(True, alpha=0.3)
        ax.legend()

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

# taking input
strike_price = int(input("Enter Strike Price: "))  
premium = int(input("Enter Strike Price: "))         

# generating plot
plot_payoffs(strike_price, premium)

"""
Greeks Explained
1. Delta : How much the premium price changes for each rupee change in spot price. Calls
           usually have positive deltas (0 to +1) and puts have negative deltas (0 to -1).
2. Gamma: Rate of change of delta. Higher typically gamma indicates higher risk in position
3. Theta: Option premiums decay with time. Usually negative for calls and positive for puts.
4. Vega: Relative price change wrt to implied volatility (IV). Options are often pricier when
         volatility is high.

"""