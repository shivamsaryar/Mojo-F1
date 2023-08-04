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
    bigquery.SchemaField("circuitId", "string"),
    bigquery.SchemaField("circuitRef", "string"),
    bigquery.SchemaField("name", "string"),
    bigquery.SchemaField("location", "string"),
    bigquery.SchemaField("country", "string"),
    bigquery.SchemaField("lat", "string"),
    bigquery.SchemaField("lng", "string"),
    bigquery.SchemaField("alt", "string"),
    bigquery.SchemaField("url", "string") 
]

# Table schema for 'constructor_results'
colSchema_constructor_results = [
    bigquery.SchemaField("constructorResultsId", "string"),
    bigquery.SchemaField("raceId", "string"),
    bigquery.SchemaField("constructorId", "string"),
    bigquery.SchemaField("points", "string"),
    bigquery.SchemaField("status", "string")
]

# Table schema for 'constructor_standings'
colSchema_contructor_standings = [
    bigquery.SchemaField("constructorStandingsId", "string"),
    bigquery.SchemaField("raceId", "string"),
    bigquery.SchemaField("constructorId", "string"),
    bigquery.SchemaField("points", "string"),
    bigquery.SchemaField("position", "string"),
    bigquery.SchemaField("positionText", "string"),
    bigquery.SchemaField("wins", "string")
]

# Table schema for 'constructors'
colSchema_constructors = [
    bigquery.SchemaField("constructorId", "string"),
    bigquery.SchemaField("constructorRef", "string"),
    bigquery.SchemaField("name", "string"),
    bigquery.SchemaField("nationality", "string"),
    bigquery.SchemaField("url", "string")
]

# Table schema for 'driver_standings'
colSchema_driver_standings = [
    bigquery.SchemaField("driverStandingsId","string"),
    bigquery.SchemaField("raceId","string"),
    bigquery.SchemaField("driverId","string"),
    bigquery.SchemaField("points","string"),
    bigquery.SchemaField("position","string"),
    bigquery.SchemaField("positionText","string"),
    bigquery.SchemaField("wins","string")
]

# Table schema for 'drivers'
colSchema_drivers = [
    bigquery.SchemaField("driverId","string"),
    bigquery.SchemaField("driverRef","string"),
    bigquery.SchemaField("number","string"),
    bigquery.SchemaField("code","string"),
    bigquery.SchemaField("forename","string"),
    bigquery.SchemaField("surname","string"),
    bigquery.SchemaField("dob","string"),
    bigquery.SchemaField("nationality","string"),
    bigquery.SchemaField("url","string")
]

# Table schema for 'lap_times'
colSchema_lap_times = [
    bigquery.SchemaField("raceId","string"),
    bigquery.SchemaField("driverId","string"),
    bigquery.SchemaField("lap","string"),
    bigquery.SchemaField("position","string"),
    bigquery.SchemaField("time","string"),
    bigquery.SchemaField("milliseconds","string")
]

# Table schema for 'pit_stops'
colSchema_pit_stops = [
    bigquery.SchemaField("raceId","string"),
    bigquery.SchemaField("driverId","string"),
    bigquery.SchemaField("stop","string"),
    bigquery.SchemaField("lap","string"),
    bigquery.SchemaField("time","string"),
    bigquery.SchemaField("duration","string"),
    bigquery.SchemaField("milliseconds","string")
]

# Table schema for 'qualifying'
colSchema_qualifying = [
    bigquery.SchemaField("qualifyId","string"),
    bigquery.SchemaField("raceId","string"),
    bigquery.SchemaField("driverId","string"),
    bigquery.SchemaField("constructorId","string"),
    bigquery.SchemaField("number","string"),
    bigquery.SchemaField("position","string"),
    bigquery.SchemaField("q1","string"),
    bigquery.SchemaField("q2","string"),
    bigquery.SchemaField("q3","string")
]

# Table schema for 'races'
colSchema_races = [
    bigquery.SchemaField("raceId","string"),
    bigquery.SchemaField("year","string"),
    bigquery.SchemaField("round","string"),
    bigquery.SchemaField("circuitId","string"),
    bigquery.SchemaField("name","string"),
    bigquery.SchemaField("date","string"),
    bigquery.SchemaField("time","string"),
    bigquery.SchemaField("url","string"),
    bigquery.SchemaField("fp1_date","string"),
    bigquery.SchemaField("fp1_time","string"),
    bigquery.SchemaField("fp2_date","string"),
    bigquery.SchemaField("fp2_time","string"),
    bigquery.SchemaField("fp3_date","string"),
    bigquery.SchemaField("fp3_time","string"),
    bigquery.SchemaField("quali_date","string"),
    bigquery.SchemaField("quali_time","string"),
    bigquery.SchemaField("sprint_date","string"),
    bigquery.SchemaField("sprint_time","string")
]

# Table schema for 'results'
colSchema_results = [
    bigquery.SchemaField("resultId","string"),
    bigquery.SchemaField("raceId","string"),
    bigquery.SchemaField("driverId","string"),
    bigquery.SchemaField("constructorId","string"),
    bigquery.SchemaField("number","string"),
    bigquery.SchemaField("grid","string"),
    bigquery.SchemaField("position","string"),
    bigquery.SchemaField("positionText","string"),
    bigquery.SchemaField("positionOrder","string"),
    bigquery.SchemaField("points","string"),
    bigquery.SchemaField("laps","string"),
    bigquery.SchemaField("time","string"),
    bigquery.SchemaField("milliseconds","string"),
    bigquery.SchemaField("fastestLap","string"),
    bigquery.SchemaField("rank","string"),
    bigquery.SchemaField("fastestLapTime","string"),
    bigquery.SchemaField("fastestLapSpeed","string"),
    bigquery.SchemaField("statusId","string")
]

# Table schema for 'seasons'
colSchema_seasons = [
    bigquery.SchemaField("year","string"),
    bigquery.SchemaField("url","string")
]

# Table schema for 'sprint_results'
colSchema_sprint_results = [
    bigquery.SchemaField("resultId","string"),
    bigquery.SchemaField("raceId","string"),
    bigquery.SchemaField("driverId","string"),
    bigquery.SchemaField("constructorId","string"),
    bigquery.SchemaField("number","string"),
    bigquery.SchemaField("grid","string"),
    bigquery.SchemaField("position","string"),
    bigquery.SchemaField("positionText","string"),
    bigquery.SchemaField("positionOrder","string"),
    bigquery.SchemaField("points","string"),
    bigquery.SchemaField("laps","string"),
    bigquery.SchemaField("time","string"),
    bigquery.SchemaField("milliseconds","string"),
    bigquery.SchemaField("fastestLap","string"),
    bigquery.SchemaField("fastestLapTime","string"),
    bigquery.SchemaField("statusId","string")
]

# Table schema for 'status'
colSchema_status = [
    bigquery.SchemaField("statusId","string"),
    bigquery.SchemaField("status","string")
]