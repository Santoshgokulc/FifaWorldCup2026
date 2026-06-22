from pydantic import BaseModel,ValidationError

#defining my blueprint 

#master data 
class Team(BaseModel):
    name:str
    goals:int
    logo_url:str | None=None

class Stadium(BaseModel):
    name:str
    city:str
    capacity:int

class Fixture(BaseModel):
    fixture_id:int
    home_team: Team
    away_team: Team
    date_time:str
    stadium:Stadium

class MatchScore(BaseModel):
    match_id:int
    status:str
    home_team:Team
    away_team:Team
    minute:int | None=None
    stadium:Stadium | None = None

class GroupStanding(BaseModel):
    group_name:str
    team:Team
    points:int
    goal_difference:int

if __name__ == "__main__":
    print("Testing the Stadium validation")

    try:
        bad_data = Stadium(name="Spotify Camp Nou", city="Barcelona",capacity="Eighty Thousand People")
    except ValidationError as e:
        print("\n🎉 Success! Pydantic blocked invalid data: ")
        print(e)