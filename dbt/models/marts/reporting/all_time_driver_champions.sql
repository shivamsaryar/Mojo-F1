with drivers as (
    select * from {{ ref('stg__drivers') }}
),

constructors as (
    select * from {{ ref('stg__constructors') }}
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

cte_union as (
    (select
        race_id,
        driver_id,
        constructor_id,
        sum(points) as points
    from results
    group by 1, 2, 3)
    union all
    (select
        race_id,
        driver_id,
        constructor_id,
        sum(points) as points
    from sprint_results
    group by 1, 2, 3)
),

cte_combined as (
    select
        cte_union.*,
        races.year,
        drivers.full_name as driver_name,
        constructors.name as team
    from cte_union left join races on cte_union.race_id = races.race_id
    left join drivers on cte_union.driver_id = drivers.driver_id
    left join
        constructors
        on cte_union.constructor_id = constructors.constructor_id
),

final as (
    select
        year,
        driver_name,
        team,
        sum(points) as points
    from cte_combined
    group by 1, 2, 3
)

select
    *,
    rank() over (partition by year order by points desc) as season_rank
from final
where true qualify season_rank = 1
order by year desc
