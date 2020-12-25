import pyodbc
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('mssql+pyodbc://predictable-id:84n4n4.P13' +
                       '@predictable-server2.database.windows.net,1433/' +
                       'predictable-db?' +
                       'driver=ODBC+Driver+17+for+SQL+Server}',
                       convert_unicode=True)

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
