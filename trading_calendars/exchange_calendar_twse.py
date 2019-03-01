from datetime import time
import pandas as pd
from pytz import timezone
from .precomputed_trading_calendar import PrecomputedTradingCalendar

precomputed_taiwan_holidays = pd.to_datetime([
    "1999-01-01",
    "1999-02-10",
    "1999-02-11",
    "1999-02-12",
    "1999-02-15",
    "1999-02-16"
    # TODO
])


class TWSEExchangeCalendar(PrecomputedTradingCalendar):
    """
    Exchange calendar for the Taiwan Stock Exchange (TWSE).

    Open time: 9:00 Asia/Taipei
    Close time: 13:30 Asia/Taipei

    Due to the complexity around the Taiwan exchange holidays, we are
    hardcoding a list of holidays covering 1999-2025, inclusive. There are
    no known early closes or late opens.
    """

    name = "TWSE"
    tz = timezone("Asia/Taipei")
    open_times = (
        (None, time(9, 1)),
    )
    close_times = (
        (None, time(13, 30)),
    )

    @property
    def precomputed_holidays(self):
        return precomputed_taiwan_holidays
