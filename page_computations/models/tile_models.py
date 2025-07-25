import pandas, pathlib, ast, os, json
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

        total = faction_frame.count().sum()
        
        counts = (
            faction_frame.apply(pandas.Series.value_counts)
            .sum(axis=1)
            .div(total)
            .mul(100)
            .round(2)
            .sort_values(ascending=False)
        )
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
        total = faction_frame.count().sum()
        
        counts = (
            faction_frame.apply(pandas.Series.value_counts)
            .sum(axis=1)
            .div(total)
            .mul(100)
            .round(2)
            .sort_values(ascending=False)
        )
        town_counts[faction] = counts.to_dict()

    return town_counts


def fetch_vp_gained_by_scoring_tile(s_year, e_year, map=None, num_players=None, faction=None):
    player_cols = ['game_id', 'year', 'map', 'num_players', 'faction', 'vp_by_round']
    player_data = ds.player_data[player_cols]
    game_data = ds.game_data[['game_id', 'scoring_tiles']]

    players_filtered = player_data[player_data['year'].between(s_year, e_year)]

    if map is not None:
        players_filtered = players_filtered[players_filtered['map'] == map]
    if num_players is not None:
        players_filtered = players_filtered[players_filtered['num_players'] == num_players]
    if faction is not None:
        players_filtered = players_filtered[players_filtered['faction'] == faction]

    players_filtered = players_filtered[['game_id', 'faction', 'vp_by_round']]

    df = players_filtered.merge(game_data, on='game_id', how='inner')


    df['vp_by_round'] = df['vp_by_round'].map(ast.literal_eval)
    df['scoring_tiles'] = df['scoring_tiles'].map(ast.literal_eval)

    df = df[df['vp_by_round'].apply(lambda x: isinstance(x, list) and len(x) >= 6)]
    df = df[df['scoring_tiles'].apply(lambda x: isinstance(x, list) and len(x) >= 6)]

    if df.empty:
        return {}

    rows = []
    for _, row in df.iterrows():
        vp_list = row['vp_by_round']
        tiles = row['scoring_tiles']
        for i in range(6):
            vp_gain = vp_list[i] if i == 0 else vp_list[i] - vp_list[i - 1]
            rows.append({
                'faction': row['faction'],
                'scoring_tile': tiles[i],
                'vp_gain': vp_gain
            })

    vp_df = pandas.DataFrame(rows)

    result = (
        vp_df.groupby('scoring_tile')['vp_gain']
        .mean()
        .round(2)
        .reset_index()
        .rename(columns={'vp_gain': 'avg_vp_gain'})
    )

    return result.set_index('scoring_tile')['avg_vp_gain'].to_dict()
