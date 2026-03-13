def analyze_load(load):

    rate = load["rate"]
    miles = load["miles"]

    dollars_per_mile = rate / miles

    market_rate = 2.80 #simulated average market rate

    score = 0
    recommendation = "ACCEPT"
    counter_offer = rate

    if dollars_per_mile < market_rate * 0.9:
        score = 3
        recommendation = "REJECT"
        counter_offer = rate + 400

    elif market_rate * 0.9: <= dollars_per_mile < market_rate:
        score = 6
        recommendation = "NEGOTIATE"
        counter_offer = rate + 200

        elif dollars_per_mile >= market_rate:
            score = 9
            recommendation = "ACCEPT"
            counter_offer = rate
        
    return {
        "dollars_per_mile": round(dollars_per_mile, 2),
        "market_rate": market_rate,
        "score": score,
        "recommendation": recommendation,
        "counter_offer": counter_offer
    }
