select 
    raceId as race_id,
    driverId as driver_id,
    cast(lap as int64) as lap_number,
    position as final_position,
    time,
    cast(milliseconds as int64) as milliseconds
from
    {{ source('f1_raw', 'lap_times') }}