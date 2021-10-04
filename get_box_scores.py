# Import Libs

import requests
import pandas as pd

def get_box_scores():

    season_type = input('Insert the season type, "Regular+Season" or "Playoffs": ')

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

    columns_list_box_scores = [
    "SEASON_ID",
    "PLAYER_ID",
    "PLAYER_NAME",
    "TEAM_ID",
    "TEAM_ABBREVIATION",
    "TEAM_NAME",
    "GAME_ID",
    "GAME_DATE",
    "MATCHUP",
    "WL",
    "MIN",
    "FGM",
    "FGA",
    "FG_PCT",
    "FG3M",
    "FG3A",
    "FG3_PCT",
    "FTM",
    "FTA",
    "FT_PCT",
    "OREB",
    "DREB",
    "REB",
    "AST",
    "STL",
    "BLK",
    "TOV",
    "PF",
    "PTS",
    "PLUS_MINUS",
    "FANTASY_PTS",
    "VIDEO_AVAILABLE",
    ]

    # List of season_ids

    # season_list = ['2020-21', '2019-20', '2018-19', '2017-18', '2016-17']

    dfs=[]

    for season_id in season_list:
        box_score_info_url = 'https://stats.nba.com/stats/leaguegamelog?Counter=1000&DateFrom=&DateTo=&Direction=DESC&LeagueID=00&PlayerOrTeam=P&Season='+season_id+'&SeasonType='+season_type+'&Sorter=DATE'
        #json response
        response = requests.get(url=box_score_info_url, headers=headers).json()
        #pulling just desired data
        box_score_info = response['resultSets'][0]['rowSet']
        df = pd.DataFrame(box_score_info, columns=columns_list_box_scores)
        df['season_id'] =season_id
        print(season_id)
        dfs.append(df)

    # Save DataFrame to an excel file

    final_df = pd.concat(dfs, sort=False)
    final_df.to_excel('box_scores_'+ season_type +'.xlsx')

if __name__ == '__main__':
    get_box_scores()