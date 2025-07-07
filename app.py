
from flask import Flask, request, jsonify
import duckdb
import pandas as pd
from page_computations.routes.general_routes import general_bp
from page_computations.routes.faction_routes import factions_bp

app = Flask(__name__)

app.register_blueprint(general_bp, url_prefix='/api')
app.register_blueprint(factions_bp, url_prefix='/api/factions')



if __name__ == "__main__":
    app.run(debug=True)
