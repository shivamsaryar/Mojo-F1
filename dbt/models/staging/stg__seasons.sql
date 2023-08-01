select
    year,
    url as wiki_url
from {{ source('f1_raw_csv', 'seasons') }}