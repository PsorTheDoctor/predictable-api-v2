from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import urllib

# Necessary params for hosting at Azure cloud
# Can be omitted at e.g. heroku or local server
params = urllib.parse.quote_plus(
    'Driver={ODBC Driver 13 for SQL Server};' +
    'Server=tcp:predictable-sever.database.windows.net;' +
    'Database=predictable-db;' +
    'Uid=predictable-admin;' +
    'Pwd={SekSI2019};' +
    'Encrypt=yes;' +
    'TrustServerCertificate=no;' +
    'Connection Timeout=30;'
)

engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(params))
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
    Base.metadata.create_all(bind=engine)
