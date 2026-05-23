input_filename = "./files/country_info.txt"

countries = {}

with open(input_filename) as country_file:
    country_info = country_file.readline()
    for row in country_file:
        data = row.strip("\n").split("|")
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep="\n\t")
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict
        countries[code.casefold()] = country_dict

while True:
    country_inp = input("Enter the country:\t").casefold()
    if country_inp in countries:
        capital_city = countries[country_inp]['capital']
        print(capital_city)
    elif country_inp == "quit":
        break
