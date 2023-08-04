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
    sum(cr.points) as season_points
from c left join cr on c.constructor_id = cr.constructor_id
left join r on cr.race_id = r.race_id
where year = 2022
group by 2,1
order by 3 desc