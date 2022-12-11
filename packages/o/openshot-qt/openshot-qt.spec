#
# spec file for package openshot-qt
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


%define appname org.openshot.OpenShot
Name:           openshot-qt
Version:        3.0.0
Release:        0
Summary:        Non-linear video editor with broad format support
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://openshot.org/
Source:         openshot-qt-%{version}.tar.xz
# PATCH-FIX-OPENSUSE openshot-qt-disable-sending-metrics.patch -- disable sending anonymous metrics and errors by default to Google Analytics
Patch0:         openshot-qt-disable-sending-metrics.patch
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-openshot >= 0.3.0
BuildRequires:  python3-pytest
# Check list of dependencies:
BuildRequires:  python3-pyxdg
BuildRequires:  python3-pyzmq
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-qtwebengine-qt5
BuildRequires:  python3-setuptools
BuildRequires:  shared-mime-info
BuildRequires:  update-desktop-files
Requires:       python3-openshot >= 0.3.0
Requires:       python3-pyxdg
Requires:       python3-pyzmq
Requires:       python3-qt5
Requires:       python3-qtwebengine-qt5
Requires:       python3-requests
Provides:       openshot = %{version}
Obsoletes:      openshot < %{version}
BuildArch:      noarch

%description
OpenShot Video Editor is a non-linear video editor. It can create and
edit videos and movies using many video, audio, and image formats.

%prep
%setup -q
%patch0 -p1
sed -e 's|pixmaps|icons/hicolor/scalable/apps|' \
    -e '/lib.mime.packages/d' \
    -i setup.py

find . -type f -name '*.py' \
  -exec perl -n -i -e 'print $_ unless ($.==1 and /^#!/)' {} \;

chmod -x src/language/*.py
chmod -x src/presets/format_*.xml

%build
%python3_build

%install
%python3_install
%suse_update_desktop_file -r %{appname} AudioVideo AudioVideoEditing
%fdupes -s %{buildroot}%{python3_sitelib}

%check
python3 -B ./src/tests/query_tests.py -platform minimal

%files
%doc AUTHORS README.md
%license COPYING
%dir %{_datadir}/icons/hicolor/*/apps
%dir %{_datadir}/icons/hicolor/*
%{_bindir}/%{name}
%{python3_sitelib}/openshot_qt
%{python3_sitelib}/openshot_qt-%{version}*-info
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/metainfo/%{appname}.appdata.xml
%{_datadir}/mime/packages/%{appname}.xml
%{_datadir}/icons/hicolor/*/*/%{name}*.??g

%changelog
