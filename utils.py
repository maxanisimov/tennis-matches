import pandas
from typing import Union


def get_atp_matches(first_year: int, last_year: int, concatenate: bool = True) -> Union[dict, pandas.DataFrame]:
    """Get ATP matches data from Jeff Sackmann's repo."""
    dataframes = {}
    for year in range(first_year, last_year+1):
        dataframes[year] = pandas.read_csv(f'https://raw.githubusercontent.com/JeffSackmann/tennis_atp/master/atp_matches_{year}.csv')

    if concatenate:
        matches = pandas.concat(dataframes.values())
        # tourney_date is a start date of the correspnding tournament!
        matches['Tournament Start Date'] = pandas.to_datetime(matches['tourney_date'], format='%Y%m%d')
        matches = matches.sort_values(['Tournament Start Date', 'match_num']).set_index(['Tournament Start Date', 'match_num'])
    else:
        matches = dataframes

    return matches

def get_atp_betting_odds(first_year: int, last_year: int, concatenate: bool = True) -> Union[dict, pandas.DataFrame]:
    """Get ATP betting odds data from tennis-data.co.uk."""
    dataframes = {}
    for year in range(first_year, last_year+1):
        dataframes[year] = pandas.read_excel(f'http://www.tennis-data.co.uk/{year}/{year}.xlsx')

    if concatenate:
        odds = pandas.concat(dataframes.values()).set_index('Date')
    else:
        odds = dataframes

    return odds
