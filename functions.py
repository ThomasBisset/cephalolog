import pandas
import requests

from secret import private_info


def url_maker(energy_type):
    """
        Makes the URL required for the request
    """
    base_url = f"https://api.octopus.energy/v1/"
    if energy_type == "gas":
        mprn = private_info()["gas_mprn"]
        sn = private_info()["gas_serial_number"]
        url = f"{base_url}gas-meter-points/{mprn}/meters/{sn}/consumption/"
        return url
    elif energy_type == "electric":
        mpan = private_info()["electric_mpan"]
        sn = private_info()["electric_serial_number"]
        url = f"{base_url}electricity-meter-points/{mpan}/meters/{sn}/consumption/"
        return url
    else:
        return "error"


def get_dataframe(energy):
    """
        Creates the dataframe for the respective energy type
    """
    energy_request = requests.get(url_maker(energy), auth=(private_info()["api_key"], ""), params="page_size=25000")
    energy_dataframe = pandas.DataFrame(energy_request.json()["results"])
    return energy_dataframe
