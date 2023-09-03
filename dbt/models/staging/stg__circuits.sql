select 
    circuitId as circuit_id,
    circuitRef as circuit_ref,
    cast(name as string) as name,
    location,
    country,
    lat as latitude,
    lng as longitude,
    alt as altitude,
    url
from
    {{ source('f1_raw', 'circuits') }}