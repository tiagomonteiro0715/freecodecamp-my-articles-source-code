from blackscholes import BlackScholesCall, BlackScholesPut

def calculate_option_prices(S, K, T, r, sigma, q):
    """
    Calculate the Black-Scholes option prices for European call and put options using the 'blackscholes' package.

    Parameters:
    S : float - current stock price
    K : float - strike price of the option
    T : float - time to maturity (in years)
    r : float - risk-free interest rate (annual as a decimal)
    sigma : float - volatility of the underlying stock (annual as a decimal)
    q : float - annual dividend yield (as a decimal)

    Returns:
    tuple - (call price, put price)
    """
    # Creating instances of BlackScholesCall and BlackScholesPut
    call_option = BlackScholesCall(S=S, K=K, T=T, r=r, sigma=sigma, q=q)
    put_option = BlackScholesPut(S=S, K=K, T=T, r=r, sigma=sigma, q=q)

    # Get call and put prices
    call_price = call_option.price()
    put_price = put_option.price()

    return call_price, put_price

# Example usage:
# Current stock price: $100
# Strike price: $105
# Time to maturity: 1 year
# Risk-free interest rate: 0.05% (as a decimal: 0.0005)
# Volatility: 20% (as a decimal: 0.20)
# Dividend yield: 0%
call_price, put_price = calculate_option_prices(100, 105, 1, 0.0005, 0.20, 0.0)
print("Call Price: {:.6f}, Put Price: {:.6f}".format(call_price, put_price))
