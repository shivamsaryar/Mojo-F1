select
    constructorStandingsId as constructor_standings_id,
    raceId as race_id,
    constructorId as constructor_id,
    points,
    position,
    positionText as position_text,
    wins
from
    {{ source('f1_raw_csv', 'constructor_standings') }}