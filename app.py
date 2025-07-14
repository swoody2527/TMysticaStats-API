
from flask import Flask, request, jsonify
import duckdb
import pandas as pd
from page_computations.routes.faction_routes import factions_bp
from page_computations.routes.maps_routes import maps_bp

app = Flask(__name__)

app.register_blueprint(factions_bp, url_prefix='/api/factions')
app.register_blueprint(maps_bp, url_prefix='/api/maps')




if __name__ == "__main__":
    app.run(debug=True)
