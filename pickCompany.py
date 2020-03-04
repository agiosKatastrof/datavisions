def pickCompany(company,df):
    dfC = df.loc[df['Company'] == company]
    dfC_dates = dfC.groupby('Date').count()[['Complaint ID']]
    dfC_dates = dfC_dates.reset_index()
    dfC_dates = dfC_dates.rename(columns={'Complaint ID':company}) 
    return dfC_dates
