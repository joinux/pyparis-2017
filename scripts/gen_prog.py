#!/usr/bin/env python

from __future__ import print_function, unicode_literals

from textwrap import dedent

import pandas
from numpy import nan

df = pandas.read_excel("data/accepted-final.xlsx")
themes = [
    "Core Python",
    "Data Science",
    "Tools",
    "Web & Cloud",
    "Devops",
    "Education",
    "Tutorials"
]


def speakers_info(d):
    d = d.to_dict()
    speaker = d['speaker_first_name'] + ' ' + d['speaker_last_name']
    affiliation = d['speaker_affiliation']

    if d['speaker2_first_name'] is nan:
        return f"({speaker}, {affiliation})"

    speaker2 = d['speaker2_first_name'] + ' ' + d['speaker2_last_name']
    affiliation2 = d['speaker2_affiliation']

    return f"({speaker}, {affiliation} &amp; {speaker2}, {affiliation2})"


def gen_talks():
    fd = open("contents/talks.md", "wt")
    fd.write(dedent("""
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
    h3, h4 {
        margin-top: 30px;
    }
    </style>

    # Talk details

    [The detailed schedule](/static/pdf/Schedule-PyParis-2018.pdf) is available as a PDF file.
    """).strip())
    fd.write("\n\n## At a glance\n\n")

    for theme in themes:
        fd.write(f"\n### Theme: {theme}\n\n")

        if theme == 'Education':
            fd.write(f"\nNOTE: Les présentations du track 'Education' ont lieu **en français**.\n\n")

        for i in range(0, len(df)):
            r = df.iloc[i]
            duration = r['wanted_duration']
            if int(duration) == 90:
                talk_track = 'Tutorials'
            else:
                talk_track = r['track']
            if talk_track != theme:
                continue

            title = r['title_en']

            fd.write(f"- {title} {speakers_info(r)}\n")

    fd.write("\n----\n\n## Talk / Tutorials details\n")
    for theme in themes:
        fd.write(f"\n### Theme: {theme}\n\n")

        if theme == 'Education':
            fd.write(f"\nNOTE: Les présentations du track 'Education' ont lieu **en français**.\n\n")

        for i in range(0, len(df)):
            r = df.iloc[i]
            duration = r['wanted_duration']
            if int(duration) == 90:
                talk_track = 'Tutorials'
            else:
                talk_track = r['track']
            if talk_track != theme:
                continue

            title = r['title_en']

            fd.write(f"\n#### {title} {speakers_info(r)}\n\n")
            fd.write(r['abstract_en'])
            fd.write("\n")


def gen_speakers():
    fd = open("contents/speakers.md", "wt")
    fd.write(dedent("""
    ---
    title: Speakers
    author: sfermigier
    template: text.html
    ---
    
    <style>
    blockquote p {
        font-style: italic;
        color: #555;
    }
    h3, h4 {
        margin-top: 30px;
    }
    </style>
    """).strip())
    fd.write("\n\n## Speakers\n\n")

    speakers = []

    for i in range(0, len(df)):
        r = df.iloc[i]
        d = r.to_dict()
        speakers.append(
            {
                'name': d['speaker_first_name'] + " " + d['speaker_last_name'],
                'last_name': d['speaker_last_name'],
                'affiliation': d['speaker_affiliation'],
                'job_title': d['speaker_title'],
                'bio': d['speaker_bio'],
            }
        )

        if d['speaker2_first_name'] is nan:
            continue

        speakers.append(
            {
                'name': d['speaker2_first_name'] + " " + d['speaker2_last_name'],
                'last_name': d['speaker2_last_name'],
                'affiliation': d['speaker2_affiliation'],
                'job_title': d['speaker2_title'],
                'bio': d['speaker2_bio'],
            }
        )

    speakers.sort(key=lambda x: x['last_name'])

    for speaker in speakers:
        fd.write(f"\n\n### {speaker['name']} ({speaker['job_title']}, {speaker['affiliation']})\n")
        fd.write(f"\n{speaker['bio']}\n\n")


gen_talks()
gen_speakers()
