# Include sender information and version
data['guid'] = self.guid
data['senderGUID'] = self.transport.guid
data['uri'] = self.transport.uri
data['pubkey'] = self.transport.pubkey
data['senderNick'] = self.transport.nickname
data['senderNamecoin'] = self.transport.namecoin_id
data['v'] = constants.VERSION
