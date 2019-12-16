#
# spec file for package whipper
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


Name:           whipper
Version:        0.9.0
Release:        0
Summary:        A CD ripper aiming for accuracy over speed
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/CD/Grabbers
URL:            https://github.com/JoeLametta/whipper/
Source0:        https://github.com/JoeLametta/whipper/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  libsndfile-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
# SECTION test requirements
BuildRequires:  cd-paranoia >= 10.2
BuildRequires:  cdrdao
BuildRequires:  python3-Twisted
BuildRequires:  python3-musicbrainzngs
BuildRequires:  python3-mutagen
BuildRequires:  python3-pycdio
BuildRequires:  python3-pytest
BuildRequires:  python3-requests
BuildRequires:  python3-ruamel.yaml
BuildRequires:  sox
# /SECTION
# nb: there is a difference between cd-paranoia [we want] and
#     cdparanoia [we don't]
Requires:       cd-paranoia >= 10.2
Requires:       cdrdao
Requires:       flac
Requires:       python3-gobject
Requires:       python3-musicbrainzngs
Requires:       python3-mutagen
Requires:       python3-pycdio
Requires:       python3-requests
Requires:       python3-ruamel.yaml
Requires:       sox
Conflicts:      morituri

%description
Whipper is an audio CD ripper that aims for accuracy over speed. It
automatically tags tracks using MusicBrainz data, takes drive offsets into
account, supports AccurateRip, and can rip certain hidden tracks.
It is written in Python 2. Whipper was forked from the Morituri project,
after Morituri development halted.

%prep
%setup -q

%build
echo "Version: %{version}" > PKG-INFO
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python_sitearch}

%check
export PYTHONPATH=%{buildroot}%{python3_sitearch}
cd whipper/test/
# Don't run accurip tests since those needs a network connection to www.accuraterip.com
rm -f test_common_accurip.py
/usr/bin/py.test3

%files
%doc CHANGELOG.md README
%license LICENSE
%{_bindir}/accuraterip-checksum
%{_bindir}/whipper
%{python3_sitearch}/whipper
%{python3_sitearch}/accuraterip.cpython*
%{python3_sitearch}/%{name}-%{version}-py%{py3_ver}.egg-info
%{_datadir}/metainfo/com.github.whipper_team.Whipper.metainfo.xml

%changelog
