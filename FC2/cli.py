import click
from FC2 import utils
from FC2 import aircraft
from FC2 import airport
from FC2 import country
from FC2 import currency
from FC2 import itenerary
import routing
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
        for routes in testRoutes:
            locations = []
            cleanedInput = utils_obj.checkInputErrors(routes, airports, aircrafts)
            filteredData = it_obj.getIteneraryData(cleanedInput,mergedData)
            for locs in cleanedInput[0]:
                locations.append((filteredData.get(locs).get('Latitude'),filteredData.get(locs).get('Longitude')))
            airportAdjGraph = it_obj.getAdjacencyGraph(locations)
            _route.getRoute(airportAdjGraph,cleanedInput,_aircraftsDict,filteredData)

    
if __name__=="__main__":
    main()
