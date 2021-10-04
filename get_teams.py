# Import Libs

import requests
import pandas as pd

def get_teams():

    seasons =input('Enter the seasons you would like to get data from separated by space (ex:"2020-21 2019-20"): ')
    season_list = seasons.split()

    per_mode = 'PerGame'

    headers  = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'x-nba-stats-token': 'true',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'x-nba-stats-origin': 'stats',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Referer': 'https://stats.nba.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    # Column names from stats.nba.com

    columns_list_teams = [
    "LEAGUE_ID",
    "TEAM_ID",
    "TEAM_CITY",
    "TEAM_NAME",
    "START_YEAR",
    "END_YEAR",
    "YEARS",
    "GAMES",
    "WINS",
    "LOSSES",
    "WIN_PCT",
    "PO_APPEARANCES",
    "DIV_TITLES",
    "CONF_TITLES",
    "LEAGUE_TITLES"
    ]
    
    # List of season_ids

    # season_list = ['2020-21', '2019-20', '2018-19', '2017-18', '2016-17']

    dfs=[]

    for season_id in season_list:
        teams_info_url = 'https://stats.nba.com/stats/franchisehistory?LeagueID=00'
        response = requests.get(url=teams_info_url, headers=headers).json()
        teams_info = response['resultSets'][0]['rowSet']
        df = pd.DataFrame(teams_info, columns=columns_list_teams)
        df['season_id'] =season_id
        print(season_id)
        dfs.append(df) 

    # Save DataFrame to an excel file

    final_df = pd.concat(dfs, sort=False)
    final_df.to_excel('teams.xlsx')

if __name__ == '__main__':
    get_teams()