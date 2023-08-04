with drivers as (
    select * from {{ ref('stg__drivers') }}
),

qualifying as (
    select * from {{ ref('stg__qualifying') }}
),

races as (
    select * from {{ ref('stg__races') }}
),

constructors as (
    select * from {{ ref('stg__constructors') }}
),

combined as (
    select 
        races.year,
        races.name,
        races.round,
        drivers.full_name,
        constructors.name as team,
        qualifying.final_position,
        qualifying.q1_lap_time,
        qualifying.q2_lap_time,
        qualifying.q3_lap_time
    from
        qualifying 
            left join races on qualifying.race_id = races.race_id
            left join drivers on qualifying.driver_id = drivers.driver_id
            left join constructors on qualifying.constructor_id = constructors.constructor_id
    where qualifying.final_position = '1' and year = 2022
)

select * except (final_position) from combined order by round