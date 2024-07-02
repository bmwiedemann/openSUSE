#
# spec file for package picard
#
# Copyright (c) 2024 SUSE LLC
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


Name:           picard
Version:        2.12
Release:        0
Summary:        The Next Generation MusicBrainz Tagger
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://picard.musicbrainz.org
Source0:        https://codeload.github.com/metabrainz/picard/tar.gz/release-%{version}#/%{name}-%{version}.tar.gz
# PATCH-FIX-SUSE picard-requirements.patch, code@bnavigator.de -- clean python requirements metadata
Patch0:         picard-requirements.patch
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libofa-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  update-desktop-files
Requires:       python3-Markdown >= 3.2
Requires:       python3-PyJWT >= 2.0
Requires:       python3-PyQt5 >= 5.11
Requires:       python3-PyYAML >= 5.1
Requires:       python3-discid >= 1.0
Requires:       python3-fasteners >= 0.14
Requires:       python3-mutagen >= 1.37
Requires:       python3-python-dateutil >= 2.7
Recommends:     chromaprint-fpcalc
# SECTION test
BuildRequires:  python3-Markdown >= 3.2
BuildRequires:  python3-PyJWT >= 2.0
BuildRequires:  python3-PyQt5 >= 5.11
BuildRequires:  python3-PyYAML >= 5.1
BuildRequires:  python3-discid >= 1.0
BuildRequires:  python3-fasteners >= 0.14
BuildRequires:  python3-mutagen >= 1.37
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-xvfb
BuildRequires:  python3-python-dateutil >= 2.7
# /SECTION

%description
MusicBrainz Picard is a MusicBrainz tag editor written in Python.
Picard Tagger focuses on album-oriented tagging as opposed to
track-based tagging.

%lang_package

%prep
%autosetup -p1 -n %{name}-release-%{version}

%build
export LANG=en_US.UTF-8
%python3_pyproject_wheel

%install
export LANG=en_US.UTF-8
%python3_pyproject_install

%suse_update_desktop_file -G "Music Tagger" -N "picard" org.musicbrainz.Picard

rm -rfv %{buildroot}%{_datadir}/locale/sco

%find_lang %{name} %{name}.lang
%find_lang %{name}-countries %{name}.lang
%find_lang %{name}-attributes %{name}.lang
%fdupes %{buildroot}%{python3_sitearch}

%check
pytest -v

%files
%doc AUTHORS.txt NEWS.md
%license COPYING.txt
%{_bindir}/picard
%{_datadir}/applications/org.musicbrainz.Picard.desktop
%{python3_sitearch}/picard
%{python3_sitearch}/picard-%{version}.dist-info
%{_datadir}/icons/hicolor/*/apps/org.musicbrainz.Picard.png
%{_datadir}/icons/hicolor/*/apps/org.musicbrainz.Picard.svg
%{_datadir}/metainfo/org.musicbrainz.Picard.appdata.xml

%files lang -f %{name}.lang
%{_datadir}/locale/*/LC_MESSAGES/picard-constants.mo

%changelog
