import requests
import urllib.parse
# import json

main_api = "https://www.mapquestapi.com/directions/v2/route?"
# orig = "Washington, D.C."
# dest = "Baltimore, Md"

# This key may have been revoked
key = "GWx3msmdWRFjMjpn9KqvVMefttbzUCjZ"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    
    url = main_api + \
        urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL: " + url)

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print(f"API Status: {json_status} = A successful route call.\n")
        print("=============================================")
        print(f"Directions from {orig} to {dest}")
        print(f'Trip Duration:   {json_data["route"]["formattedTime"]}')
        print(
            f'Kilometers:           {json_data["route"]["distance"]*1.61:.2f}')
        # print(f'Fuel Used (Gal): {json_data["route"]["fuelUsed"]}')
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print(f'{each["narrative"]} ({each["distance"]*1.61:.2f}  km)')
        print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print(f"Status Code: {json_status}; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print(f"Status Code: {json_status}; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print(f"For Staus Code: {json_status}; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
        
# Formatting json data
# json_formatted_str = json.dumps(json_data, indent=2)
# print(json_formatted_str)