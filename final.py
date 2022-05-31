import json
from pathlib import Path


DIR = Path(__file__).parent


if __name__ == "__main__":
    json_files = sorted(Path(DIR / "json-3-urls").glob("*.json"))
    i_max = len(json_files)
    for i, json_file in enumerate(json_files, start=1):
        version_json = json.load(json_file.open())
        version_id: str = version_json["id"]

        print(f"{i:02}/{i_max} {version_id}")

        for key in ["releaseTime", "time"]:
            if len(version_json[key]) == 10:
                version_json[key] += "T00:00:00+00:00"

        version_json["javaVersion"] = {
            "component": "jre-legacy",
            "majorVersion": 8,
        }

        json_file_out = Path(DIR / "json-4-final" / json_file.name)
        json_file_out.write_text(json.dumps(version_json, indent=2))

    print("done")
