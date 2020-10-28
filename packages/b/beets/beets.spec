#
# spec file for package beets
#
# Copyright (c) 2020 SUSE LLC
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


Name:           beets
Version:        1.4.9
Release:        0
Summary:        Music tagger and library organizer
License:        MIT
Group:          Productivity/Multimedia/Sound/Players
URL:            http://beets.io/
Source:         https://github.com/beetbox/beets/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-Fixed-failing-test-where.patch
# PATCH-FIX-UPSTREAM fix_test_command_line_option_relative_to_working_dir.diff alarrosa@suse.de - Fixes one of the tests to run successfully
Patch1:         fix_test_command_line_option_relative_to_working_dir.diff
# PATCH-FIX-UPSTREAM 0001-Compatibility-with-breaking-changes-to-the-ast-module.patch -- Fix from upstream for boo#1178199
Patch2:         0001-Compatibility-with-breaking-changes-to-the-ast-module.patch
BuildRequires:  python3-PyYAML
BuildRequires:  python3-Unidecode
BuildRequires:  python3-devel
BuildRequires:  python3-jellyfish
BuildRequires:  python3-munkres
BuildRequires:  python3-musicbrainzngs >= 0.4
BuildRequires:  python3-mutagen >= 1.33
BuildRequires:  python3-setuptools
BuildRequires:  python3-six >= 1.9
# test requirements
BuildRequires:  python3-Flask
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-discogs-client
BuildRequires:  python3-mock
%if 0%{?suse_version} <= 1320
BuildRequires:  python3-pathlib
%endif
BuildRequires:  python3-pylast
BuildRequires:  python3-python-mpd2 >= 0.4.2
BuildRequires:  python3-pyxdg
BuildRequires:  python3-rarfile
BuildRequires:  python3-responses
BuildRequires:  python3-testsuite
Requires:       python3-PyYAML
Requires:       python3-Unidecode
Requires:       python3-jellyfish
Requires:       python3-munkres
Requires:       python3-musicbrainzngs >= 0.4
Requires:       python3-mutagen >= 1.33
Requires:       python3-six >= 1.9
Recommends:     python3-pyacoustid
Recommends:     python3-flask
Recommends:     python3-flask-cors
Recommends:     python3-discogs-client >= 2.1.0
Recommends:     python3-pyxdg
Recommends:     python3-requests
Recommends:     python3-dbus-python
Recommends:     python3-rarfile
Recommends:     python3-requests-oauthlib >= 0.6.1
Recommends:     python3-python-mpd2
Recommends:     python3-pylast
Recommends:     python3-requests
Recommends:     ffmpeg
Suggests:       flac
Suggests:       mp3val
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Beets is a media library management system for obsessive-compulsive music
geeks.

The purpose of beets is to get a music collection right once and for all.
It catalogs the collection, automatically improving its metadata as it goes.
It then provides a bouquet of tools for manipulating and accessing the music.

beets is designed as a library, has a number of plugins which
support these actions:

- Fetch or calculate all the metadata that could possibly be needed:
  album art, lyrics, genres, tempos, ReplayGain levels, or acoustic
  fingerprints.
- Get metadata from MusicBrainz, Discogs, and Beatport, or guess
  metadata using songs' filenames or their acoustic fingerprints.
- Transcode audio to any format.
- Check your library for duplicate tracks and albums or for albums that
  are missing tracks.
- Clean up crufty tags left behind by other tools.
- Embed and extract album art from files' metadata.
- Browse the music library graphically through a Web browser and play it in any
  browser that supports HTML5 Audio.
- Analyze music files' metadata from the command line.
- Listen to your library with a music player that speaks the MPD protocol
  and works with a variety of interfaces.

Writing additional plugins for beets is possible using Python.

%prep
%setup -q -n beets-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE
%{_bindir}/beet
%{python3_sitelib}/*

%changelog
