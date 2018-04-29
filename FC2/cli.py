import click
from FC2 import utils
from FC2 import aircraft
from FC2 import airport
from FC2 import country
from FC2 import currency
from FC2 import itenerary
from FC2 import price
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
            _route = routing.Routes()
            locations = []
            cleanedInput = utils_obj.checkInputErrors(routes, airports, aircrafts)
            filteredData = it_obj.getIteneraryData(cleanedInput,mergedData)
            for locs in cleanedInput[0]:
                locations.append((filteredData.get(locs).get('Latitude'),filteredData.get(locs).get('Longitude')))
            airportAdjGraph = it_obj.getAdjacencyGraph(locations)
            routeList,routeDistances,airCRange,aircraft_type=_route.getRoute(airportAdjGraph,cleanedInput,_aircraftsDict,filteredData)
            if not airCRange == None:
                isRoutePossible = _route.isPossible(airCRange, routeDistances)
                if isRoutePossible:
                    finalRoute, finalDistances = _route.getFinalAcRoute(
                        airCRange, routeList, routeDistances)
                    totalDistance = sum(finalDistances)
                    _price = price.Price()
                    finalRoute, finalPrice = _price.getPrice(
                        finalRoute, finalDistances, filteredData, airCRange)
                    finalRoute.append(aircraft_type)
                    finalRoute.append(finalPrice)
                    finalCSV.append(finalRoute)
                else:
                    total_distance="Route Not Possible"
                    ogRoute = list(cleanedInput[0])
                    ogRoute.append(aircraft_type)
                    ogRoute.append("No Route")
                    finalCSV.append(ogRoute)
            else:
                total_distance = sum(routeDistances)
                routeList.append(total_distance)
                finalCSV.append(routeList)
        if not finalCSV == []:
            utils_obj.to_csv(finalCSV)
    
if __name__=="__main__":
    main()
