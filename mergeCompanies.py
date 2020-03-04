def mergeCompanies(dfT,n,df):
    columns = ['Date']
    dfm = pd.DataFrame(columns=columns)
    i=0
    while i<n:
        df1 = pickCompany(dfT['Company'][i], df)
        dfm = pd.merge(dfm, df1, on='Date', how='outer')
        i += 1
    dfm = dfm.fillna(0)
    return dfm  
