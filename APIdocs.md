# API Reference

## Factions

**Parameters:**
- `faction` (string, required): Target faction  
- `s_year`, `e_year` (int, required): Start and end year range  
- `num_players` (int, optional)  

**Endpoints:**
- **`/faction-wr`**: Win rate of the specified faction within given filters.  
- **`/faction-pickrate`**: Pick rate of the specified faction within given filters.  
- **`/faction-wr-versus`**: Win rate of the faction against all other factions.  
- **`/faction-wr-maps`**: Win rate of the faction across different maps.  
- **`/faction-avg-vp`**: Average victory points (VP) earned by the faction.  
- **`/faction-avg-vp-per-round`**: Average VP earned per round.  
- **`/faction-games-played`**: Number of games played with the faction.  
- **`/faction-popularity-ot`**: Popularity of a faction over time.  
- **`/wr-by-playercount`**: Win rate of a faction broken down by number of players.  

---

## Maps

**Parameters:**
- `map_id` (string, required)  
- `s_year`, `e_year` (int, required)  

**Endpoints:**
- **`/games-per-map`**: Number of games played per map.  
- **`/avg-players-per-map`**: Average number of players per map.  
- **`/faction-pickrate`**: Pick rate of factions on a given map.  
- **`/faction-winrate`**: Win rates of factions on a given map.  
- **`/avg-vp-per-map`**: Average VP scored on a given map.  
- **`/performance-variation`**: Performance variance of factions on the given map.  

---

## Tiles

**Parameters:**
- `s_year`, `e_year` (int, required)  
- `map_id`, `num_players`, `faction` (optional)  

**Endpoints:**
- **`/score-tile-freq`**: Frequency of scoring tile orders.  
- **`/bonus-tile-pop`**: Popularity of bonus tiles across games.  
- **`/favor-tiles-by-faction`**: Frequency of favour tiles chosen by factions.  
- **`/town-tiles-by-faction`**: Frequency of town tiles chosen by factions.  
- **`/vp-gained-by-score-tile`**: VP gained from each scoring tile.  

---

## Trends

**Parameters:**
- `s_year`, `e_year` (int, required)  

**Endpoints:**
- **`/win-rate-ot`**: Faction win rates over time.  
- **`/pick-rate-ot`**: Faction pick rates over time.  
- **`/map-picks-ot`**: Map popularity over time.  
- **`/played-games-ot`**: Number of games played over time.  

---

## Predictions

**Parameters:**
- `num_players` (int, required)  
- `map_id` (string, required)  
- `bonus_tiles` (list, required)  
- `score_tiles` (list, required)  

**Endpoints:**
- **`/win_prediction`**: Ranked win probability predictions for each faction under the given setup.  
