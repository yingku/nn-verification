import pandas as pd
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import StandardScaler
from statsmodels.robust import mad
import numpy as np

from TL4HDR.data.preProcess import get_one_race, get_n_years
from TL4HDR.data.tcga import read_data
from TL4HDR.examples.classify_util import run_mixture_cv, run_one_race_cv, \
    run_unsupervised_transfer_cv


def run_cv():
    dataset = read_data('MMRF', 'mRNA', 'OS', 3)
    dataset_w = get_one_race(dataset, 'WHITE')
    dataset_w = get_n_years(dataset_w, 3)
    dataset_b = get_one_race(dataset, 'BLACK')
    dataset_b = get_n_years(dataset_b, 3)
    dataset = get_n_years(dataset, 3)
    X, Y, R, y_sub, y_strat = dataset
    df = pd.DataFrame(y_strat, columns=['RY'])
    df['R'] = R
    df['Y'] = Y
    print(X.shape)
    print(df['RY'].value_counts())
    print(df['R'].value_counts())
    print(df['Y'].value_counts())

    k=-1
    parametrs_b = {'fold': 3, 'k': k, 'val_size':0.0, 'batch_size':4,
                     'learning_rate':0.01, 'lr_decay':0.0, 'dropout':0.5,
                     'L1_reg': 0.001, 'L2_reg': 0.001, 'hidden_layers': [128, 64]}

    res = pd.DataFrame()
    for i in range(20):
        seed = i
        df_m, _mixture_classifiers = run_mixture_cv(seed, dataset, fold=3)
        df_w, _w_classifiers = run_one_race_cv(seed, dataset_w, fold=3)
        df_w = df_w.rename(columns={"Auc": "W_ind"})
        df_b, _b_classifiers = run_one_race_cv(seed, dataset_b, **parametrs_b)
        df_b = df_b.rename(columns={"Auc": "B_ind"})
        df_tl, _unsupervised_transfer_classifiers = run_unsupervised_transfer_cv(seed, dataset, fold=3)

        df1 = pd.concat([df_m, df_w['W_ind'], df_b['B_ind'], df_tl['TL_Auc']],
                        sort=False, axis=1)
        print(df1)
        res = res.append(df1)
    f_name = 'TL4HDR/Result/MM-AA-EA-mRNA-OS-3YR.xlsx'
    res.to_excel(f_name)


def main():
    run_cv()


if __name__ == '__main__':
    main()


