import numpy as np
import pandas as pd


def cat_convertor(data):
    df = data['O2 Volts Bank 1 sensor 2(V)']
    A = np.mean(df)
    return A
