import pandas as pd
import os

def combine_performances():
    all_files = os.listdir('performance')
    all_files = [f for f in all_files if f.endswith('.csv') and f != 'all.csv']
    combined_df = pd.DataFrame()
    for f in all_files:
        df = pd.read_csv(f'performance/{f}')
        combined_df = pd.concat([combined_df, df])
    combined_df.rename(columns={'Unnamed: 0': 'model'}, inplace=True)
    combined_df.to_csv('performance/all.csv', index=False)
    with open("performance/all.md", 'w') as md:
        combined_df.to_markdown(buf=md, index=False)
    
if __name__ == '__main__':
    combine_performances()