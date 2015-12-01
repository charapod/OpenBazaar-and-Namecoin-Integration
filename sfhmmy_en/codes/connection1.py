self.send_raw(
    json.dumps({
        'type': 'hello',
        'pubkey': self.transport.pubkey,
        'uri': self.transport.uri,
        'senderGUID': self.transport.guid,
        'senderNick': self.transport.nickname,
        'senderNamecoin': self.transport.namecoin_id,
        'v': constants.VERSION
    }),
    cb
)
