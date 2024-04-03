import pandas
import requests

from secret import private_info


def url_maker(energy_type: str) -> str:
    """
    Function returns the URL required to connect to the Octopus API based
    on the contents of 'secret.py'
    Parameter: energy_type - either 'gas' or 'electric'
    Returns: the URL required to connect to the API
    """
    base_url = "https://api.octopus.energy/v1"
    if energy_type == "gas":
        mprn: int = private_info()["gas_mprn"]
        sn: str = private_info()["gas_serial_number"]
        url: str = f"{base_url}/gas-meter-points/{mprn}/meters/{sn}/consumption/"
        return url
    elif energy_type == "electric":
        mpan: int = private_info()["electric_mpan"]
        sn: str = private_info()["electric_serial_number"]
        url: str = (
            f"{base_url}/electricity-meter-points/{mpan}/meters/{sn}/consumption/"
        )
        return url
    else:
        return "error"


def get_dataframe(energy: str, payload: dict):
    """
    Creates the Pandas dataframe for the respective energy type
    Parameter: The energy type, being either 'electric' or 'gas'
    Returns: The Pandas dataframe with the energy readings
    """
    energy_request = requests.get(
        url_maker(energy),
        auth=(private_info()["api_key"], ""),
        params=payload,
        timeout=60,
    )
    energy_dataframe = pandas.DataFrame(energy_request.json()["results"])
    return energy_dataframe
