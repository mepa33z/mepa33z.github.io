from modules.python_tools.profit_calculator import calculate_profit
from load_search import find_loads
from truck_manager import get_available_trucks
from rate_checker import filter_good_loads

def run_dispatch():

    loads = find_loads()

    good_loads = filter_good_loads(loads)

    trucks = get_available_trucks()

    if len(good_loads)> 0 and len(trucks)> 0:
       
       evaluated_loads = []

       #Evaluate profibility of loads
       for index, load in good_loads.iterrows():
           
           load_data = {
                "rate": load["rate"],
                "miles": load["miles"]
           }

           profit = calculate_profit(load_data)

           evaluated_loads.append({
                "load_id": load["load_id"],
                "origin": load["origin"],
                "destination": load["destination"],
                "rate": load["rate"],
                "miles": load["miles"],
                "profit":profit
           })

           #Sort loads by carrier profit
         evaluated_loads.sort(key=lambda x: x["profit"]["carrier_profit"],reverse=True)
             
best_load = evaluated_loads[0]
       
truck = trucks.iloc[0]
       
            print("\nDispatch Recommendation:\n")
       
            print(
                f"Assign Truck {truck['truck_id']}" 
                f"to load {best_load['load_id']}" 
                f"{best_load['origin']} -> {best_load['destination']}"
            )
       
            print("\nProfit Breakdown:\n")
       
            print(
                f"Carrier Profit: ${best_load['profit']['carrier_profit']:.2f}"
            )
       
            print(
                f"Fuel Cost Estimate: ${best_load['profit']['driver_pay']:.2f}"
            )
          
    else:
        print("No good dispatch opportunities found")
