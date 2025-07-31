import joblib, json
import pandas as pd
from page_computations.ML_models import vp_faction_model, vp_no_faction_model, win_class_faction_model, win_class_no_faction_model
from page_computations.ML_models import vp_info, wr_info

faction_to_id = {
    'ACOLYTES': 1,
    'ALCHEMISTS': 2,
    'AUREN': 3,
    'CHAOSMAGICIANS': 4,
    'CULTISTS': 5,
    'DARKLINGS': 6,
    'DRAGONLORDS': 7,
    'DWARVES': 8,
    'ENGINEERS': 9,
    'FAKIRS': 10,
    'GIANTS': 11,
    'HALFLINGS': 12,
    'ICEMAIDENS': 13,
    'MERMAIDS': 14,
    'NOMADS': 15,
    'RIVERWALKERS': 16,
    'SHAPESHIFTERS': 17,
    'SWARMLINGS': 18,
    'WITCHES': 19,
    'YETIS': 20
}

features_faction = [
    "num_players",
    "wr_on_map",
    "seat1",
    "seat2",
    "seat3",
    "seat4",
    "seat5",
    "pick1",
    "pick2",
    "pick3",
    "pick4",
    "pick5",
    "avg_faction_vp",
    "gamebonus_BON1",
    "gamebonus_BON10",
    "gamebonus_BON2",
    "gamebonus_BON3",
    "gamebonus_BON4",
    "gamebonus_BON5",
    "gamebonus_BON6",
    "gamebonus_BON7",
    "gamebonus_BON8",
    "gamebonus_BON9",
    "score_SCORE1",
    "score_SCORE2",
    "score_SCORE3",
    "score_SCORE4",
    "score_SCORE5",
    "score_SCORE6",
    "score_SCORE7",
    "score_SCORE8",
    "score_SCORE9",
    "game_ACOLYTES",
    "game_ALCHEMISTS",
    "game_AUREN",
    "game_CHAOSMAGICIANS",
    "game_CULTISTS",
    "game_DARKLINGS",
    "game_DRAGONLORDS",
    "game_DWARVES",
    "game_ENGINEERS",
    "game_FAKIRS",
    "game_GIANTS",
    "game_HALFLINGS",
    "game_ICEMAIDENS",
    "game_MERMAIDS",
    "game_NOMADS",
    "game_RIVERWALKERS",
    "game_SHAPESHIFTERS",
    "game_SWARMLINGS",
    "game_WITCHES",
    "game_YETIS",
    "player_ACOLYTES",
    "player_ALCHEMISTS",
    "player_AUREN",
    "player_CHAOSMAGICIANS",
    "player_CULTISTS",
    "player_DARKLINGS",
    "player_DRAGONLORDS",
    "player_DWARVES",
    "player_ENGINEERS",
    "player_FAKIRS",
    "player_GIANTS",
    "player_HALFLINGS",
    "player_ICEMAIDENS",
    "player_MERMAIDS",
    "player_NOMADS",
    "player_RIVERWALKERS",
    "player_SHAPESHIFTERS",
    "player_SWARMLINGS",
    "player_WITCHES",
    "player_YETIS",
    "map_126FE960806D587C78546B30F1A90853B1ADA468",
    "map_224736500D20520F195970EB0FD4C41DF040C08C",
    "map_2AFADC63F4D81E850B7C16FB21A1DCD29658C392",
    "map_30B6DED823E53670624981ABDB2C5B8568A44091",
    "map_735B073FD7161268BB2796C1275ABDA92ACD8B1A",
    "map_91645CDB135773C2A7A50E5CA9CB18AF54C664C4",
    "map_95A66999127893F5925A5F591D54F8BCB9A670E6",
    "map_B109F78907D2CBD5699CED16572BE46043558E41",
    "map_BE8F6EBF549404D015547152D5F2A1906AE8DD90",
    "map_C07F36F9E050992D2DAF6D44AF2BC51DCA719C46",
    "map_FDB13A13CD48B7A3C3525F27E4628FF6905AA5B1",
    "R1_SCORE1", "R1_SCORE2", "R1_SCORE3", "R1_SCORE4", "R1_SCORE5", "R1_SCORE6", "R1_SCORE7", "R1_SCORE8", "R1_SCORE9",
    "R2_SCORE1", "R2_SCORE2", "R2_SCORE3", "R2_SCORE4", "R2_SCORE5", "R2_SCORE6", "R2_SCORE7", "R2_SCORE8", "R2_SCORE9",
    "R3_SCORE1", "R3_SCORE2", "R3_SCORE3", "R3_SCORE4", "R3_SCORE5", "R3_SCORE6", "R3_SCORE7", "R3_SCORE8", "R3_SCORE9",
    "R4_SCORE1", "R4_SCORE2", "R4_SCORE3", "R4_SCORE4", "R4_SCORE5", "R4_SCORE6", "R4_SCORE7", "R4_SCORE8", "R4_SCORE9",
    "R5_SCORE1", "R5_SCORE2", "R5_SCORE3", "R5_SCORE4", "R5_SCORE5", "R5_SCORE6", "R5_SCORE7", "R5_SCORE8", "R5_SCORE9",
    "R6_SCORE1", "R6_SCORE2", "R6_SCORE3", "R6_SCORE4", "R6_SCORE5", "R6_SCORE6", "R6_SCORE7", "R6_SCORE8", "R6_SCORE9"
]


