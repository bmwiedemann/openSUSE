#
# spec file for package mycroft-core
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           mycroft-core
Version:        18.8.13
Release:        0
Summary:        The Mycroft Artificial Intelligence platform
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
# FIXME: use correct group, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
License:        GPL-3.0-only
Group:          System/GUI/Other
Url:            https://mycroft.ai
Source:         https://github.com/MycroftAI/%{name}/archive/release/v%{version}.tar.gz
Source1:        version.json
Source2:        mycroft-bus.service
Source3:        mycroft-skills.service
Source4:        mycroft-audio.service
Source5:        mycroft-voice.service
Source6:        mycroft.target
Source7:        SKILL_README.md
Source8:        mycroft.conf
Source9:        mycroft-user-template.conf
Source10:       create-initial-user-configuration.sh
Source13:       skills-mycroft-youtube.patch
Source14:       skills-mycroft-music-skill.patch
Source15:       skills-skill-desktop-launcher.patch
Source16:       skills-mycroft-fallback-duck-duck-go.patch
Source17:       skills-skill-autogui.patch
Source18:       skills-mycroft-weather.patch
Patch1000:      fix-installation-paths.patch
Patch1001:      use-pycodestyle-instead-of-pep8.patch
Patch1004:      fix-skill-settings-hash.patch
BuildRequires:  fdupes
BuildRequires:  python3-setuptools
Requires:       mimic
Requires:       python3-Pillow
Requires:       python3-PyChromecast
Requires:       python3-PyRIC
Requires:       python3-PyYAML >= 3.13
Requires:       python3-SpeechRecognition >= 3.8.1
Requires:       python3-adapt-parser >= 0.3.0
Requires:       python3-fann2 >= 1.0.7
Requires:       python3-fasteners >= 0.14.1
Requires:       python3-gTTS >= 2.0.1
Requires:       python3-gTTS-token >= 1.1.3
Requires:       python3-gobject
Requires:       python3-google-api-python-client >= 1.6.4
Requires:       python3-inflection >= 0.3.1
Requires:       python3-monotonic
Requires:       python3-msk >= 0.3.12
Requires:       python3-msm >= 0.6.3
Requires:       python3-padaos >= 0.1.9
Requires:       python3-padatious >= 0.4.6
Requires:       python3-parsedatetime
Requires:       python3-petact >= 0.1.2
Requires:       python3-pip
Requires:       python3-pocketsphinx-python
Requires:       python3-precise-runner >= 0.2.1
Requires:       python3-psutil
Requires:       python3-pulsectl
Requires:       python3-pyalsaaudio
Requires:       python3-pycodestyle
Requires:       python3-pyee
Requires:       python3-pyserial
Requires:       python3-python-dateutil
Requires:       python3-python-vlc
Requires:       python3-requests >= 2.20.0
Requires:       python3-requests-futures >= 0.9.5
Requires:       python3-setuptools
Requires:       python3-six
Requires:       python3-tornado >= 4.5.3
Requires:       python3-virtualenv
Requires:       python3-virtualenvwrapper
Requires:       python3-websocket-client >= 0.32.0
#--- Requirements of the default skills
Requires:       python3-arrow
Requires:       python3-astral >= 1.4
Requires:       python3-ddg3
Requires:       python3-feedparser
Requires:       python3-humanhash3
Requires:       python3-ifaddr
Requires:       python3-multi_key_dict
Requires:       python3-netifaces
Requires:       python3-pyjokes
Requires:       python3-pyowm
Requires:       python3-pytz
Requires:       python3-tzlocal
Requires:       python3-wikipedia
Requires:       python3-wolframalpha
# Required by Plasma skills
Requires:       python3-PyAutoGUI
Requires:       python3-dbus-python
Requires:       python3-num2words
Requires:       python3-python-aiml
Requires:       python3-python-xlib
#----
Requires:       curl
Requires:       git
Requires:       jq
Requires:       mpg123
Requires:       mpg123-pulse
Requires:       openssl
Requires:       patch
Requires:       portaudio
Requires:       screen
Recommends:     espeak
Recommends:     plasma-mycroft
Recommends:     vlc
BuildArch:      noarch
%systemd_requires

%description
Mycroft is a voice assistant.

