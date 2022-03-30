import fastf1
fastf1.Cache.enable_cache('F:\cache')
session = fastf1.get_session(2022, 1, "R")
session.load()
print(session.laps)