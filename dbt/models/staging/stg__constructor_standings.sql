select
    constructorStandingsId as constructor_standings_id,
    raceId as race_id,
    constructorId as constructor_id,
    cast(points as float64) as points,
    position as final_position,
    positionText as position_text,
    cast(wins as int64) as num_wins
from
    {{ source('f1_raw', 'constructor_standings') }}