%prep
%setup -q -n %{name}-release-v%{version}
%patch1000 -p1
%patch1001 -p1
%patch1004 -p1
sed -i -s "s/==.*//" requirements.txt
sed -i -s "s,#!/usr/bin/env bash,#!/bin/bash," scripts/my-info.sh
sed -i -s "s,#!/usr/bin/env bash,#!/bin/bash," scripts/prepare-msm.sh

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/mycroft-core/skills
install -D -m644 %{S:1} %{buildroot}%{_datadir}/mycroft-core/version.json
install -d %{buildroot}%{_userunitdir}/
install -m 0644 %{S:2} %{S:3} %{S:4} %{S:5} %{S:6} %{buildroot}%{_userunitdir}/
install -D -m644 %{S:7} %{buildroot}%{_docdir}/mycroft-core/SKILL_README.md
install -D -m644 mycroft/configuration/mycroft.conf %{buildroot}%{_docdir}/mycroft-core/mycroft.conf
install -D -m644 %{S:8}     %{buildroot}%{_sysconfdir}/mycroft/mycroft.conf
install -D -m644 %{S:9}     %{buildroot}%{_datadir}/mycroft-core/mycroft-user-template.conf
install -D -m755 %{S:10}    %{buildroot}%{_datadir}/mycroft-core/create-initial-user-configuration.sh
install -D -m644 %{S:13}    %{buildroot}%{_datadir}/mycroft-core/skill-patches/mycroft-youtube.patch
install -D -m644 %{S:14}    %{buildroot}%{_datadir}/mycroft-core/skill-patches/mycroft-music-skill.patch
install -D -m644 %{S:15}    %{buildroot}%{_datadir}/mycroft-core/skill-patches/skill-desktop-launcher.patch
install -D -m644 %{S:16}    %{buildroot}%{_datadir}/mycroft-core/skill-patches/mycroft-fallback-duck-duck-go.patch
install -D -m644 %{S:17}    %{buildroot}%{_datadir}/mycroft-core/skill-patches/skill-autogui.patch
install -D -m644 %{S:18}    %{buildroot}%{_datadir}/mycroft-core/skill-patches/mycroft-weather.patch

%fdupes %{buildroot}/%{python3_sitelib}/mycroft

%post
echo "*** ATTENTION ***"
echo ""
echo "* You can configure your Mycroft instance preferences systemwide at:"
echo "    /etc/mycroft/mycroft.conf"
echo "  or locally for your user at:"
echo "    ~/.mycroft/mycroft.conf"
echo ""
echo "* The systemd units are"
echo "    - mycroft.target"
echo "    - mycroft-bus.service"
echo "    - mycroft-skills.service"
echo "    - mycroft-audio.service"
echo "    - mycroft-voice.service"
echo ""
echo "* Those are USER units which you can start issuing:"
echo "    systemctl --user daemon-reload"
echo "    systemctl --user start mycroft.target"
echo "  and stop with:"
echo "    systemctl --user stop mycroft.target"
echo ""
echo "* If you installed plasma-mycroft from packages, then it will"
echo "  start/stop the services automatically when enabling/disabling"
echo "  Mycroft from the user interface."

%files
%defattr(-,root,root)
%doc README.md ACKNOWLEDGEMENTS.md
%license LICENSE.md
%{_docdir}/mycroft-core
%dir %{_sysconfdir}/mycroft
%config %{_sysconfdir}/mycroft/mycroft.conf
%{_bindir}/mycroft-audio
%{_bindir}/mycroft-audio-test
%{_bindir}/mycroft-cli-client
%{_bindir}/mycroft-echo-observer
%{_bindir}/mycroft-enclosure-client
%{_bindir}/mycroft-messagebus
#%{_bindir}/mycroft-skill-container
%{_bindir}/mycroft-skills
%{_bindir}/mycroft-speech-client
%{_datadir}/mycroft-core
%{_userunitdir}/mycroft-bus.service
%{_userunitdir}/mycroft-skills.service
%{_userunitdir}/mycroft-audio.service
%{_userunitdir}/mycroft-voice.service
%{_userunitdir}/mycroft.target
%{python3_sitelib}/mycroft/
%{python3_sitelib}/mycroft_core-%{version}-py%{py3_ver}.egg-info

%changelog
