import hashlib
import json
from dataclasses import dataclass
from pathlib import Path

import requests


DIR = Path(__file__).parent
SESSION = requests.Session()
BASE_URL = "https://assets.minecraft.net"


@dataclass
class Download:
    sha1: str
    size: int
    url: str


def get_download(download_id: str, filename: str) -> Download | None:
    url = f"{BASE_URL}/{download_id}/{filename}"
    print(f"head {url}")
    r = SESSION.head(url)
    if r.ok:
        print(f" get {url}")
        r = SESSION.get(url)
        return Download(
            sha1=hashlib.sha1(r.content).hexdigest(),
            size=len(r.content),
            url=url,
        )


if __name__ == "__main__":
    json_files = sorted(Path(DIR / "json-2-cleanup").glob("*.json"))
    i_max = len(json_files)
    for i, json_file in enumerate(json_files, start=1):
        version_json = json.load(json_file.open())
        version_id: str = version_json["id"]

        if i != 1:
            print()
        print(f"{i:02}/{i_max} {version_id}")

        download_id = version_id
        if download_id.startswith("b"):
            download_id = download_id[1:]
        download_id = download_id.replace("1.", "1_")
        download_id = download_id.replace("~", "_")
        download_id = download_id.replace("-pre1", "-pre")

        version_json["downloads"] = dict()

        found_client = False
        for client_filename in ["minecraft.jar", "minecraft.zip"]:
            download = get_download(download_id, client_filename)
            if download:
                found_client = True
                version_json["downloads"]["client"] = download.__dict__

        if not found_client:
            raise Exception(f"failed to find client for {version_id=} {download_id=}")

        download = get_download(download_id, "minecraft_server.jar")
        if download:
            version_json["downloads"]["server"] = download.__dict__

        download = get_download(download_id, "Minecraft_Server.exe")
        if download:
            version_json["downloads"]["windows_server"] = download.__dict__

        json_file_out = Path(DIR / "json-3-urls" / json_file.name)
        json_file_out.write_text(json.dumps(version_json, indent=2))

    print("done")
