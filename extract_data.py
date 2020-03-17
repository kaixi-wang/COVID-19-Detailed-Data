import re
import os
import sys
from bs4 import BeautifulSoup
import pandas as pd
pd.set_option("display.min_rows", 15)
pd.set_option("display.max_rows", 101)
pd.set_option("display.max_columns", 101)
pd.set_option('max_colwidth', 1000)



def html2tsv(html_file_path: str, out_dir='sheets-tsv', ret_files=True):
    """

    :param html_file_path: path to downloaded google sheets .html file (for published public google sheets
    :return:
    """

    # setup output filenames
    base_fn=(html_file_path.split('/')[-1]).split('.html')[0]
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    with open(html_file_path, 'r') as f:
        data=f.read()
    soup=BeautifulSoup(data, "html.parser")
    sheets=soup.find_all('tbody')

    # Parse HTML sheets
    data=[[t.find_next_siblings() for t in sheet.find_all('th', id=True)] for sheet in sheets]
    parsed=list(map(lambda x: [[txt.text for txt in line] for line in x], data))    # data formatted as parsed[sheet][line]

    for i,sheet in enumerate(parsed):
        fn=base_fn+"--{}.tsv".format(i)
        out_path=os.path.join(out_dir, fn)
        with open(out_path, 'a+') as f:
            for cells in sheet:
                row = '\t'.join(cells)
                f.write(row + '\n')
        print("Saved sheet {} to {}".format(i, out_path))
    if ret_files == True:
        return

def infer_column_header(tsv_filepath):
    with open(tsv_filepath) as f:
        num_cols=0
        idx=0
        for row in f.readlines():
            cols=[c for c in row.split('\t') if len(c)>0]
            if len(cols)>=num_cols:
                num_cols=len(cols)
                idx += 1
            else:
                return max([idx-1,0])

def read_tsv(tsv_filepath):
    header_idx=infer_column_header(tsv_filepath)
    return pd.read_csv(tsv_filepath, sep='\t', header=header_idx, na_values='n/a', error_bad_lines=False, warn_bad_lines=True)

def read_csv(csv_filepath):
    return pd.read_csv(csv_filepath, na_values='n/a', error_bad_lines=False,
                       warn_bad_lines=True)
#
# # DXY.cn data (3/13/2020)
# html_file='html-data/Kudos to DXY.cn Last update03132020.html'
# tsv_filepath='/Volumes/iMac_external_SSD/github-repos/COVID-19-Detailed-Data/sheets-tsv/Kudos to DXY.cn Last update03132020--0.tsv'
# df=read_tsv(tsv_filepath)
# df['first']=df['summary'].str.contains('First')
# df['first_related']=df['summary'].str.contains('first')
# df['Wuhan']=df['summary'].str.contains('Wuhan', case=False)
#
# # Kaggle coronavirusdataset
# input_dir='kaggle-data/coronavirusdataset'
# data={}
# for fn in os.listdir(input_dir):
#     fil = fn.split('.')[0]
#     data[fil]=read_csv(os.path.join(input_dir, fn))