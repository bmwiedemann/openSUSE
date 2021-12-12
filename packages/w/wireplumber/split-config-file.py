#!/usr/bin/python3
import hashlib
import sys


def md5FromData(data):
    hash_md5 = hashlib.md5()
    hash_md5.update(data)
    return hash_md5.hexdigest()


contents = open('90-enable-all.lua', 'r', encoding='utf-8').read()

md5sum = md5FromData(contents.encode('utf-8'))
expected_md5sum = '1317fb5df6ae842fda3ef845f195e084'

if md5sum != expected_md5sum:
    print('The script has to be updated for new changes in 90-enable-all.lua')
    print(f'File md5sum: {md5sum}')
    print(f'expected md5sum: {expected_md5sum}')
    sys.exit(1)

content_sections = contents.split('\n\n')

sections = ['enable-metadata',
            'default-access-policy',
            'load-devices',
            'track-user-choices',
            'link-nodes-by-roles',
            'suspend-idle-nodes',
            'device-activation']

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
