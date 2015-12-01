def upgrade(db_path):
    with dbapi2.connect(db_path) as con:
        cur = con.cursor()

        # Use PRAGMA key to encrypt / decrypt database.
        cur.execute("PRAGMA key = 'passphrase';")

        try:
            cur.execute("ALTER TABLE settings "
                        "ADD COLUMN namecoin_id TEXT")
            print 'Upgraded'
            con.commit()
        except dbapi2.Error as e:
            print 'Exception: %s' % e
