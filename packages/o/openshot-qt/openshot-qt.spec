#
# spec file for package openshot-qt
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        4.0.0
Release:        0
Summary:        Non-linear video editor with broad format support
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://openshot.org/
Source:         openshot-qt-%{version}.tar.xz
# PATCH-FIX-OPENSUSE openshot-qt-disable-sending-metrics.patch -- disable sending anonymous metrics and errors by default to Google Analytics
Patch0:         openshot-qt-disable-sending-metrics.patch
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-openshot >= 1.0.0
BuildRequires:  python3-pip
# Check list of dependencies:
BuildRequires:  python3-pyzmq
BuildRequires:  python3-qt6-devel
BuildRequires:  python3-setuptools
BuildRequires:  shared-mime-info
Requires:       python3-openshot >= 1.0.0
Requires:       python3-pyzmq
Requires:       python3-qt6
Requires:       python3-requests
# Upstream guards all of these behind try/ImportError and degrades gracefully,
# so they are not hard dependencies -- but each one enables a real feature:
# defusedxml (hardened XML parsing), distro (OS name in About/metrics),
# numpy (vectorscope hue labels), opengl (preloads libGL before QApplication,
# for the video preview). certifi is deliberately not listed: python3-requests
# already requires it, and our certifi points at the system /etc/ssl/ca-bundle.pem
# anyway, so classes/http_client.py's "packaged CA bundle" path is a no-op here.
Recommends:     python3-defusedxml
Recommends:     python3-distro
Recommends:     python3-numpy
Recommends:     python3-opengl
Provides:       openshot = %{version}
Obsoletes:      openshot < %{version}
BuildArch:      noarch

%description
OpenShot Video Editor is a non-linear video editor. It can create and
edit videos and movies using many video, audio, and image formats.

%prep
%autosetup -p1

sed -e 's|pixmaps|icons/hicolor/scalable/apps|' \
    -e '/lib.mime.packages/d' \
    -i setup.py

find . -type f -name '*.py' \
  -exec perl -n -i -e 'print $_ unless ($.==1 and /^#!/)' {} \;

# This is a Qt application, GNOME/GTK are not valid categories for it.
# Replaces the deprecated %%suse_update_desktop_file -- to be dropped once
# https://github.com/OpenShot/openshot-qt/ ships correct categories.
sed -i -e '/^Categories=/s|.*|Categories=AudioVideo;Video;AudioVideoEditing;Qt;|' \
    xdg/%{appname}.desktop

%build
%python3_pyproject_wheel

%install
%python3_pyproject_install
# Nothing shipped in sitelib is meant to be run directly, and %%prep already
# stripped the shebangs -- drop the executable bits so rpmlint is happy.
find %{buildroot}%{python3_sitelib} -type f \( -name '*.py' -o -name '*.xml' \) \
  -exec chmod a-x {} +
%fdupes -s %{buildroot}%{python3_sitelib}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appname}.desktop
# Upstream's unittest suite (openshot_qt/tests) is not run: it does not pass in
# the OBS build environment. To retry it after an upstream fix:
#   export QT_QPA_PLATFORM=offscreen
#   export PYTHONPATH="%%{buildroot}%%{python3_sitelib}:%%{buildroot}%%{python3_sitelib}/openshot_qt"
#   %%{__python3} -m unittest discover -s %%{buildroot}%%{python3_sitelib}/openshot_qt/tests \
#     -t %%{buildroot}%%{python3_sitelib}/openshot_qt

%files
%doc README.md
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
