from numpy.random import seed
import pandas as pd
import random as rn
import os

from TL4HDR.data.preProcess import get_one_race, get_n_years, normalize_dataset, standarize_dataset, get_dataset
from TL4HDR.data.tcga import read_data
from TL4HDR.examples.classify_util import run_mixture_cv, run_one_race_cv, \
    run_CCSA_transfer
from tensorflow import set_random_seed

seed(11111)
set_random_seed(11111)
os.environ['PYTHONHASHSEED'] = '0'
os.environ["KERAS_BACKEND"] = "tensorflow"
rn.seed(11111)

def run_cv(cancer_type, feature_type, target, years=3):

    print (cancer_type, feature_type, target, years)
    dataset = get_dataset(cancer_type=cancer_type, feature_type=feature_type, target=target, groups=("WHITE", "BLACK"))
    # dataset = read_data(cancer_type, feature_type[0], target, years)
    dataset = standarize_dataset(dataset)
    dataset_w = get_one_race(dataset, 'WHITE')
    dataset_w = get_n_years(dataset_w, years)
    dataset_b = get_one_race(dataset, 'BLACK')
    dataset_b = get_n_years(dataset_b, years)

    dataset_tl = normalize_dataset(dataset)
    dataset_tl = get_n_years(dataset_tl, years)

    dataset = get_n_years(dataset, years)

    k = -1
    X, Y, R, y_sub, y_strat = dataset
    df = pd.DataFrame(y_strat, columns=['RY'])
    df['R'] = R
    df['Y'] = Y
    print(X.shape)
    print(df['RY'].value_counts())
    print(df['R'].value_counts())
    print(df['Y'].value_counts())

    parametrs_mix = {'fold': 3, 'k': k, 'val_size':0.0, 'batch_size':20,
                     'learning_rate':0.01, 'lr_decay':0.0, 'dropout':0.5,
                     'L1_reg': 0.001, 'L2_reg': 0.001, 'hidden_layers': [128, 64]}
    parametrs_w = {'fold': 3, 'k': k, 'val_size':0.0, 'batch_size':20,
                     'learning_rate':0.01, 'lr_decay':0.0, 'dropout':0.5,
                     'L1_reg': 0.001, 'L2_reg': 0.001, 'hidden_layers': [128, 64]}
    parametrs_b = {'fold': 3, 'k': k, 'val_size':0.0, 'batch_size':4,
                     'learning_rate':0.01, 'lr_decay':0.0, 'dropout':0.5,
                     'L1_reg': 0.001, 'L2_reg': 0.001, 'hidden_layers': [128, 64]}
    parameters_CCSA = {'fold': 3, 'n_features': k, 'alpha':0.3, 'batch_size':20, 'learning_rate':0.01,
                       'hidden_layers': [100], 'dr':0.0, 'momentum':0.0,
                       'decay':0.0, 'sample_per_class':2}

    res = pd.DataFrame()
    for i in range(20):
        seed = i
        df_m, _mixture_classifiers = run_mixture_cv(seed, dataset, **parametrs_mix)
        df_w, _w_classifiers = run_one_race_cv(seed, dataset_w, **parametrs_w)
        df_w = df_w.rename(columns={"Auc": "W_ind"})
        df_b, _b_classifiers = run_one_race_cv(seed, dataset_b, **parametrs_b)
        df_b = df_b.rename(columns={"Auc": "B_ind"})
        df_tl, _ccsa_transfer_classifiers = run_CCSA_transfer(seed, dataset_tl, **parameters_CCSA)

        df1 = pd.concat([df_m, df_w['W_ind'], df_b['B_ind'], df_tl['TL_Auc']],
                        sort=False, axis=1)
        print (df1)
        res = res.append(df1)
    f_name = 'TL4HDR/Result/' + cancer_type + '-AA-EA-' + feature_type[0] + '-' + target + '-' + str(years) + 'YR.xlsx'
    res.to_excel(f_name)

def main():
    run_cv('KIPAN', 'Protein', 'PFI', years=3)

if __name__ == '__main__':
    main()
