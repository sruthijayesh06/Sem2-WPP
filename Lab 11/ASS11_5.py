import pandas as pd
import numpy as np

data = {
    'date': pd.to_datetime([
        '2024-01-10', '2024-01-15', '2024-01-20', '2024-02-01', '2024-02-05',
        '2024-03-10', '2024-03-15', '2024-03-20', '2024-01-10'
    ]),
    'artist': ['A', 'A', 'B', 'A', 'B', 'C', 'A', 'B', 'C'],
    'venue':  ['X', 'X', 'Y', 'Y', 'Y', 'X', 'X', 'Y', 'X']
}

df = pd.DataFrame(data)

df['year_month'] = df['date'].dt.to_period('M')

grouped = df.groupby(['year_month', 'artist', 'venue']).size().reset_index(name='count')

year_months = df['year_month'].drop_duplicates()
artists = df['artist'].drop_duplicates()
venues = df['venue'].drop_duplicates()

year_artist_venue = (
    year_months.to_frame(name='year_month')
    .assign(key=1)
    .merge(artists.to_frame(name='artist').assign(key=1), on='key')
    .merge(venues.to_frame(name='venue').assign(key=1), on='key')
    .drop(columns='key')
)

full_data = pd.merge(year_artist_venue, grouped, on=['year_month', 'artist', 'venue'], how='left').fillna(0)

wide_table = full_data.pivot_table(
    index='year_month',
    columns=['artist', 'venue'],
    values='count',
    fill_value=0
)

wide_table.columns = [f"{artist}_{venue}" for artist, venue in wide_table.columns]
wide_table = wide_table.reset_index()

print(wide_table)
