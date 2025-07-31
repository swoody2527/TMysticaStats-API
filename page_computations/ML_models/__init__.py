# prediction_models/__init__.py
from pathlib import Path
import joblib
import json

MODEL_DIR = Path(__file__).resolve().parent

vp_faction_model = joblib.load(MODEL_DIR / 'vp_faction_model.joblib')
vp_no_faction_model = joblib.load(MODEL_DIR / 'vp_no_faction_model.joblib')

win_class_faction_model = joblib.load(MODEL_DIR / 'win_classifier_faction.joblib')
win_class_no_faction_model = joblib.load(MODEL_DIR / 'win_classifier_no_faction.joblib')


with (MODEL_DIR / 'avg_faction_vp.json').open() as f:
    vp_info = json.load(f)

with (MODEL_DIR / 'wr_on_map.json').open() as f:
    wr_info = json.load(f)