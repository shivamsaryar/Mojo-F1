select 
    driverStandingsId as driver_standings_id,
    raceId as race_id,
    driverId as driver_id,
    points,
    position,
    positionText as position_text,
    wins
from
    {{ source('f1_raw_csv', 'driver_standings') }}