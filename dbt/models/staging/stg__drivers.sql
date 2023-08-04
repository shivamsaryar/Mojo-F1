select
    driverId as driver_id,
    driverRef as driver_ref,
    number as driver_number,
    code as driver_code,
    forename as first_name,
    surname as last_name,
    concat(forename, ' ', surname) as full_name,
    cast(dob as date) as dob,
    nationality,
    url
from {{ source('f1_raw', 'drivers') }}