from sdn_controller_api.odlutil import send_request


def get_topology():
    api = "/operational/network-topology:network-topology"
    return send_request(api)['network-topology']['topology'][0]
