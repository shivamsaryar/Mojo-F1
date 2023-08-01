select 
    raceId as race_id,
    driverId as driver_id,
    lap,
    position,
    time,
    milliseconds
from
    {{ source('f1_raw_csv', 'lap_times') }}