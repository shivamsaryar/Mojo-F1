with drivers as (
    select * from {{ ref('stg__drivers') }}
),

races as (
    select * from {{ ref('stg__races') }}
),

results as (
    select * from {{ ref('stg__results') }}
),

circuits as (
    select * from {{ ref('stg__circuits') }}
),

constructors as (
    select * from {{ ref('stg__constructors') }}
),

sprint_results as (
    select * from {{ ref('stg__sprint_results') }}
),

combined_results as (
    (select race_id,
    driver_id,
    constructor_id,
    sum(points) as points
    from results
    group by 1,2,3)

    union all

    (select race_id,
    driver_id,
    constructor_id,
    sum(points) as points
    from sprint_results
    group by 1,2,3)
),

combined_all as (
    select
        races.date,
        circuits.country as grand_prix,
        circuits.name as circuit,
        drivers.full_name as driver,
        drivers.nationality as nationality,
        constructors.name as team,
        combined_results.points as points

    from combined_results
        left join drivers on combined_results.driver_id = drivers.driver_id
        left join races on combined_results.race_id = races.race_id
        left join circuits on races.circuit_id = circuits.circuit_id
        left join constructors on combined_results.constructor_id = constructors.constructor_id

    where races.year = 2022
    order by date
)

select 
    driver,
    nationality,
    team as car,
    sum(points) as points
from combined_all
group by 1,2,3
order by points desc