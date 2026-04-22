import requests

def fetch_doctors(specialty="", zipcode=""):

    url = "https://npiregistry.cms.hhs.gov/api/"

    params = {
        "version": "2.1",
        "limit": 10,
        "enumeration_type": "NPI-1"
    }

    if specialty and specialty != "All":
        params["taxonomy_description"] = specialty

    if zipcode:
        params["postal_code"] = zipcode

    try:
        res = requests.get(url, params=params)
        data = res.json()
    except:
        return []

    doctors = []

    for item in data.get("results", []):

        basic = item.get("basic", {})
        address = item.get("addresses", [{}])[0]

        first = basic.get("first_name", "")
        last = basic.get("last_name", "")

        name = f"{first} {last}".strip()

        doctors.append({
            "name": name if name else "Unknown Doctor",
            "specialty": basic.get("primary_taxonomy", {}).get("desc", "General Practice"),
            "zip": address.get("postal_code", "N/A")
        })

    return doctors
