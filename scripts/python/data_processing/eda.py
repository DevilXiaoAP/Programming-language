import pandas_profiling
import pandas as pd


def eda(in_file, out_file):
    data = pd.read_csv(in_file, sep=',')
    pfr = pandas_profiling.ProfileReport(data)
    pfr.to_file(out_file)


if __name__ == '__main__':
    in_file = 'labels.csv'
    out_file = 'labels.html'
    eda(in_file, out_file)
    print('eda done!')

