import asyncio
from pydantic import BaseModel , ValidationError
from models import MatchScore , Team , Stadium


async def processing_data(raw_data:dict):
    print("⏳ Async function started... processing data.")
    await asyncio.sleep(0.5)

    validateMatchData = MatchScore.model_validate(raw_data)
    return validateMatchData
    

async def fetch_live_matches():
    
    dummyData ={
    "match_id": "1",
    "home_team": {
      "name":"Brazil",
      "goals":4,
      "logo_url":"https://flagcdn.com/w80/br.png"
    },
    "away_team": {
      "name":"Argentina",
      "goals":3,
      "logo_url":"https://flagcdn.com/w80/ar.png"
    },
    "home_score": "0",
    "away_score": "0",
    "home_scorers": "null",
    "away_scorers": "null",
    "group": "A",
    "matchday": "1",
    "date_time": "06/11/2026 13:00",
    "persian_date": "1405-03-21 13:00",
    "stadium": {
      "name":"MetLife stadium",
      "city":"New York",
      "capacity":"80,000"
    },
    "finished": "FALSE",
    "time_elapsed": "notstarted",
    "type": "group"
    }
    
    try:
        live_score = await processing_data(dummyData)
        print("✅ Success! Data successfully mapped by Pydantic.")
        print(f"Match ID: {live_score.match_id} (Type: {type(live_score.match_id)})")
        print(f"Home team: {live_score.home_team.name}")
        print(f"Away team: {live_score.away_team.name}")
    except ValidationError as e:
        print(f"❌ Pydantic Validation failed:\n{e}")

if __name__ =="__main__":
    asyncio.run(fetch_live_matches())