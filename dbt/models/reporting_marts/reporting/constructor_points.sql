with constructors as (
    select * 
    from {{ ref('stg__constructors') }}
),

constructor_results as (
    select *
    from {{ ref('stg__constructor_results') }}
),

races as (
    select * from {{ ref('stg__races') }}
),

constructor_points as (
    select 
        constructors.constructor_id,
        constructors.constructor_ref,
        constructors.name,
        constructors.nationality,
        constructor_results.race_id,
        sum(constructor_results.points) as season_points,
        races.year
    from constructors 
    left join constructor_results on (constructor_id)
    left join races on race_id

)

select * from constructor_points limit 20