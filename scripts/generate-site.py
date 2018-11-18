#!/usr/bin/env python
# coding=utf-8

import pickle
from textwrap import dedent
import hashlib

records = pickle.load(open("talks.pickle", "rb"))
records.sort(key=lambda x: x['fields']['title_en'])
themes = [
    "Keynote",
    "Core Python",
    "Data Science",
    "Tools",
    "Web & Cloud",
    "Devops",
    "Education",
    "Tutorials"
]


def md5hex(s):
    h = hashlib.md5()
    h.update(s.encode('utf8'))
    return h.hexdigest()


def speaker_names(d):
    speaker = d['speaker_first_name'] + ' ' + d['speaker_last_name']
    if 'speaker2_first_name' not in d:
        return f"{speaker}"

    speaker2 = d['speaker2_first_name'] + ' ' + d['speaker2_last_name']

    return f"{speaker}+{speaker2}"


def speakers_info(d):
    speaker = d['speaker_first_name'] + ' ' + d['speaker_last_name']
    affiliation = d['speaker_affiliation']

    url = f"/speakers.html#{md5hex(speaker)}"

    if 'speaker2_first_name' not in d:
        return f"[{speaker}]({url}), {affiliation}"

    speaker2 = d['speaker2_first_name'] + ' ' + d['speaker2_last_name']
    affiliation2 = d.get('speaker2_affiliation', "")
    url2 = f"/speakers.html#{md5hex(speaker2)}"

    return f"[{speaker}]({url}), {affiliation} &amp; [{speaker2}]({url2}), {affiliation2}"


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

    # Talks
    
    Slides or presentation material for the talks are currently being collected and are
    published as soon as we get them.
    
    Half of the videos are already available, the next batch is expected on Nov. 19th.

    """).strip())

    for theme in themes:
        fd.write(f"\n### {theme}\n\n")

        if theme == 'Education':
            fd.write(f"\nNOTE: Les présentations du track 'Education' ont lieu **en français**.\n\n")

        for i in range(0, len(records)):
            r = records[i]['fields']
            duration = r['wanted_duration']
            if int(duration) == 90:
                talk_track = 'Tutorials'
            else:
                talk_track = r['track']
            if talk_track != theme:
                continue

            title = r['title_en']

            fd.write(f"\n- *{title}*<br>\n")
            fd.write(f"  By: {speakers_info(r)}<br>\n")

            if 'Slides' in r:
                fd.write(f"  Slides: ")
                decks = r['Slides']
                for i, deck in enumerate(decks):
                    hash = md5hex(speaker_names(r) + deck['id'] + str(i))[0:8]
                    filename = f"{speaker_names(r)}-{hash}.pdf"
                    url = f"/static/slides/{filename}"
                    fd.write(f"[{filename}]({url}) ")
                fd.write("<br>\n")
            if "URL" in r:
                fd.write(f"  Slides / presentation material (online): [{r['URL']}]({r['URL']})\n")
            if "Video" in r:
                fd.write(f"  Video: [here]({r['Video']})\n")

            fd.write("\n")


def gen_talk_details():
    fd = open("contents/talk-details.md", "wt")
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

    # Talks details

    """).strip())

    for theme in themes:
        fd.write(f"\n### {theme}\n\n")

        if theme == 'Education':
            fd.write(f"\nNOTE: Les présentations du track 'Education' ont lieu **en français**.\n\n")

        for i in range(0, len(records)):
            r = records[i]['fields']
            duration = r['wanted_duration']
            if int(duration) == 90:
                talk_track = 'Tutorials'
            else:
                talk_track = r['track']
            if talk_track != theme:
                continue

            title = r['title_en']

            fd.write(f"\n#### {title}\n")
            fd.write(f"\n**By**: {speakers_info(r)}\n\n")
            if 'abstract_en' in r:
                fd.write(f"\n**Abstract**: {r['abstract_en']}\n")

            if 'Slides' in r:
                fd.write(f"\n**Slides (PDF)**: ")
                for i, deck in enumerate(r['Slides']):
                    hash = md5hex(speaker_names(r) + str(i))[0:8]
                    filename = f"{speaker_names(r)}-{hash}.pdf"
                    url = f"/static/slides/{filename}"
                    fd.write(f"[{filename}]({url}) ")
                fd.write("\n")

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

    for i in range(0, len(records)):
        d = records[i]['fields']
        speakers.append(
            {
                'name': d['speaker_first_name'] + " " + d['speaker_last_name'],
                'last_name': d['speaker_last_name'],
                'affiliation': d['speaker_affiliation'],
                'job_title': d['speaker_title'],
                'bio': d['speaker_bio'],
            }
        )

        if 'speaker2_first_name' not in d:
            continue

        speakers.append(
            {
                'name': d['speaker2_first_name'] + " " + d['speaker2_last_name'],
                'last_name': d['speaker2_last_name'],
                'affiliation': d.get('speaker2_affiliation', ""),
                'job_title': d.get('speaker2_title', ""),
                'bio': d.get('speaker2_bio', ""),
            }
        )

    speakers.sort(key=lambda x: x['last_name'])

    for speaker in speakers:
        fd.write(f"\n\n### <a name='{md5hex(speaker['name'])}'></a> {speaker['name']}\n")
        fd.write(f"\nJob title: {speaker['job_title']}, {speaker['affiliation']}\n")
        fd.write(f"\nBio: {speaker['bio']}\n\n")


gen_talks()
gen_talk_details()
gen_speakers()
