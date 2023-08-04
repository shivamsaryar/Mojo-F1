with c as (
    select * from {{ ref('stg__constructors') }}
),
cr as (
    select * from {{ ref('stg__constructor_results') }}
),

r as (
    select * from {{ ref('stg__races') }}
),

all_teams as (
    select 
        r.year as year,
        c.name as team,
        c.nationality,
        sum(cr.points) as points,
    from
        c left join cr on c.constructor_id = cr.constructor_id
        left join r on cr.race_id = r.race_id
    group by year, team, nationality
    order by 1 desc, 4 desc
),

winning_teams as (
    select 
        year, 
        team, 
        nationality,
        points,
        row_number() over (partition by year order by points desc) as row_number
    from all_teams
)
select * except(row_number) from winning_teams 
where row_number = 1
order by year desc, points desc 