select
    constructorResultsId as constructor_results_id,
    raceId as race_id,
    constructorId as constructor_id,
    cast(points as float64) as points
from 
    {{ source('f1_raw', 'constructor_results') }}