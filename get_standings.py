# Import Libs

import requests
import pandas as pd

def get_standings():

    seasons =input('Enter the seasons you would like to get data from separated by space (ex:"2020-21 2019-20"): ')
    season_list = seasons.split()

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

    columns_list_standings = [
    "LeagueID",
    "SeasonID",
    "TeamID",
    "TeamCity",
    "TeamName",
    "TeamSlug",
    "Conference",
    "ConferenceRecord",
    "PlayoffRank",
    "ClinchIndicator",
    "Division",
    "DivisionRecord",
    "DivisionRank",
    "WINS",
    "LOSSES",
    "WinPCT",
    "LeagueRank",
    "Record",
    "HOME",
    "ROAD",
    "L10",
    "Last10Home",
    "Last10Road",
    "OT",
    "ThreePTSOrLess",
    "TenPTSOrMore",
    "LongHomeStreak",
    "strLongHomeStreak",
    "LongRoadStreak",
    "strLongRoadStreak",
    "LongWinStreak",
    "LongLossStreak",
    "CurrentHomeStreak",
    "strCurrentHomeStreak",
    "CurrentRoadStreak",
    "strCurrentRoadStreak",
    "CurrentStreak",
    "strCurrentStreak",
    "ConferenceGamesBack",
    "DivisionGamesBack",
    "ClinchedConferenceTitle",
    "ClinchedDivisionTitle",
    "ClinchedPlayoffBirth",
    "ClinchedPlayIn",
    "EliminatedConference",
    "EliminatedDivision",
    "AheadAtHalf",
    "BehindAtHalf",
    "TiedAtHalf",
    "AheadAtThird",
    "BehindAtThird",
    "TiedAtThird",
    "Score100PTS",
    "OppScore100PTS",
    "OppOver500",
    "LeadInFGPCT",
    "LeadInReb",
    "FewerTurnovers",
    "PointsPG",
    "OppPointsPG",
    "DiffPointsPG",
    "vsEast",
    "vsAtlantic",
    "vsCentral",
    "vsSoutheast",
    "vsWest",
    "vsNorthwest",
    "vsPacific",
    "vsSouthwest",
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec"
    ]
    
    # List of season_ids

    # season_list = ['2020-21', '2019-20', '2018-19', '2017-18', '2016-17']

    dfs=[]

    for season_id in season_list:
        standings_info_url = 'https://stats.nba.com/stats/leaguestandingsv3?LeagueID=00&Season='+season_id+'&SeasonType=Regular%20Season'
        response = requests.get(url=standings_info_url, headers=headers).json()
        standings_info = response['resultSets'][0]['rowSet']
        df = pd.DataFrame(standings_info, columns=columns_list_standings)
        df['season_id'] =season_id
        print(season_id)
        dfs.append(df)

    # Save DataFrame to an excel file

    final_df = pd.concat(dfs, sort=False)
    final_df.to_excel('standings.xlsx')

if __name__ == '__main__':
    get_standings()