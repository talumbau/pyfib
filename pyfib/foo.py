import fwrapper
import pandas as pd

def fib_df(n):
    return pd.DataFrame(fwrapper.fib(n), columns=["fib"])