features_no_faction = [
    item for item in features_faction if not (
        item.startswith('game_') or item.startswith('seat') or item.startswith('pick')
    )
]



def fetch_vp_score_prediction(num_players, map_id, b_tiles, s_tiles, g_factions):
    is_faction = len(g_factions) > 0

    model = vp_faction_model if is_faction else vp_no_faction_model
    features = features_faction if is_faction else features_no_faction

    input_dict = {feat: 0 for feat in features}
    input_dict['num_players'] = int(num_players)
    input_dict[f'map_{map_id.upper()}'] = 1


    for bon in b_tiles:
        input_dict[f'gamebonus_{bon.upper()}'] = 1
    for score in s_tiles:
        input_dict[f'score_{score.upper()}'] = 1
    if is_faction:
        for faction in g_factions:
            input_dict[f'game_{faction.upper()}'] = 1
        
        
        for i in range(5):
            if i < len(g_factions):
                input_dict[f'seat{i+1}'] = faction_to_id.get(g_factions[i], 0)
                input_dict[f'pick{5-(i+1)}'] = faction_to_id.get(g_factions[i], 0)
            else:
                input_dict[f'seat{i+1}'] = 0
                input_dict[f'pick{5-(i+1)}'] = 0


    
    
    for i, tile_name in enumerate(s_tiles):
        input_dict[f'R{i+1}_{tile_name}'] = 1


    all_factions = [f for f in faction_to_id.keys() if f not in g_factions]


    prediction_results = {f: 0 for f in all_factions}
    for faction in all_factions:
        current_input = input_dict.copy()
        current_input[f'player_{faction}'] = 1
        current_input['wr_on_map'] = wr_info[faction.lower()][map_id]
        current_input['avg_faction_vp'] = vp_info[faction.lower()]

        input_df = pd.DataFrame([current_input])[features]

        prediction = model.predict(input_df)[0]
        prediction_results[faction] = float(prediction)




    return prediction_results
        



def fetch_classification_prediction(num_players, map_id, b_tiles, s_tiles, g_factions):
    is_faction = len(g_factions) > 0

    model = win_class_faction_model if is_faction else win_class_no_faction_model
    features = features_faction if is_faction else features_no_faction

    input_dict = {feat: 0 for feat in features}
    input_dict['num_players'] = int(num_players)
    input_dict[f'map_{map_id.upper()}'] = 1


    for bon in b_tiles:
        input_dict[f'gamebonus_{bon.upper()}'] = 1
    for score in s_tiles:
        input_dict[f'score_{score.upper()}'] = 1
    if is_faction:
        for faction in g_factions:
            input_dict[f'game_{faction.upper()}'] = 1
        
        
        for i in range(5):
            if i < len(g_factions):
                input_dict[f'seat{i+1}'] = faction_to_id.get(g_factions[i], 0)
                input_dict[f'pick{5-(i+1)}'] = faction_to_id.get(g_factions[i], 0)
            else:
                input_dict[f'seat{i+1}'] = 0
                input_dict[f'pick{5-(i+1)}'] = 0


    
    
    for i, tile_name in enumerate(s_tiles):
        input_dict[f'R{i+1}_{tile_name}'] = 1


    all_factions = [f for f in faction_to_id.keys() if f not in g_factions]


    prediction_results = {}
    for faction in all_factions:
        current_input = input_dict.copy()
        current_input[f'player_{faction}'] = 1
        current_input['wr_on_map'] = wr_info[faction.lower()][map_id]
        current_input['avg_faction_vp'] = vp_info[faction.lower()]

        input_df = pd.DataFrame([current_input])[features]

        win_prob = model.predict_proba(input_df)[0][1]

        if win_prob < 0.3:
            risk_level = 2 
        elif win_prob < 0.5:
            risk_level = 1 
        else:
            risk_level = 0 

        prediction_results[faction] = {
            "win_prob": round(float(win_prob), 3),
            "risk_level": risk_level
        }


    return prediction_results