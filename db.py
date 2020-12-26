import pyodbc
import urllib
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

params = urllib.parse.quote_plus(
    'Driver={ODBC Driver 13 for SQL Server};' +
    'Server=tcp:predictable-server2.database.windows.net,1433;' +
    'Database=predictable-db' +
    'Uid=predictable-id' +
    'Pwd=84n4n4.P13' +
    'Encrypt=yes;' +
    'TrustServerCertificate=no;' +
    'Connection Timeout=30;')

conn_str = 'mssql+pyodbc:///?odbc_connect=' + params
engine = create_engine(conn_str)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import models.subscriber
    import models.past_price
    import models.future_price
    import models.entry
    import models.order
    Base.metadata.create_all(bind=engine)
