select
    resultId as result_id,
    raceId as race_id,
    driverId as driver_id,
    constructorId as constructor_id,
    number as car_number,
    cast(grid as int64) as grid_position,
    position,
    positionText as position_text,
    cast(positionOrder as int64) as position_order,
    cast(points as float64) as points,
    laps as num_laps,
    time,
    milliseconds,
    fastestLap as fastest_lap_number,
    fastestLapTime as fastest_lap_time,
    statusId as status_id
from {{ source('f1_raw', 'sprint_results') }}