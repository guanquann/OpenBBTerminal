""" NYSE View """
__docformat__ = "numpy"

import logging
import os

from openbb_terminal.decorators import log_start_end
from openbb_terminal.helper_funcs import export_data, print_rich_table
from openbb_terminal.rich_config import console
from openbb_terminal.stocks.discovery import nyse_model

logger = logging.getLogger(__name__)


@log_start_end(log=logger)
def display_trading_halts(ticker: str, num_stocks: int, reason: str, export: str):
    """Display stocks with recent trading halts. [Source: NYSE]

    Parameters
    ----------
    ticker: str
        Optional filter by ticker
    num_stocks: int
        Number of stocks to display
    reason: str
        Reason for trading halt
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    df = nyse_model.get_trading_halts(ticker=ticker, reason=reason).head(num_stocks)

    if df.empty:
        console.print("No data found.")
    else:
        print_rich_table(
            df,
            headers=list(df.columns),
            show_index=False,
            title="Trading Halts",
        )
    console.print("")

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "trading_halts",
        df,
    )
