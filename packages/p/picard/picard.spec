#
# spec file for package picard
#
# Copyright (c) 2022 SUSE LLC
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
Version:        2.8.4
Release:        0
Summary:        The Next Generation MusicBrainz Tagger
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://picard.musicbrainz.org
Source0:        https://codeload.github.com/metabrainz/picard/tar.gz/release-%{version}#/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libofa-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-fasteners
BuildRequires:  python3-mutagen >= 1.37
BuildRequires:  python3-qt5 >= 5.11
BuildRequires:  python3-setuptools
BuildRequires:  python3-sip
BuildRequires:  update-desktop-files
Requires:       python3-Markdown
Requires:       python3-PyYAML
Requires:       python3-dateutil >= 2.7.3
Requires:       python3-fasteners
Requires:       python3-mutagen >= 1.37
Requires:       python3-qt5 >= 5.11
Recommends:     chromaprint-fpcalc
Recommends:     python3-discid

%description
MusicBrainz Picard is a MusicBrainz tag editor written in Python.
Picard Tagger focuses on album-oriented tagging as opposed to
track-based tagging.

%lang_package

%prep
%setup -q -n %{name}-release-%{version}

%build
export LANG=en_US.UTF-8
python3 setup.py config
python3 setup.py build

%install
export LANG=en_US.UTF-8
python3 setup.py install --skip-build --prefix=%{_prefix} --root=%{buildroot}

%suse_update_desktop_file -G "Music Tagger" -N "picard" org.musicbrainz.Picard

rm -rfv %{buildroot}%{_datadir}/locale/sco

%find_lang %{name} %{name}.lang
%find_lang %{name}-countries %{name}.lang
%find_lang %{name}-attributes %{name}.lang

%if 0%{?suse_version} < 1500
%post
%icon_theme_cache_post

%postun
%icon_theme_cache_postun
%endif

%files
%doc AUTHORS.txt NEWS.md
%license COPYING.txt
%{_bindir}/picard
%{_datadir}/applications/org.musicbrainz.Picard.desktop
%{python3_sitearch}/picard*
%{_datadir}/icons/hicolor/*/apps/org.musicbrainz.Picard.png
%{_datadir}/icons/hicolor/*/apps/org.musicbrainz.Picard.svg
%{_datadir}/metainfo/org.musicbrainz.Picard.appdata.xml

%files lang -f %{name}.lang

%changelog
