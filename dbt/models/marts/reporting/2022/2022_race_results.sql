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
)

select
    races.date,
    circuits.country as GRAND_PRIX,
    circuits.name as CIRCUIT,
    drivers.full_name as WINNER,
    constructors.name as TEAM,
    results.car_number as CAR_NUMBER,
    results.points as POINTS,
    results.num_laps LAPS,
    results.race_duration as TIME

from results
left join drivers on results.driver_id = drivers.driver_id
left join races on results.race_id = races.race_id
left join circuits on races.circuit_id = circuits.circuit_id
left join constructors on results.constructor_id = constructors.constructor_id

where results.final_position = '1' and races.year = 2022
order by date
