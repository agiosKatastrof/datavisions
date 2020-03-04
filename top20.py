dfT20 = df_grouped.sort_values('Complaint ID', ascending=False).head(20)
dfT20.insert(loc=1, column='Top 20', value=np.arange(len(dfT20)) +1)
dfT20.rename(columns={'Complaint ID':"Issue Counts"})
dfT20 = dfT20.reset_index()
dfAT20 = df.loc[df['Company'].isin(dfT20['Company'])] #reduce original data to T20
