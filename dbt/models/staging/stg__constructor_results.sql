select
    constructorResultsId as constructor_results_id,
    raceId as race_id,
    constructorId as constructor_id,
    points,
    status
from 
    {{ source('f1_raw_csv', 'constructor_results') }}