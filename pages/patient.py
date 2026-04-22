import requests

def fetch_doctors(specialty, zipcode):

    url = "https://npiregistry.cms.hhs.gov/api/"

    params = {
        "version": "2.1",
        "limit": 10,
        "enumeration_type": "NPI-1",
    }

    # optional filters
    if specialty != "All":
        params["taxonomy_description"] = specialty

    if zipcode:
        params["postal_code"] = zipcode

    response = requests.get(url, params=params)
    data = response.json()

    doctors = []

    for item in data.get("results", []):

        basic = item.get("basic", {})
        addresses = item.get("addresses", [{}])

        doctors.append({
            "name": " ".join(basic.get("first_name", "") + " " + basic.get("last_name", "")),
            "specialty": basic.get("primary_taxonomy", {}).get("desc", "General"),
            "zip": addresses[0].get("postal_code", "N/A")
        })

    return doctors
