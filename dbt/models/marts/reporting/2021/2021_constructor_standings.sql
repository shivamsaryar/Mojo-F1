with c as (
    select * 
    from {{ ref('stg__constructors') }}
),

cr as (
    select *
    from {{ ref('stg__constructor_results') }}
),

r as (
    select * from {{ ref('stg__races') }}
)

select 
    r.year,
    c.name,
    c.nationality,
    sum(cr.points) as season_points
from c left join cr on c.constructor_id = cr.constructor_id
left join r on cr.race_id = r.race_id
where year = 2021
group by 1,2,3
order by 4 desc