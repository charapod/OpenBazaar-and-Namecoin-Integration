def is_valid_namecoin(namecoin, guid):
    if not namecoin or not guid:
        return False

    server = DNSChainServer.Server(
        constants.DNSCHAIN_SERVER_IP, ""
    )
    _log.info("Looking up namecoin id: %s", namecoin)
    try:
        data = server.lookup("id/" + namecoin)
    except (DNSChainServer.DataNotFound, 
            DNSChainServer.MalformedJSON):
        _log.info(
            'Claimed remote namecoin id not found: %s', 
            namecoin
        )
        return False

    return data.get('openbazaar') == guid
