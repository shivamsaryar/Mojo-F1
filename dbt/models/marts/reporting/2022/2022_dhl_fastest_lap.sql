with drivers as (
    select * from {{ ref('stg__drivers') }}
),

results as (
    select * from {{ ref('stg__results') }}
),

sprint_results as (
    select * from {{ ref('stg__sprint_results') }}
),

races as (
    select * from {{ ref('stg__races') }}
),

constructors as (
    select * from {{ ref('stg__constructors') }}
),

combined_results as (
    (select race_id,
    driver_id,
    constructor_id,
    sum(points) as points,
    fastest_lap_number,
    fastest_lap_time,
    status_id
    from results
    group by 1,2,3,5,6,7)

    union all

    (select race_id,
    driver_id,
    constructor_id,
    sum(points) as points,
    fastest_lap_number,
    fastest_lap_time,
    status_id
    from sprint_results
    group by 1,2,3,5,6,7)
),

combined_all as (
    select combined_results.*,
    races.name as grand_prix,
    races.year as year,
    races.round,
    drivers.full_name as driver,
    constructors.name as team,
    from combined_results
    left join races on combined_results.race_id = races.race_id
    left join drivers on combined_results.driver_id = drivers.driver_id
    left join constructors on combined_results.constructor_id = constructors.constructor_id
    where fastest_lap_number not like '%N%' and status_id = '1' and year = 2022
),

final as (
    select grand_prix,
    round,
    driver,
    team as car,
    fastest_lap_time,
    row_number() over (partition by grand_prix order by fastest_lap_time) as row_number
    from combined_all
    where true qualify row_number = 1
)

select * except (round, row_number)
from final
order by round