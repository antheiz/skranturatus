from flask import Flask, render_template, jsonify, request
import json
import mysql.connector
import geojson

app = Flask(__name__)

db_config = {
    "host": "mysql",
    "user": "admin",
    "password": "rahasia",
    "database": "web-gis",
}


def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn


def query_database(query):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()


# def get_provinces():
#     return query_database("SELECT id, nama, ST_AsGeoJSON(geo_data) FROM provinsi")


# def get_regencies(province_id=None):
#     base_query = "SELECT id, province_id, name, ST_AsGeoJSON(geo_data) FROM regencies"
#     if province_id:
#         base_query += f" WHERE province_id = {province_id}"
#     return query_database(base_query)


def get_districts():
    base_query = (
        "SELECT distrik_id, nama_distrik, ST_AsGeoJSON(peta_distrik) FROM distriks"
    )
    return query_database(base_query)


def get_villages(district_id=None):
    base_query = (
        "SELECT desa_id, distrik_id, nama_desa, ST_AsGeoJSON(peta_desa) FROM desas"
    )
    if district_id:
        base_query += f" WHERE distrik_id = {district_id}"
    return query_database(base_query)


def create_geojson(features):
    return geojson.FeatureCollection(features)


@app.route("/")
def regency_map():
    return render_template("regency_map.html")


# @app.route("/api/provinces")
# def provinces_api():
#     provinces = get_provinces()
#     features = [
#         geojson.Feature(geometry=json.loads(geom), properties={"id": id, "name": name})
#         for id, name, geom in provinces
#     ]
#     return jsonify(create_geojson(features))


# @app.route("/api/regencies")
# def regencies_api():
#     regencies = get_regencies()
#     features = [
#         geojson.Feature(geometry=json.loads(geom), properties={"id": id, "name": name})
#         for id, name, geom in regencies
#     ]
#     return jsonify(features)


@app.route("/api/districts")
def districts_api():
    districts = get_districts()
    features = [
        geojson.Feature(
            geometry=json.loads(geom),
            properties={"distrik_id": distrik_id, "name": name},
        )
        for distrik_id, name, geom in districts
    ]
    return jsonify(create_geojson(features))


@app.route("/api/villages")
def villages_api():
    district_id = request.args.get("districtId")
    print(district_id)
    villages = get_villages(district_id)
    features = [
        geojson.Feature(
            geometry=json.loads(geom),
            properties={"desa_id": desa_id, "distrik_id": distrik_id, "name": name},
        )
        for desa_id, distrik_id, name, geom in villages
    ]
    return jsonify(create_geojson(features))


if __name__ == "__main__":
    app.run(debug=True)
