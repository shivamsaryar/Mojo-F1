select
    raceId as race_id,
    driverId as driver_id,
    cast(stop as int64) as pitstop_number,
    cast(lap as int64) as lap_number,
    time,
    duration,
    cast(milliseconds as int64) as milliseconds
from {{ source('f1_raw', 'pit_stops') }}