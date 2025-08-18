from ..utils import validate_inputs as val

def test_require_map():
    # Map required but not provided
    err, res = val.validate_route_inputs(2020, 2025, require_map=True)

    assert err == 'Map required for search.'
    assert res is None

def test_require_faction():
    # Faction required but not provided
    err, res = val.validate_route_inputs(2020, 2025, require_faction=True)

    assert err == 'Faction required for search.'
    assert res is None

def test_require_player_count():
    # Player count required but not provided
    err, res = val.validate_route_inputs(2020, 2025, require_players=True)

    assert err == 'Player count required for search.'
    assert res is None

def test_no_years():
    # Year Parameters not given.
    err, res = val.validate_route_inputs(None, None, faction='dwarves')

    assert err == 'Missing year parameters.'
    assert res is None

def test_invalid_map():
    # Map Id is not valid.
    err, res = val.validate_route_inputs(2020, 2025, map='INVALID_MAP_ID')

    assert err == 'Invalid map id.'
    assert res is None

def test_invalid_faction():
    # Faction is not valid.
    err, res = val.validate_route_inputs(2020, 2025, faction='INVALID_FACTION')

    assert err == 'Invalid faction choice.'
    assert res is None

def test_invalid_types():
    # Years cannot be cast to ints.
    err, res = val.validate_route_inputs('INVALID STRING', 'INVALID STRING')

    assert err == '1 or more invalid parameter type(s).'
    assert res is None


def test_invalid_type_num_players():
    # Num players cannot be cast to ints
    err, res = val.validate_route_inputs(2020, 2025, num_players='INVALID STRING')
    
    assert err == '1 or more invalid parameter type(s).'
    assert res == None

def test_num_players_oob():
    # Num players out of bounds
    err, res = val.validate_route_inputs(2020, 2025, num_players=10)

    assert err == 'Player number filter out of bounds.'
    assert res is None

def test_xpac_factions():
    # Expansion faction search for 2013.
    err, res = val.validate_route_inputs(2013, 2013, faction='yetis')

    assert err == 'Invalid search including expansion factions for 2013. Expansion factions released in 2014.'
    assert res is None

def test_year_oob():
    # Year out of bounds. Data starts at 2013
    err, res = val.validate_route_inputs(2011, 2025)

    assert err == 'Year parameter out of bounds.'
    assert res is None

def test_startyear_greater():
    # Start year greater than end year
    err, res = val.validate_route_inputs(2023, 2015)

    assert err == 'Invalid year filter dates. Start year greater than end year.'
    assert res is None

def test_happy_path():
    # All valid inputs, okay recieved.
    err, res = val.validate_route_inputs(2015, 2020, map='126fe960806d587c78546b30f1a90853b1ada468', num_players=3, faction='dwarves')
    assert err is None
    assert res == [2015, 2020, '126fe960806d587c78546b30f1a90853b1ada468', 3, 'dwarves']
