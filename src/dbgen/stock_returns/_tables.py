import sqlalchemy as db
from sqlalchemy.orm.decl_api import DeclarativeMeta


def OHLCV(base) -> DeclarativeMeta:
    """
    This function takes a SQLAlchemy declarative_base and returns a SQLAlchemy 
    table/mapper. The mapper will take the open, low, high, close and volume
    of a stock during a specified time period as well as the datetime 
    and timestamp from the beginning of the time period and the timestep from
    the open of a period to the close of a period and map it to a row in a 
    database titled "ohlcv". The mapper contains of an underlying sqlalchemy
    metadata object that can be combined with an engine to create the table
    if it does not exist. See example usage below.
    
    Parameters
    --------------------------------------------------
    base : sqlalchemy.orm.declarative_base
        A declarative_base that will be inheirited by the underlying class
       

    Returns
    --------------------------------------------------
    _OHLCV(base) : SQLAlchemy table/mapper class 
        _OHLCV maps rows to a sql table names "ohlcv" under a 
        sqlalchemy.orm.sessionmaker setting. 

    Example Usage
    --------------------------------------------------
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.orm import declarative_base as Base
    
    base = Base()
    _OHLCV = OHLCV(base)

    engine = create_engine(...)

    if not database_exists(engine.url):
        create_database(engine.url) 
    base.metadata.create_all(bind=engine)

    session = sessionmaker(bind=engine)()

    entry = _OHLCV(
        datetime, ticker, open, high, low, close, volumne, timestamp
    )

    session.add(entry)
    session.commit()
    session.close()
    """

    class _OHLCV(base):
        # table name for User model
        __tablename__ = "ohlcv"
    
        # user columns
        datetime = db.Column(
            db.DateTime(), primary_key=True, autoincrement=False
        )
        ticker = db.Column(
            db.String(5), primary_key=True, autoincrement=False
        )
        open = db.Column(db.Float())
        high = db.Column(db.Float())
        low = db.Column(db.Float())
        close = db.Column(db.Float())
        volume = db.Column(db.Float())
        timestamp = db.Column(db.Integer())
     
        def __init__(
            self,
            datetime,
            ticker,
            open,
            high,
            low,
            close,
            volume,
            timestamp,
        ):
            """
            Parameters
            --------------------------------------------------
            datetime : datetime.datetime
                The datetime from the start of the period for the stock price

            ticker : str
                stock ticker

            open : float 
                open price of the period

            high : float
                high price of the period

            low : float 
                low price of the period

            close : float 
                close price of the period

            volume : float
                volume price of the period

            timestamp : float 
                unix timestamp of the datetime

            Returns
            --------------------------------------------------
            A mapable object that can be sent to a sql table with the use of
            sqlalchemy.creat_engine and sqlalchemy.orm.sessionmaker. See 
            example usage in help(OHLCV)
            """
            self.datetime = datetime 
            self.ticker = ticker
            self.open = open 
            self.high = high
            self.low = low
            self.close = close
            self.volume = volume
            self.timestamp = timestamp

    return _OHLCV


def TransactionHistory(base) -> DeclarativeMeta:
    """
    This function takes a SQLAlchemy declarative_base and returns a SQLAlchemy 
    table/mapper. The mapper will take information of a stock transaction and 
    return a mappable object that can then be sent sql table titled
    "transaction_history". The mapper contains of an underlying sqlalchemy
    metadata object that can be combined with an engine to create the table
    if it does not exist. See example usage below.
    
    Parameters
    --------------------------------------------------
    base : sqlalchemy.orm.declarative_base
        A declarative_base that will be inheirited by the underlying class
       

    Returns
    --------------------------------------------------
    _Transaction_History(base) : SQLAlchemy table/mapper class 
        _Transaction_History maps rows to a sql table named 
        "transaction_history" under a sqlalchemy.orm.sessionmaker setting. 

    Example Usage
    --------------------------------------------------
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.orm import declarative_base as Base
    
    base = Base()
    _Transaction_History = Transaction_History(base)

    engine = create_engine(...)

    if not database_exists(engine.url):
        create_database(engine.url) 
    base.metadata.create_all(bind=engine)

    session = sessionmaker(bind=engine)()

    entry = _Transaction_History(
        datetime, ticker, position_type, action, no_shares, at_price
    )

    session.add(entry)
    session.commit()
    session.close()
    """

    class _TransactionHistory(base):
        # table name for User model
        __tablename__ = "transaction_history"
    
        # user columns
        user_id = db.Column(
            db.Integer(), primary_key=True, autoincrement=False
        )
        trans_id = db.Column(
            db.Integer(), primary_key=True, autoincrement=True
        )
        datetime = db.Column(
            db.DateTime()
        )
        ticker = db.Column(
            db.String(6),
        )
        position_type = db.Column(
            db.Integer(), 
            db.CheckConstraint("position_type = 1 or position_type = -1")
        )
        action = db.Column(
            db.Integer()
        )
        no_shares = db.Column(db.Float())
        at_price = db.Column(db.Float())
     
        def __init__(
            self,
            user_id,
            datetime,
            ticker,
            position_type,
            action,
            no_shares,
            at_price
        ):
            """
            Parameters
            --------------------------------------------------
            user_id : int
                ID of the investor

            datetime : datetime.datetime
                The datetime of the transaction.

            ticker : str
                stock ticker

            position_type : float 
                Indication of whether the transaction is a short or long. 1.0
                refers to a long position and -1.0 refers to a short position.

            action : float
                Indication of whether the transaction refers to a sell or a 
                purchase. 1.0 indicates a purchase and -1.0 indicates a sell.

            no_shares : float 
                Amount of shares either bought or sold in the transaction.

            at_price : float 
                The price per share of the transaction.

            Returns
            --------------------------------------------------
            A mapable object that can be sent to a sql table with the use of
            sqlalchemy.creat_engine and sqlalchemy.orm.sessionmaker. See
            example usage in help(Transaction_History)
            """
            self.user_id = user_id 
            self.datetime = datetime 
            self.ticker = ticker 
            self.position_type = position_type 
            self.action = action
            self.no_shares = no_shares
            self.at_price = at_price

    return _TransactionHistory 


