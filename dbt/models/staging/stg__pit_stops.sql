select
    raceId as race_id,
    driverId as driver_id,
    stop,
    lap,
    time,
    duration,
    milliseconds
from {{ source('f1_raw_csv', 'pit_stops') }}