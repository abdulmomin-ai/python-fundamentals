def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()
    df['Marks'] = df['Marks'].astype(int)
    df['StudyHours'] = df['StudyHours'].astype(int)
    return df 