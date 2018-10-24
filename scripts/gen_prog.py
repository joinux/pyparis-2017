#!/usr/bin/env python

from __future__ import print_function, unicode_literals

from csv import reader

import pandas

# for line in reader(open("data/accepted.csv")):
#     print(line)

df = pandas.read_csv("data/accepted.csv", encoding="utf8")

# print(df)

tutorials = []

emails = set()

last_track = ""
for i in range(0, len(df)):
    r = df.iloc[i]
    title = r['title_en']
    track = r['track']
    duration = r['wanted_duration']
    speaker = r['speaker_first_name'] + ' ' + r['speaker_last_name']
    affiliation = r['speaker_affiliation']
    email = r['owner']
    emails.add(email)

    if int(duration) == 90:
        tutorials.append(f"- {title} ({speaker}, {affiliation})")
        continue

    if last_track != track:
        print()
        print(f"## Theme: {track}")
        print()
        last_track = track

    print(f"- {title} ({speaker}, {affiliation})")

print("\n## Tutorials\n")
for tut in tutorials:
    print(tut)


print(78 * "=")
for email in emails:
    print(email)
