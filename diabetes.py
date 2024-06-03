from ucimlrepo import fetch_ucirepo
# fetch dataset
diabetes_130_us_hospitals_for_years_1999_2008 = fetch_ucirepo(id=296)

# data (as pandas dataframes)
X = diabetes_130_us_hospitals_for_years_1999_2008.data.features
y = diabetes_130_us_hospitals_for_years_1999_2008.data.targets


X = X.drop(columns=['weight', 'payer_code'])
X['race'] = X['race'].fillna('Unknown')
X['medical_specialty'] = X['medical_specialty'].fillna('Unknown')
X['max_glu_serum'] = X['max_glu_serum'].fillna('-1') # Changing None, to -1
X['A1Cresult'] = X['A1Cresult'].fillna('-1') # Changing None, to -1
print(X.iloc[135])