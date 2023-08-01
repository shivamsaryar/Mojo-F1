select 
    constructorId as constructor_id,
    constructorRef as constructor_ref,
    name,
    nationality,
    url
from {{ source('f1_raw_csv', 'constructors') }}