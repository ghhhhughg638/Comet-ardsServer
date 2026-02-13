from datetime import datetime, timezone


async def Timez_Create_Now():
    current_time = datetime.now(timezone.utc)
    server_time_z = current_time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    return server_time_z
