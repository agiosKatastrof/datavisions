df['Date'] = pd.to_datetime(df['Date received'],infer_datetime_format=True)
df_grouped = df.groupby('Company').count()[['Complaint ID']]
df_issues_dates = df.groupby('Date').count()[['Complaint ID']]
df_issues_dates = df_issues_dates.reset_index()
df_issues_dates = df_issues_dates.rename(columns={'Complaint ID':"Issue Counts"})
