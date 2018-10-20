from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np
import pandas as pd

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func , inspect, and_
from flask import Flask, jsonify
engine = create_engine("sqlite:///hawaii.sqlite")
 # reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
 # We can view all of the classes that automap found
Base.classes.keys()
 # Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
 # Create our session (link) from Python to the DB
session = Session(engine)
app = Flask(__name__)

@app.route("/api/v1.0/precipitation")
def list_precipitation():
    # Calculate the date 1 year ago from today
    year_ago = dt.date.today() - dt.timedelta(days=365)
    # Perform a query to retrieve the data and precipitation scores
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year_ago).all()
    dic = {}
    for d, p in results:
        dic[d] = p
    print(dic)
    return jsonify(dic)

@app.route("/api/v1.0/stations")
def list_stations():
    stations = session.query(Station.station).group_by(Station.station).all()
    print(stations)
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def list_tobs():
    year_ago = dt.date.today() - dt.timedelta(days=365)
    temperature = session.query(Measurement.tobs).\
    filter(and_(Measurement.station == 'USC00519281', Measurement.date >= year_ago)).all()
    return jsonify(temperature)

@app.route("/api/v1.0/<start>")
def start_date(start):
    print(start)
    result = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
           .filter(Measurement.date >= start).first()
    print(result)
    return jsonify(result)

@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start,end):
    print(start)
    print(end)
    start_end = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
           .filter(and_(Measurement.date >= start,Measurement.date <= end)).all()
    print(start_end)
    return jsonify(start_end)

if __name__ == "__main__":
    app.run()