import requests

# covid19_2020_open_line_list: 'https://docs.google.com/spreadsheets/d/1itaohdPiAeniCXNlntNztZ_oRvjh0HsGuJXUJWET008/export?format=tsv#gid=0    #htmlview?sle=true#gid=0'
# inside: https://docs.google.com/spreadsheets/d/1itaohdPiAeniCXNlntNztZ_oRvjh0HsGuJXUJWET008/htmlview?sle=true#
# https://docs.google.com/spreadsheets/d/1itaohdPiAeniCXNlntNztZ_oRvjh0HsGuJXUJWET008/edit#gid=0

tsv_url='https://docs.google.com/spreadsheets/d/1itaohdPiAeniCXNlntNztZ_oRvjh0HsGuJXUJWET008/export?format=tsv#gid=0'
res=requests.get(url=tsv_url)
with open('kaggle-data/covid19_2020_open_line_list-outside_hubei.tsv', 'wb') as f:
    f.write(res.content)

tsv_url='https://docs.google.com/spreadsheets/d/1itaohdPiAeniCXNlntNztZ_oRvjh0HsGuJXUJWET008/export?format=tsv'
res=requests.get(url=tsv_url)
with open('kaggle-data/covid19_2020_open_line_list-hubei.tsv', 'wb') as f:
    f.write(res.content)


h=read_tsv('kaggle-data/covid19_2020_open_line_list-hubei.tsv')