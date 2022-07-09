#!/usr/bin/python3
import hashlib
import sys

def sha256_from_data(data):
    hash_sha256 = hashlib.sha256()
    hash_sha256.update(data)
    return hash_sha256.hexdigest()

contents = open('90-enable-all.lua', 'r', encoding='utf-8').read()

sha256sum = sha256_from_data(contents.encode('utf-8'))
expected_sha256sum = 'cb9f05eb3b4959b84e94a67867645130f2bc0aa761eb864d227890aea310ab74'

if sha256sum != expected_sha256sum:
    print('The script has to be updated for new changes in 90-enable-all.lua')
    print(f'File sha256sum: {sha256sum}')
    print(f'expected sha256sum: {expected_sha256sum}')
    sys.exit(1)

content_sections = contents.split('\n\n')

sections = ['enable-metadata',
            'default-access-policy',
            'load-devices',
            'track-user-choices-devices',
            'track-user-choices-streams',
            'link-nodes-by-roles',
            'suspend-idle-nodes']

if len(content_sections) != len(sections):
    print('The script has to be updated for new changes in 90-enable-all.lua')
    sys.exit(1)

for i, (content, sec) in enumerate(zip(content_sections, sections)):
    if sec == 'load-devices':
        lines = content.split('\n')
        open(f'90-{i}-1-enable-alsa.lua', 'w',
             encoding='utf-8').write(lines[1])
        open(f'90-{i}-2-enable-v4l2.lua', 'w',
             encoding='utf-8').write(lines[2])
        continue

    filename = f'90-{i}-{sec}.lua'
    open(filename, 'w', encoding='utf-8').write(content)
