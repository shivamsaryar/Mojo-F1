select
    resultId as result_id,
    raceId as race_id,
    driverId as driver_id,
    constructorId as constructor_id,
    number as car_number,
    grid as grid_position,
    position,
    positionText as position_text,
    positionOrder as position_order,
    points,
    laps,
    time,
    milliseconds,
    fastestLap as fastest_lap_number,
    fastestLapTime as fastest_lap_time,
    statusId as status_id
from {{ source('f1_raw_csv', 'sprint_results') }}