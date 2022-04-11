""" NYSE Model """
__docformat__ = "numpy"

import logging

from datetime import datetime, timedelta
import pandas as pd


from openbb_terminal.decorators import log_start_end

logger = logging.getLogger(__name__)


@log_start_end(log=logger)
def get_trading_halts(ticker: str, reason: str) -> pd.DataFrame:
    """Get stocks with recent trading halts [Source: NYSE]

    Returns
    -------
    pd.DataFrame
        Trading Halts
    """
    data = pd.read_csv(
        f"https://www.nyse.com/api/trade-halts/historical/download?haltDateFrom="
        f"{str(datetime.utcnow().date() - timedelta(days=365))}"
    )
    data.fillna("N/A", inplace=True)
    del data["Name"]
    data.rename(
        columns={"Symbol": "Ticker", "NYSE Resume Time": "Resume Time"}, inplace=True
    )
    if ticker:
        data = data[data["Ticker"] == ticker.upper()]
    if reason:
        data = data[data["Reason"] == reason.replace("-", " ")]
    return data
