def private_info() -> dict:
    """
        Account details - see https://octopus.energy/dashboard/developer/
        Do not share these details with others!
        Make sure this file is ignored by Git!
    """
    private: dict = {
        "api_key": "API_KEY",
        "electric_mpan": MPAN_NUMBER,
        "electric_serial_number": "ELECTRIC_METER_SERIAL_NUMBER",
        "gas_mprn": MPRN_NUMBER,
        "gas_serial_number": "GAS_METER_SERIAL_NUMBER",
    }
    return private
