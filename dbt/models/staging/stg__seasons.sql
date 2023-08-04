select
    cast(year as int64) as year,
    url
from {{ source('f1_raw', 'seasons') }}