#
# spec file for package beets
#
# Copyright (c) 2025 SUSE LLC
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


%if 0%{?suse_version} > 1500
# Build only one time
%define pythons %{primary_python}
%else
# Build only with python 3.11
%{?sle15_python_module_pythons}
%endif
Name:           beets
Version:        2.2.0
Release:        0
Summary:        Music tagger and library organizer
License:        MIT
Group:          Productivity/Multimedia/Sound/Players
URL:            http://beets.io/
Source:         https://github.com/beetbox/beets/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-PyYAML
BuildRequires:  python3-Unidecode
BuildRequires:  python3-confuse >= 1.5.0
BuildRequires:  python3-devel >= 3.8.0
BuildRequires:  python3-jellyfish
BuildRequires:  python3-mediafile >= 0.12.0
BuildRequires:  python3-munkres
BuildRequires:  python3-musicbrainzngs >= 0.4
BuildRequires:  python3-pip
BuildRequires:  python3-poetry-core
BuildRequires:  python3-setuptools
# test requirements
BuildRequires:  python3-Flask
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-discogs-client
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
Requires:       python3-confuse >= 1.5.0
Requires:       python3-jellyfish
Requires:       python3-mediafile >= 0.12.0
Requires:       python3-munkres
Requires:       python3-musicbrainzngs >= 0.4
Requires:       python3-musicbrainzngs >= 0.4
Requires:       python3-platformdirs
Recommends:     ffmpeg
Recommends:     python3-Flask
Recommends:     python3-Flask-Cors
Recommends:     python3-dbus-python
Recommends:     python3-discogs-client >= 2.3.15
Recommends:     python3-pyacoustid
Recommends:     python3-pylast
Recommends:     python3-python-mpd2
Recommends:     python3-pyxdg
Recommends:     python3-rarfile
Recommends:     python3-requests
Recommends:     python3-requests
Recommends:     python3-requests-oauthlib >= 0.6.1
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

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE
%{_bindir}/beet
%{python3_sitelib}/*

%changelog
