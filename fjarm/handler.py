from .jarm import initf

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    #Set destination host and port
    destination_port = 443
    destination_host = req #TODO:
    out = initf(destination_host, destination_port)

    return out
