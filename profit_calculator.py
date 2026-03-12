from config.system_settings.dispatch_settings import *

def calculate_profit(load):
    try:
        #Extract values from load parameter
        rate = load['rate']
        miles = load['miles']
    except KeyError as e:
        raise ValueError(f"Missing required key in load: {e}")
    
    if miles == 0:
        raise ValueError("Miles cannot be zero")
    
    #Rate per mile
    rate_per_mile = rate / miles
    
    #Fuel estimate
    gallons_used = miles / TRUCK_MPG
    fuel_cost = gallons_used * FUEL_PRICE_PER_GALLON
    
    #Driver pay
    driver_pay = miles * DRIVER_PAY_PER_MILE
    
    #Dispatcher fee
    dispatch_fee = rate * DISPATCH_PERCENTAGE
    
    #Carrier profit
    carrier_profit = rate - fuel_cost - driver_pay - dispatch_fee
    
    return {
        "rate_per_mile": rate_per_mile,
        "fuel_cost": fuel_cost,
        "driver_pay": driver_pay,
        "dispatch_commission": dispatch_fee,
        "carrier_profit": carrier_profit
    }