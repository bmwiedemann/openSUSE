#
# spec file for package mpc-qt
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


Name:           mpc-qt
Version:        20.10
Release:        0
Summary:        Media Player Classic Qute Theater
License:        GPL-2.0-only
URL:            https://github.com/cmdrkotori/mpc-qt
Source0:        https://github.com/cmdrkotori/mpc-qt-origin/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.changes
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.4
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(mpv) >= 1.101.0
%if 0%{?suse_version} > 1500
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc7-c++
%endif

%description
A clone of Media Player Classic reimplemented in Qt.

%prep
%autosetup -p1 -n mpc-qt-origin-%{version}
rm -rf mpv-dev

%build
export CXX=g++
test -x "$(type -p g++-7)" && export CXX=g++-7
qmake-qt5 \
  QMAKE_CFLAGS+="%{optflags}" QMAKE_CXXFLAGS+="%{optflags}" \
  QMAKE_CC="${CC}" QMAKE_CXX="${CXX}" PREFIX=%{_prefix} \
  mpc-qt.pro
%make_build

%install
mkdir -p %{buildroot}/%{_bindir} \
         %{buildroot}/%{_datadir}/applications \
         %{buildroot}/%{_datadir}/pixmaps \
         %{buildroot}/%{_datadir}/%{name}/translations
install -m 0755 %{name} %{buildroot}/%{_bindir}
install -m 0644 images/icon/mpc-qt.svg %{buildroot}/%{_datadir}/pixmaps/%{name}.svg
install -m 0644 resources/translations/%{name}_*.qm -t %{buildroot}/%{_datadir}/%{name}/translations
install -m 0644 mpc-qt.desktop %{buildroot}/%{_datadir}/applications/Media\ Player\ Classic\ Qute\ Theater.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/applications/*.desktop
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/translations/%{name}_*.qm

%changelog
