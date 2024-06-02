import pandas as pd
file_path = 'product_view_analysis_report.csv'
df = pd.read_csv(file_path)
grouped_df = df.groupby(['Parent org', 'Brand']).agg({'Product View Count': 'sum'}).reset_index()
parent_org_cumulative = grouped_df.groupby('Parent org')['Product View Count'].sum().reset_index()
sorted_parent_org_cumulative = parent_org_cumulative.sort_values(by='Product View Count', ascending=False)
sorted_df = pd.merge(sorted_parent_org_cumulative, grouped_df, on='Parent org', how='left')
sorted_df = sorted_df.sort_values(by=['Product View Count_x', 'Product View Count_y'], ascending=[False, False])
current_parent_org = None
for index, row in sorted_df.iterrows():
    if current_parent_org != row['Parent org']:
        if current_parent_org is not None:
            print()
        current_parent_org = row['Parent org']
        print(f"{row['Parent org']}: {row['Product View Count_x']}")
    print(f"  {row['Brand']}: {row['Product View Count_y']}")
