from google.cloud import bigquery

def getSchema(table_name):

    if table_name == 'circuits':
        return colSchema_circuits
    if table_name == 'constructor_results':
        return colSchema_constructor_results
    if table_name == 'constructor_standings':
        return colSchema_contructor_standings
    if table_name == 'constructors':
        return colSchema_constructors
    if table_name == 'driver_standings':
        return colSchema_driver_standings
    if table_name == 'drivers':
        return colSchema_drivers
    if table_name == 'lap_times':
        return colSchema_lap_times
    if table_name == 'pit_stops':
        return colSchema_pit_stops
    if table_name == 'qualifying':
        return colSchema_qualifying
    if table_name == 'races':
        return colSchema_races
    if table_name == 'results':
        return colSchema_results
    if table_name == 'seasons':
        return colSchema_seasons
    if table_name == 'sprint_results':
        return colSchema_sprint_results
    if table_name == 'status':
        return colSchema_status

# Table schema for 'circuits'
colSchema_circuits = [
    bigquery.SchemaField("circuitId", "STRING"),
    bigquery.SchemaField("circuitRef", "STRING"),
    bigquery.SchemaField("name", "STRING"),
    bigquery.SchemaField("location", "STRING"),
    bigquery.SchemaField("country", "STRING"),
    bigquery.SchemaField("lat", "STRING"),
    bigquery.SchemaField("lng", "STRING"),
    bigquery.SchemaField("alt", "STRING"),
    bigquery.SchemaField("url", "STRING") 
]

# Table schema for 'constructor_results'
colSchema_constructor_results = [
    bigquery.SchemaField("constructorResultsId", "STRING"),
    bigquery.SchemaField("raceId", "STRING"),
    bigquery.SchemaField("constructorId", "STRING"),
    bigquery.SchemaField("points", "STRING"),
    bigquery.SchemaField("status", "STRING")
]

# Table schema for 'constructor_standings'
colSchema_contructor_standings = [
    bigquery.SchemaField("constructorStandingsId", "STRING"),
    bigquery.SchemaField("raceId", "STRING"),
    bigquery.SchemaField("constructorId", "STRING"),
    bigquery.SchemaField("points", "STRING"),
    bigquery.SchemaField("position", "STRING"),
    bigquery.SchemaField("positionText", "STRING"),
    bigquery.SchemaField("wins", "STRING")
]

# Table schema for 'constructors'
colSchema_constructors = [
    bigquery.SchemaField("constructorId", "STRING"),
    bigquery.SchemaField("constructorRef", "STRING"),
    bigquery.SchemaField("name", "STRING"),
    bigquery.SchemaField("nationality", "STRING"),
    bigquery.SchemaField("url", "STRING")
]

# Table schema for 'driver_standings'
colSchema_driver_standings = [
    bigquery.SchemaField("driverStandingsId","STRING"),
    bigquery.SchemaField("raceId","STRING"),
    bigquery.SchemaField("driverId","STRING"),
    bigquery.SchemaField("points","STRING"),
    bigquery.SchemaField("position","STRING"),
    bigquery.SchemaField("positionText","STRING"),
    bigquery.SchemaField("wins","STRING")
]

# Table schema for 'drivers'
colSchema_drivers = [
    bigquery.SchemaField("driverId","STRING"),
    bigquery.SchemaField("driverRef","STRING"),
    bigquery.SchemaField("number","STRING"),
    bigquery.SchemaField("code","STRING"),
    bigquery.SchemaField("forename","STRING"),
    bigquery.SchemaField("surname","STRING"),
    bigquery.SchemaField("dob","STRING"),
    bigquery.SchemaField("nationality","STRING"),
    bigquery.SchemaField("url","STRING")
]

# Table schema for 'lap_times'
colSchema_lap_times = [
    bigquery.SchemaField("raceId","STRING"),
    bigquery.SchemaField("driverId","STRING"),
    bigquery.SchemaField("lap","STRING"),
    bigquery.SchemaField("position","STRING"),
    bigquery.SchemaField("time","STRING"),
    bigquery.SchemaField("milliseconds","STRING")
]

