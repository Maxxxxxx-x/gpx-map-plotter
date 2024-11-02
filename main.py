#!/usr/bin/python3


import os
import gpxpy
import argparse

import map


def parseGpx(gpxFilePath: str) -> tuple[str, list[float], list[float]]:
    print(f"Processing {gpxFilePath}...")
    lats = []
    lons = []
    trailId = os.path.basename(gpxFilePath).split(".")[0]
    with open(gpxFilePath, "r") as file:
        gpx = gpxpy.parse(file)
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    lats.append(point.latitude)
                    lons.append(point.longitude)

    return (trailId, lats, lons)


def main():
    parser = argparse.ArgumentParser(
        description="Map GPX data",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "gpx_folder_path",
        type=str,
        help="Path to the directory that contains the GPX files."
    )

    args = parser.parse_args()
    gpxsPath = args.gpx_folder_path
    if not os.path.exists(gpxsPath):
        print("Invalid path")
        return

    gpxData = []
    for filePath in os.listdir(gpxsPath):
        if not filePath.endswith(".gpx"):
            continue
        gpxData.append(parseGpx(os.path.join(gpxsPath, filePath)))
    map.generateMap(gpxData)
    return


if __name__ == "__main__":
    main()
