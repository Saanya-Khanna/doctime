import requests

# -----------------------
# FALLBACK DATA (ALWAYS WORKS)
# -----------------------
FALLBACK_DOCTORS = [
    {"name": "Dr. Sarah Johnson", "specialty": "Cardiologist", "zip": "76013"},
    {"name": "Dr. Michael Lee", "specialty": "Dermatologist", "zip": "75001"},
    {"name": "Dr. Priya Patel", "specialty": "Pediatrician", "zip": "75201"},
    {"name": "Dr. Emily Chen", "specialty": "Neurologist", "zip": "75080"},
]

# -----------------------
# REAL API (BEST EFFORT)
# -----------------------
def fetch_doctors(specialty="All", zipcode=""):

    url = "https://npiregistry.cms.hhs.gov/api/"

    params = {
        "version": "2.1",
        "limit": 10,
        "enumeration_type": "NPI-1"
    }

    # NOTE: NPI is picky → don't over-filter
    if zipcode:
        params["postal_code"] = zipcode

    try:
        res = requests.get(url, params=params, timeout=5)
        data = res.json()

        doctors = []

        for item in data.get("results", []):

            basic = item.get("basic", {})
            address = item.get("addresses", [{}])[0]

            first = basic.get("first_name", "")
            last = basic.get("last_name", "")

            name = f"{first} {last}".strip()

            doctors.append({
                "name": name if name else "Unknown Doctor",
                "specialty": "General Practice",
                "zip": address.get("postal_code", "N/A")
            })

        # If API returns something → use it
        if doctors:
            return doctors

    except:
        pass

    # FALLBACK ALWAYS RETURNS DATA
    return filter_fallback(specialty, zipcode)


# -----------------------
# FALLBACK FILTER LOGIC
# -----------------------
def filter_fallback(specialty, zipcode):

    results = []

    for doc in FALLBACK_DOCTORS:

        match_specialty = (specialty == "All" or doc["specialty"] == specialty)
        match_zip = (zipcode == "" or doc["zip"] == zipcode)

        if match_specialty and match_zip:
            results.append(doc)

    return results
