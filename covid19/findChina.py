def findChina(df):
    x = 'Province/' # id China with this
    y = 'Hubei'# id China with this
    for df in tables:
        if (x in df.columns.values):
            if (y in df[x].tolist()):
                print(re.split('\\s+',df['Cumulative'].iloc[-1]))
