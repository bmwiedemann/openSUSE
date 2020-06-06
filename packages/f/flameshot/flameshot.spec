#
# spec file for package flameshot
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


Name:           flameshot
Version:        0.6.0
Release:        0
Summary:        Screenshot software
License:        GPL-3.0-only
Group:          Productivity/Graphics/Other
URL:            https://github.com/lupoDharkael/flameshot#flameshot
Source0:        https://github.com/lupoDharkael/flameshot/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         desktop-files.patch
Patch2:         0001-utils-confighandler.cpp-Enable-Pin-and-Text-tool-by-.patch
# PATCH-FIX-UPSTREAM
Patch3:         0001-Fix-build-with-Qt-5.15.patch
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-qtbase
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core) >= 5
BuildRequires:  pkgconfig(Qt5DBus) >= 5
BuildRequires:  pkgconfig(Qt5Gui) >= 5
BuildRequires:  pkgconfig(Qt5Network) >= 5
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets) >= 5
%if 0%{?suse_version} >= 1500
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc7
BuildRequires:  gcc7-c++
%endif

%description
A program to capture screenshots.
It includes CLI options as well as a UI for capturing and annotating screenshots.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          Productivity/Graphics/Other
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (flameshot and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash completion script for flameshot's CLI.

%prep
%autosetup -p1

%if 0%{?suse_version} < 1500
sed -i '/appdata.path/s/metainfo/appdata/' flameshot.pro
%endif

%build
%qmake5 \
%if 0%{?suse_version} < 1500
 QMAKE_CC=gcc-7 QMAKE_CXX=g++-7 \
%endif
 CONFIG+=packaging
%make_jobs

%install
%qmake5_install

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/org.dharkael.Flameshot.service
%{_datadir}/dbus-1/interfaces/org.dharkael.Flameshot.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%if 0%{?suse_version} >= 1500
%{_datadir}/metainfo/%{name}.appdata.xml
%else
%{_datadir}/appdata/%{name}.appdata.xml
%endif

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%changelog
