import sqlalchemy
import json

def connect(user, password, db, host='localhost', port=5432):
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)
    return con, meta




con,meta=connect('postgres','123','postgres')
table_name = meta.tables['tej_branch']
res2=table_name.select().where(table_name.c.index==1)

#
resp=[]
for row in con.execute(res2):
   resp.append(row)


print(json.dumps([dict(r) for r in resp],ensure_ascii=False))





# jdbc:postgresql://localhost:5432/postgres