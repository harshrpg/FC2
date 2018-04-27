import click
from FC2 import utils
from FC2 import aircraft
from FC2 import airport
from FC2 import country
from FC2 import currency
from FC2 import itenerary
import routing
import time
@click.command()
@click.argument("file", type=click.Path(exists=True), default="./data/testroutes.csv")
def main(file):
    
    # Creating the required Objects
    airport_obj = airport.Airport()
    aircraft_obj = aircraft.Aircraft()
    currency_obj = currency.Currency()
    country_obj = country.Country() 
    utils_obj = utils.Utility()
    it_obj = itenerary.Itenerary()
    _route = routing.Routes()

    # Getting the data
    airports = airport_obj.get_AirportData('./data/airports_new.csv')
    curr = currency_obj.get_CurrencyData('./data/currencyrates.csv')
    countries = country_obj.get_CountryData('./data/countrycurrency.csv')
    aircrafts = aircraft_obj.get_AircraftData('./data/aircraft.csv')
    _aircraftsDict = aircrafts.set_index('code').to_dict(orient='index')

    
    # Pass this file to Utility to check for errors
    testRoutes = utils_obj.handleTestInput(file)
    mergedData = utils_obj.getDict(airports, curr, countries[[
                                   'name', 'currency_alphabetic_code']])
    if len(testRoutes) == 0:
        print("None of the Test Lists had unique airports. Please try again")
    else:
        finalCSV = []
        for routes in testRoutes:
            # print("Route: ",routes)
            # time.sleep(2)
            locations = []
            cleanedInput = utils_obj.checkInputErrors(routes, airports, aircrafts)
            # print("cleanedInput: ",cleanedInput)
            # time.sleep(2)
            filteredData = it_obj.getIteneraryData(cleanedInput,mergedData)
            for locs in cleanedInput[0]:
                locations.append((filteredData.get(locs).get('Latitude'),filteredData.get(locs).get('Longitude')))
            # print("Locations: ",locations)
            # time.sleep(2)
            airportAdjGraph = it_obj.getAdjacencyGraph(locations)
            # print("Airport Adj Graph: ",airportAdjGraph)
            # time.sleep(2)
            routeList,routeDistances,airCRange=_route.getRoute(airportAdjGraph,cleanedInput,_aircraftsDict,filteredData)
            isRoutePossible = _route.isPossible(airCRange, routeDistances)
            # print("{}\n{}\n{}".format(routeList,routeDistances,airCRange))
            if isRoutePossible:
                # print("Possible")
                finalRoute, finalDistances = _route.getFinalAcRoute(
                    airCRange, routeList, routeDistances)
                # print("Final Route: {}\n, Final Distances: {}".format(finalRoute,finalDistances))
                totalDistance = sum(finalDistances)
                finalRoute.append(totalDistance)
                finalCSV.append(finalRoute)
            else:
                # print("Not Possible")
                total_distance="Route Not Possible"
                ogRoute = list(cleanedInput[0])
                print("OG::::::::::::", ogRoute)
                ogRoute.append("No Route")
                print("FInal OG ROUTE::::::::::",ogRoute)
                finalCSV.append(ogRoute)
                # utils_obj.to_csv(cleanedInput,total_distance)
        print(finalCSV)
        if not finalCSV == []:
            utils_obj.to_csv(finalCSV)
    
if __name__=="__main__":
    main()
