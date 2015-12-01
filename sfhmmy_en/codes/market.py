# Validate that the namecoin id received is well formed
if not re.match(r'^[a-z0-9\-]{1,39}$', msg['namecoin_id']):
    msg['namecoin_id'] = ''

# Update nickname and namecoin id
self.transport.nickname = msg['nickname']
self.transport.namecoin_id = msg['namecoin_id']

if 'burnAmount' in msg:
    del msg['burnAmount']
if 'burnAddr' in msg:
    del msg['burnAddr']

# Update local settings
self.db.updateEntries(
    "settings",
    msg,
    {'market_id': self.transport.market_id}
)
