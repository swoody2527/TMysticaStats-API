valid_maps = [
        '126fe960806d587c78546b30f1a90853b1ada468',
        '95a66999127893f5925a5f591d54f8bcb9a670e6',
        'be8f6ebf549404d015547152d5f2a1906ae8dd90',
        'fdb13a13cd48b7a3c3525f27e4628ff6905aa5b1',
        '91645cdb135773c2a7a50e5ca9cb18af54c664c4',
        '2afadc63f4d81e850b7c16fb21a1dcd29658c392']

valid_factions = [
        "auren", "witches",
        "mermaids", "swarmlings",
        "halflings", "cultists",
        "engineers", "dwarves",
        "alchemists", "chaosmagicians",
        "fakirs", "nomads",
        "giants", "darklings",
        "icemaidens", "yetis",
        "acolytes", "dragonlords",
        "shapeshifters", "riverwalkers"
        ]

dlc_factions = [
    'yetis', 'icemaidens',
    'acolytes', 'dragonlords',
    'riverwalkers', 'shapeshifters'
]


def validate_route_inputs(s_year, e_year, map=None, num_players=None, faction=None, require_map=False, require_faction=False, require_players=False):


    if require_map and not map:
        return 'Map required for search.', None
    if require_faction and not faction:
        return 'Faction required for search.', None
    if require_players and not num_players:
        return 'Player count required for search', None
    
    if not s_year or not e_year:
        return 'Missing 1 or more parameters for search.', None

    if map and map not in valid_maps:
        return 'Invalid map id.', None

    if faction and faction not in valid_factions:
        return 'Invalid faction choice.', None
    
    try:
        s_year = int(s_year)
        e_year = int(e_year)
        num_players = int(num_players) if num_players is not None else None
    except ValueError:
        return '1 or more invalid parameter type(s).', None
    
    if num_players and num_players > 6:
        return 'Player number filter out of bounds.', None
    
    if s_year and e_year == 2013:
        if faction in dlc_factions:
            return 'Invalid search including expansion factions for 2013. Expansion factions released in 2014.', None
    
    if s_year < 2013 or e_year > 2025:
        return 'Year parameter out of bounds.', None
    
    return None, [s_year, e_year, map, num_players, faction]