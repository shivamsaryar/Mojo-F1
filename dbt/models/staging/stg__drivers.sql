select
    driverId as driver_id,
    driverRef as driver_ref,
    number as driver_number,
    code as driver_code,
    forename as first_name,
    surname as last_name,
    dob,
    nationality,
    url
from {{ source('f1_raw_csv', 'drivers') }}