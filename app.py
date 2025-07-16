
from flask import Flask
from page_computations.routes.faction_routes import factions_bp
from page_computations.routes.maps_routes import maps_bp
from page_computations.routes.tile_routes import tiles_bp
from page_computations.routes.trends_routes import trends_bp

app = Flask(__name__)

app.register_blueprint(factions_bp, url_prefix='/api/factions')
app.register_blueprint(maps_bp, url_prefix='/api/maps')
app.register_blueprint(tiles_bp, url_prefix='/api/tiles')
app.register_blueprint(trends_bp, url_prefix='/api/trends')




if __name__ == "__main__":
    app.run(debug=True)
