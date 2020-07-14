#
# spec file for package kristall
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


Name:           kristall
Version:        0.3
Release:        0
Summary:        Graphical small-internet client
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Browsers
URL:            https://kristall.random-projects.net/
Source:         https://github.com/MasterQ32/kristall/archive/V%{version}.tar.gz
# Use qmake-qt5 instad of qmake
Patch0:         kristall-qmake5.patch
BuildRequires:  hicolor-icon-theme
BuildRequires:  libopenssl-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtmultimedia-devel
BuildRequires:  libqt5-qtsvg-devel

%description
Graphical small-internet client supporting gemini, http, https, gopher, finger.

%prep
%setup -q
%patch0 -p1

%build
%make_build PREFIX=%{_prefix}

%install
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
mkdir -p %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_bindir}/
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/kristall
%{_datadir}/applications/Kristall.desktop
%{_datadir}/icons/hicolor/??x??/apps/net.random-projects.kristall.png
%{_datadir}/icons/hicolor/128x128/apps/net.random-projects.kristall.png
%{_datadir}/icons/hicolor/scalable/apps/net.random-projects.kristall.svg

%changelog
