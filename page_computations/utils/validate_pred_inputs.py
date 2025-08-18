valid_maps = [
    '126FE960806D587C78546B30F1A90853B1ADA468',
    '95A66999127893F5925A5F591D54F8BCB9A670E6',
    'BE8F6EBF549404D015547152D5F2A1906AE8DD90',
    'FDB13A13CD48B7A3C3525F27E4628FF6905AA5B1',
    '91645CDB135773C2A7A50E5CA9CB18AF54C664C4',
    '2AFADC63F4D81E850B7C16FB21A1DCD29658C392'
]

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



valid_bonus_tiles = [f'BON{i+1}' for i in range(11)]

valid_score_tiles = [f'SCORE{i+1}' for i in range(9)]

def validate_model_inputs(is_factions, num_players, map, b_tiles, s_tiles, factions):

    if is_factions and not len(factions):
        return 'Your input indicated you had enemy faction data but none was provided. If you are first picking and have no enemy faction data please select the toggle.', None

    if not num_players or not map:
        return 'Missing player number or map parameter.', None
    
    if len(b_tiles) == 0 or len(s_tiles) == 0:
        return 'Missing bonus/scoring tile information.', None

    try:
        num_players = int(num_players)
    except ValueError:
        return 'Invalid type for No. Players', None
    
    if num_players < 2 or num_players > 5:
        return 'Cannot make predictions. No. players must be between 2 and 5', None
    
    if map not in valid_maps:
        return 'Invalid map id.', None
    
    for tile in b_tiles:
        if tile not in valid_bonus_tiles:
            return 'Invalid bonus tile.', None
        
    for tile in s_tiles:
        if tile not in valid_score_tiles:
            return 'Invalid score tile.', None
    if factions:
        for faction in factions:
            if faction.lower() not in valid_factions:
                return 'Invalid faction choice.', None
        
    return None, [is_factions, num_players, map, b_tiles, s_tiles, factions]
    