# Table schema for 'pit_stops'
colSchema_pit_stops = [
    bigquery.SchemaField("raceId","STRING"),
    bigquery.SchemaField("driverId","STRING"),
    bigquery.SchemaField("stop","STRING"),
    bigquery.SchemaField("lap","STRING"),
    bigquery.SchemaField("time","STRING"),
    bigquery.SchemaField("duration","STRING"),
    bigquery.SchemaField("milliseconds","STRING")
]

# Table schema for 'qualifying'
colSchema_qualifying = [
    bigquery.SchemaField("qualifyId","STRING"),
    bigquery.SchemaField("raceId","STRING"),
    bigquery.SchemaField("driverId","STRING"),
    bigquery.SchemaField("constructorId","STRING"),
    bigquery.SchemaField("number","STRING"),
    bigquery.SchemaField("position","STRING"),
    bigquery.SchemaField("q1","STRING"),
    bigquery.SchemaField("q2","STRING"),
    bigquery.SchemaField("q3","STRING")
]

# Table schema for 'races'
colSchema_races = [
    bigquery.SchemaField("raceId","STRING"),
    bigquery.SchemaField("year","STRING"),
    bigquery.SchemaField("round","STRING"),
    bigquery.SchemaField("circuitId","STRING"),
    bigquery.SchemaField("name","STRING"),
    bigquery.SchemaField("date","STRING"),
    bigquery.SchemaField("time","STRING"),
    bigquery.SchemaField("url","STRING"),
    bigquery.SchemaField("fp1_date","STRING"),
    bigquery.SchemaField("fp1_time","STRING"),
    bigquery.SchemaField("fp2_date","STRING"),
    bigquery.SchemaField("fp2_time","STRING"),
    bigquery.SchemaField("fp3_date","STRING"),
    bigquery.SchemaField("fp3_time","STRING"),
    bigquery.SchemaField("quali_date","STRING"),
    bigquery.SchemaField("quali_time","STRING"),
    bigquery.SchemaField("sprint_date","STRING"),
    bigquery.SchemaField("sprint_time","STRING")
]

# Table schema for 'results'
colSchema_results = [
    bigquery.SchemaField("resultId","STRING"),
    bigquery.SchemaField("raceId","STRING"),
    bigquery.SchemaField("driverId","STRING"),
    bigquery.SchemaField("constructorId","STRING"),
    bigquery.SchemaField("number","STRING"),
    bigquery.SchemaField("grid","STRING"),
    bigquery.SchemaField("position","STRING"),
    bigquery.SchemaField("positionText","STRING"),
    bigquery.SchemaField("positionOrder","STRING"),
    bigquery.SchemaField("points","STRING"),
    bigquery.SchemaField("laps","STRING"),
    bigquery.SchemaField("time","STRING"),
    bigquery.SchemaField("milliseconds","STRING"),
    bigquery.SchemaField("fastestLap","STRING"),
    bigquery.SchemaField("rank","STRING"),
    bigquery.SchemaField("fastestLapTime","STRING"),
    bigquery.SchemaField("fastestLapSpeed","STRING"),
    bigquery.SchemaField("statusId","STRING")
]

# Table schema for 'seasons'
colSchema_seasons = [
    bigquery.SchemaField("year","STRING"),
    bigquery.SchemaField("url","STRING")
]

# Table schema for 'sprint_results'
colSchema_sprint_results = [
    bigquery.SchemaField("resultId","STRING"),
    bigquery.SchemaField("raceId","STRING"),
    bigquery.SchemaField("driverId","STRING"),
    bigquery.SchemaField("constructorId","STRING"),
    bigquery.SchemaField("number","STRING"),
    bigquery.SchemaField("grid","STRING"),
    bigquery.SchemaField("position","STRING"),
    bigquery.SchemaField("positionText","STRING"),
    bigquery.SchemaField("positionOrder","STRING"),
    bigquery.SchemaField("points","STRING"),
    bigquery.SchemaField("laps","STRING"),
    bigquery.SchemaField("time","STRING"),
    bigquery.SchemaField("milliseconds","STRING"),
    bigquery.SchemaField("fastestLap","STRING"),
    bigquery.SchemaField("fastestLapTime","STRING"),
    bigquery.SchemaField("statusId","STRING")
]

# Table schema for 'status'
colSchema_status = [
    bigquery.SchemaField("statusId","STRING"),
    bigquery.SchemaField("status","STRING")
]