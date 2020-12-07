# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
zero_value = dataiku.Dataset("zero_value")
zero_value_df = zero_value.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

values_python_df = zero_value_df # For this sample code, simply copy input to output


# Write recipe outputs
values_python = dataiku.Dataset("values_python")
values_python.write_with_schema(values_python_df)
