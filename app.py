#add dependencies 
import datetime as dt
import numpy as np
import pandas as pd

#add SQLAlchemy dependencies

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#set up our database engine for the Flask application
engine = create_engine("sqlite:///hawaii.sqlite")

#reflect the database into our classes
Base = automap_base()

# reflect the database
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

#create a session list
session = Session(engine)

    #setup a Flask 
app = Flask(__name__)

#Define the welcome route
@app.route("/")

# add the routing information for each of the other routes
def welcome():
    return(
         '''
    Welcome to the Climate Analysis API! <br/>
    Available Routes: <br/>
    /api/v1.0/precipitation <br/>
    /api/v1.0/stations <br/>
    /api/v1.0/tobs <br/>
    /api/v1.0/temp/start/end 
    '''
    )

#create a precipitation route 
@app.route("/api/v1.0/precipitation")
#create percipitation function 
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)


#create a station route
@app.route("/api/v1.0/stations")

#create station function 
def station():
    #create a query that will allow us to get all of the stations in our database
    results = session.query(Station.station).all()
    #convert the results to a list
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

#create temperature observations route
@app.route("/api/v1.0/tobs")
#create a function
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


#create  report on the minimum, average, and maximum temperatures routes
#with start & end dates
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

#create a function 
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

print(Measurement)