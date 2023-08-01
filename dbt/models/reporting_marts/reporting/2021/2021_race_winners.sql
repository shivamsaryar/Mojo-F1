with drivers as(
    select * from {{ ref('stg__drivers') }}
),

races as (
    select * from {{ ref('stg__races') }}
),

results as (
    select * from {{ ref('stg__results') }}
)

select 
    results.driver_id, 
    drivers.driver_ref,
    results.constructor_id,
    results.car_number,
    results.points,
    results.laps,
    results.race_duration
from results join drivers on results.driver_id = drivers.driver_id
join races on results.race_id = races.race_id
where results.final_position = 1 and races.year = '2021'