select
    qualifyId as qualify_id,
    raceId as race_id,
    driverId as driver_id,
    constructorId as constructor_id,
    number as car_number,
    position as final_position,
    q1 as q1_time,
    q2 as q2_time,
    q3 as q3_time
from {{ source('f1_raw_csv', 'qualifying') }}