def Portfolio(base) -> DeclarativeMeta:
    """
    Suggestion
    --------------------------------------------------
    This function should predominatly used to only create the portfolio table
    and it should be used in tandom with Transaction_History with the use of
    a SQL trigger. A Trigger should be applied to take the
    transaction_history rows and calculate the performace of the portfolio 
    ranther than using this function and its underlying _Portfolio(base)
    class directly to update the portfolio table.

    This function takes a SQLAlchemy declarative_base and returns a SQLAlchemy 
    table/mapper.
    The mapper will map information about a investorys portfolio to a table
    named "portfolio".
    The mapper contains of an underlying sqlalchemy
    metadata object that can be combined with an engine to create the table
    if it does not exist. See example usage below.
    
    Parameters
    --------------------------------------------------
    base : sqlalchemy.orm.declarative_base
        A declarative_base that will be inheirited by the underlying class
       

    Returns
    --------------------------------------------------
    _Porfolio(base) : SQLAlchemy table/mapper class 
        _Portfolio maps rows to a sql table named "portfolio" under a 
        sqlalchemy.orm.sessionmaker setting. 

    Example Usage
    --------------------------------------------------
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.orm import declarative_base as Base
    
    base = Base()
    _Portfolio = Portfolio(base)

    engine = create_engine(...)

    if not database_exists(engine.url):
        create_database(engine.url) 
    base.metadata.create_all(bind=engine)

    session = sessionmaker(bind=engine)()

    entry = Portfolio(
        ticker, position_type, position, last_price, cost_basis, 
        total_invested, current_value, realized_profit, gain 
    )

    session.add(entry)
    session.commit()
    session.close()
    """
    class _Portfolio(base):
        # table name for User model
        __tablename__ = "portfolio"
    
        # user columns
        user_id = db.Column(
            db.Integer, primary_key=True, autoincrement=False
        )
        ticker = db.Column(
            db.String(6), primary_key=True, autoincrement=False
        )
        position_type = db.Column(
            db.Integer(), 
            db.CheckConstraint("position_type = 1 or position_type = -1"),
            primary_key=True,
            autoincrement=False
        )
        position = db.Column(
            db.Integer()
        )
        last_price = db.Column(db.Float())
        cost_basis = db.Column(db.Float())
        total_invested = db.Column(db.Float())
        current_value = db.Column(db.Float())
        realized_profit = db.Column(db.Float())
        gain = db.Column(db.Float())

        def __init__(
            self,
            user_id,
            ticker,
            position_type,
            position,
            last_price,
            cost_basis,
            total_invested,
            current_value,
            realized_profit,
            gain
        ):
            """
            These values will be auto-calculated by 
            './stock_returns/sql/trans_to_port_trig.sql'.

            Parameters
            --------------------------------------------------
            user_id : int 
                ID of the investor.

            ticker : str
                The stock's ticker.

            position_type : float
                Indication whether the position is a short or a long.
                1.0 indicated a long and -1.0 indicates a short.

            position : float
                The amount of shares either long or short.

            last_price : float
                The last known price of the stock of the position.

            cost_basis : float
                *   For a long postition, this is the average price per share 
                    of the position and this is only affected by new purchases.
                    For a purchase of size no_shares at a price of at_price, 
                    the cost basis is calculated to be 
                        cost_basis = (
                            ((position - no_shares) * cost_basis) 
                            + no_shares * at_price
                        ) / position,
                    where position = position + no_shares is the size of the 
                    position after the purchase of no_shares new shares.
                *   For a short postition, this represents the average price 
                    per share that the investory needs to pay back and this 
                    is only affected by borrowing more of the stock.
                    For a short of size no_shares at a price of at_price, 
                    the cost basis is calculated to be 
                        cost_basis = (
                            (-1.0 * (position + no_shares) * cost_basis) 
                            + (no_shares * at_price)
                        ) / position * -1.0,
                    where position = position - no_shares is the size of the 
                    position after the short of no_share additional shares.

            total_invested : float 
                *   For a long position, this is the total amount of money that
                    has been invested into the stock.
                *   For a short position, this is the total amount of money 
                    that has gone into repaying the total amount borrowed.

            current_value : float 
                last_price * position. 
                *   For a long position...
                *   For a short position...

            realized_profit : float 
                *   For long position, this is the total amount of money that 
                    has been accrued through selling stock. 
                    This number being positive does not mean that the 
                    invester is up on his investment, it just means that 
                    they have sold some of their stock.
                *   For a short position, this is...

            gain : float 
                This is the percent gain that the investor has on thier
                investment.
                *   For a long position...
                *   For a short position...

            Returns
            --------------------------------------------------
            A mapable object that can be sent to a sql table with the use of
            sqlalchemy.creat_engine and sqlalchemy.orm.sessionmaker. See
            example usage in help(Portfolio).
            """
            self.user_id = user_id 
            self.ticker = ticker
            self.position_type = position_type 
            self.position = position 
            self.last_price = last_price 
            self.cost_basis = cost_basis
            self.total_invested = total_invested 
            self.current_value = current_value 
            self.realized_profit = realized_profit 
            self.gain = gain

    return _Portfolio 
