# https://github.com/schneiderkamplab/syntheval/blob/main/src/syntheval/metrics/privacy

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OrdinalEncoder

from syntheval import SynthEval
from sklearn.model_selection import train_test_split

import pdb

from copy import deepcopy

def calculate_metric(args, _real_data, _synthetic):
    real_data = deepcopy(_real_data)
    synthetic = deepcopy(_synthetic)

    evaluator = SynthEval(real_data)

    evaluator.evaluate(synthetic, hit_rate={"thres_percent": .5})

    result = evaluator._raw_results['hit_rate']['hit rate']
  
    return result