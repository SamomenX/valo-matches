import requests
import pandas as pd
import tabulate as tb

url = "https://vlrggapi.vercel.app/match/upcoming"
response = requests.get(url)
data = response.json()['data']['segments']

# Create a dataframe from the data
df = pd.DataFrame(data)
df = df[['team1', 'score1', 'team2', 'score2', 'time_until_match', 'tournament_name']]
df.columns = ['Team Name', 'Score', 'Team Name','Score', 'Match Time', 'Tournament']
df['Match Time'] = df['Match Time'].replace({'LIVE': 'LIVE NOW'})

# Actually I wanted to make the match scores in color but I couldn't lmao 
styled_df = df.style.applymap("style='display:inline'").set_caption('Upcoming Matches').set_table_styles([dict(selector="caption",props=[("text-align", "center")])])

print(tb.tabulate(df, headers='keys', tablefmt='psql'))
