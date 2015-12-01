def _on_message(self, msg):

    # here goes the application callbacks
    # we get a "clean" msg which is a dict holding whatever

    pubkey = msg.get('pubkey')
    uri = msg.get('uri')
    guid = msg.get('senderGUID')
    nickname = msg.get('senderNick', '')[:120]
    msg_type = msg.get('type')
    namecoin = msg.get('senderNamecoin')

    # Checking for malformed URIs
    if not network_util.is_valid_uri(uri):
        self.log.error('Malformed URI: %s', uri)
        return

    # Validate the claimed namecoin in DNSChain
    if not trust.is_valid_namecoin(namecoin, guid):
        msg['senderNamecoin'] = ''

    self.log.info(
        'Received message type "%s" from "%s" %s %s',
        msg_type, nickname, uri, guid
    )
    self.log.datadump('Raw message: %s', 
            json.dumps(msg, ensure_ascii=False))
    self.dht.add_peer(uri, pubkey, guid, nickname)
    self.trigger_callbacks(msg['type'], msg)
