#!/usr/bin/env python3

import json
import hashlib

from pprint import pprint
from collections import defaultdict

lines = json.load(open("PyParis 2017 Submissions.json", 'rb'))
lines.sort(key=lambda x: x['name'])

by_tag = defaultdict(list)

for line in lines:
    for tag in line['tag_list']:
        by_tag[tag].append(line)

output = open('contents/talks.md', 'w')

def write_talks():

    output.write("""\
---
title: Talks details
author: sfermigier
template: text.html
---

<style>
blockquote p {
    font-style: italic;
    color: #555;
}
</style>

""")

    output.write(f"""
# All the talks and speakers at a glance

See also the [Detailed Schedule](/schedule.html).

""")

    write_track("track:core", "Core Python (Day 1 & 2)")
    write_track("track:web", "Web & Cloud (Day 1 & 2)")
    write_track("track:data1", "Data 1 - Integrating and shaping data (Day 1 only)")
    write_track("track:data2", "Data 2 - Learning, deep and wide (Day 1 only)")
    write_track("track:scikit-learn", "scikit-learn day (Day 2 only)")
    write_track("track:education", "Education (Day 2 only)")
    write_track("workshop", "Tutorials / Workshops (Day 2 only)")


    output.write("# Details of each talk\n\n")
    for line in lines:
        hash = hashlib.md5(line['title'].encode('utf8')).hexdigest()
        output.write("<a name='{}'></a>\n".format(hash))
        output.write(f"## {line['name']}: {line['title']}\n\n")

        output.write(f"**Abstract**:\n\n")
        output.write("<div class='talk-abstract'>\n")
        output.write(line['abstract'] + "\n")
        output.write("</div>\n\n")

        output.write(f"**Speaker**: {line['name']} ({line['organization']})\n\n")
        output.write(f"**Speaker bio**:\n\n")

        output.write("<div class='talk-bio'>\n")
        output.write(line['bio'] + "\n")
        output.write("</div>\n")

        output.write("\n\n")

def write_track(tag, title):
    if tag.startswith("track:"):
        tagg = tag[len("track:"):]
    else:
        tagg = tag
    print(tagg)
    output.write("<a name='{}'></a>\n\n".format(tagg))
    output.write("## {}\n\n".format(title))

    for line in by_tag[tag]:
        hash = hashlib.md5(line['title'].encode('utf8')).hexdigest()
        output.write("- <a href='#{}'>{}</a> ({})\n".format(
            hash, line['title'], line['name']))

    output.write("\n")


write_talks()
