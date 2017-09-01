# pull_it_together.py
# 
# 
def hotel_cost(nights):
    return 140 * nights   
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
def rental_car_cost(days):
    rental = 40 * days
    if days >= 7:
        rental -= 50
    elif days >= 3:
        rental -= 20
    return rental
def trip_cost(city, days):
    city = plane_ride_cost(city)
    days = hotel_cost(days) + rental_car_cost(days)
    stay = city + days
    return stay
print trip_cost("Los Angeles", 90)
print trip_cost("Tampa", 10000)
years = days / 52
weeks = days / 7
months = days / 30
print years, weeks, months