from datetime import datetime, timezone

import folium
import random

#     (trailId, lats, lons)


def generateMap(data: list[tuple[str, list[float], list[float]]]):
    map = folium.Map(
        location=[23.83462548786052, 121.01649906097934],
        zoom_start=7
    )
    failedCount = 0
    failedIds = []
    for trail in data:
        print(f"Adding {trail[0]} to map...")
        color = "%06x" % random.randint(0, 0xDDDDDD)

        if trail[1] is None or trail[2] is None:
            failedCount += 1
            failedIds.append(trail[0])
            continue

        folium.PolyLine(
            list(
                zip(trail[1], trail[2])
            ),
            color=f"#{color}",
            weight=2.5,
            opacity=1,
            popup=f"{trail[0]}"
        ).add_to(map)

        folium.Marker(
            [trail[1][0], trail[2][0]],
            popup=f"Start of trail {trail[0]}",
            icon=folium.Icon(color="green")
        ).add_to(map)

        folium.Marker(
            [trail[1][-1], trail[2][-1]],
            popup=f"End of trail {trail[0]}",
            icon=folium.Icon(color="red")
        ).add_to(map)

    print(f"Total number of trails: {len(data)}")
    print(f"Failed to process: {failedCount}")
    for id in failedIds:
        print(f"Failed to process {id}")
    print(f"Successfully processed: {len(data) - failedCount}")
    print("Saving map...")
    map.save(f"{datetime.now(timezone.utc).isoformat()}.html")
    return
