Notes:

- Zoho has API, but let's not go that way (need to request access, not a very open api it seems)
- need persistent storage, json or sqlite?
- sqlite with ORM is definitely easier with filtering
- how to do the screenshot from ANWB? append it to a preset? Probably a lot of effort, but is nice to accomplish.
- actually not that difficult if stored as a blob: https://stackoverflow.com/questions/58365883/saving-images-into-sqlite-database
- pass it as arg, and then always generate a folder with images to attach to report.


Preset has the following fields:
Title, distance (future, from/to, and calc distance?)


A trip has the following fields:
title, date, preset, return_trip (uses preset x2), id (for deletion)

zoho add-trip prompts:
title:
date:
preset:
return?


queries I can think of are:
zoho dump-month-report (--month --year optional, assume from current date)

zoho show trips --start-date yyyy-mm-dd --end-date yyyy-mm-dd

zoho set-km-rate-cents 23 (to set it to 2024 tax year)

zoho add-preset home-work 29.8 (note it can be a float)



