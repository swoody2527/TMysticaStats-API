import pandas, pathlib, ast, os
from ..utils import data_store as ds


def fetch_common_score_tile_order(s_year, e_year, map=None, num_players=None, faction=None):
    '''HOW MANY IN EACH POSITION'''
    game_data = ds.game_data
    filtered_data = game_data[(game_data['year'].between(s_year, e_year)) &
                              (game_data['map'] == map if map is not None else True) &
                              (game_data['num_players'] == num_players if num_players is not None else True)]

    s_tiles_data = filtered_data['scoring_tiles']
    s_tiles_frame = pandas.DataFrame(ast.literal_eval(row) for row in s_tiles_data)

    counts = {f'round{col}': s_tiles_frame[col].value_counts(normalize=True).mul(100).round(2).to_dict() for col in s_tiles_frame.columns}

    return counts


def fetch_popular_bonus_tiles_by_round(s_year, e_year, map=None, num_players=None, faction=None):
    player_data = ds.player_data
    filtered_data = player_data[(player_data['year'].between(s_year, e_year)) &
                                (player_data['map'] == map if map is not None else True) &
                                (player_data['num_players'] == num_players if num_players is not None else True) &
                                (player_data['faction'] == faction if faction is not None else True)]

    b_tiles_frame = pandas.DataFrame(ast.literal_eval(row) for row in filtered_data['bonus_tiles'])

    counts = {f'round{col}': b_tiles_frame[col].value_counts(normalize=True).mul(100).round(2).to_dict() for col in b_tiles_frame.columns}

    return counts


def fetch_favor_tiles_by_faction(s_year, e_year, map=None, num_players=None, faction=None):
    player_data = ds.player_data
    filtered_data = player_data[(player_data['year'].between(s_year, e_year)) &
                                (player_data['map'] == map if map is not None else True) &
                                (player_data['num_players'] == num_players if num_players is not None else True)]

    all_factions = filtered_data['faction'].unique()
    favour_counts = {}

    for faction in all_factions:
        faction_data = filtered_data[filtered_data['faction'] == faction]
        faction_favours = faction_data['favour_tiles']
        faction_frame = pandas.DataFrame(ast.literal_eval(row) for row in faction_favours)

        counts = faction_frame.apply(pandas.Series.value_counts).sum(axis=1).sort_values(ascending=False)
        favour_counts[faction] = counts.to_dict()

    return favour_counts


def fetch_town_tiles_by_faction(s_year, e_year, map=None, num_players=None, faction=None):
    player_data = ds.player_data
    filtered_data = player_data[(player_data['year'].between(s_year, e_year)) &
                                (player_data['map'] == map if map is not None else True) &
                                (player_data['num_players'] == num_players if num_players is not None else True)]

    all_factions = filtered_data['faction'].unique()
    town_counts = {}

    for faction in all_factions:
        faction_data = filtered_data[filtered_data['faction'] == faction]
        faction_favours = faction_data['town_tiles']
        faction_frame = pandas.DataFrame(ast.literal_eval(row) for row in faction_favours)

        counts = faction_frame.apply(pandas.Series.value_counts).sum(axis=1).sort_values(ascending=False)
        town_counts[faction] = counts.to_dict()

    return town_counts


def fetch_vp_gained_by_scoring_tile(s_year, e_year, map=None, num_players=None, faction=None):
    import ast
    import pandas as pd

    player_data = ds.player_data
    game_data = ds.game_data

    players_filtered = player_data[(player_data['year'].between(s_year, e_year)) &
                                   (player_data['map'] == map if map else True) &
                                   (player_data['num_players'] == num_players if num_players else True) &
                                   (player_data['faction'] == faction if faction else True)].copy()

    games_filtered = game_data[['game_id', 'scoring_tiles']].copy()
    df = players_filtered.merge(games_filtered, on='game_id', how='inner')

    df['vp_by_round'] = df['vp_by_round'].apply(lambda row: ast.literal_eval(row))
    df['scoring_tiles'] = df['scoring_tiles'].apply(lambda row: ast.literal_eval(row))

    df = df[df['vp_by_round'].apply(lambda row: isinstance(row, list) and len(row) >= 6)]
    df = df[df['scoring_tiles'].apply(lambda row: isinstance(row, list) and len(row) >= 6)]

    df_expanded = df.apply(lambda row: [
        {
            'faction': row['faction'],
            'scoring_tile': row['scoring_tiles'][i],
            'vp_gain': row['vp_by_round'][i] if i == 0 else row['vp_by_round'][i] - row['vp_by_round'][i - 1]
        }
        for i in range(6)
    ], axis=1).explode()

    vp_df = pd.DataFrame([d for d in df_expanded])

    result = (
        vp_df.groupby('scoring_tile')['vp_gain']
        .mean()
        .round(2)
        .reset_index()
        .rename(columns={'vp_gain': 'avg_vp_gain'})
    )

    return result.set_index('scoring_tile')['avg_vp_gain'].to_dict()
