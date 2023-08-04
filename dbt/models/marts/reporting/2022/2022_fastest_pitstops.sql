with pitstops as (
    select * from {{ ref('stg__pit_stops') }}
),

races as (
    select * from {{ ref('stg__races') }}
),

drivers as (
    select * from {{ ref('stg__drivers') }}
),

circuits as (
    select * from {{ ref('stg__circuits') }}
),

constructors as (
    select * from {{ ref('stg__constructors') }}
),

all_pitstops as (
    select
        races.year as year,
        races.name as grand_prix,
        races.round,
        drivers.full_name as driver,
        pitstops.milliseconds / 1000 as seconds,
        rank()
            over (partition by races.year, races.name order by pitstops.milliseconds)
            as stop_rank
    from pitstops
    left join races on pitstops.race_id = races.race_id
    left join drivers on pitstops.driver_id = drivers.driver_id
)

select * from all_pitstops
where stop_rank < 6 and year = 2022
order by year desc, round, grand_prix, stop_rank