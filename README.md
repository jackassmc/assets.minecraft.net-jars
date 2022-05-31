# assets.minecraft.net jars

This repo contains version.json files for versions that are not in the launcher but are available from assets.minecraft.net.

- [json-1-import](./json-1-import) contains a copy of https://archive.org/details/Minecraft-JSONs, thanks Nixinova!
- [json-2-cleanup](./json-2-cleanup) contains a cleaned up version of the original import:
  - Non JSON files deleted
  - `c0.0.15a-1` deleted (Omniarchive only jar)
  - `b1.8-pre1-2` deleted (Omniarchive only jar)
  - `b1.8-pre1-1` renamed to `b1.8-pre1`
- [json-3-urls](./json-3-urls) contains the cleand up JSON files with URLs for:
  - client
    - minecraft.jar
    - minecraft.zip
  - server
    - minecraft_server.jar
  - windows_server
    - Minecraft_Server.exe
- [json-4-final](./json-4-final) contains the JSON files with some final touches:
  - Dates converted to datetimes
  - Added legacy-jre javaVersion
