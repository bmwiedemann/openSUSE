#
# spec file for package mpc-qt
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


Name:           mpc-qt
Version:        24.06
Release:        0
Summary:        Media Player Classic Qute Theater
License:        GPL-2.0-only
URL:            https://github.com/cmdrkotori/mpc-qt
Source0:        https://github.com/mpc-qt/mpc-qt/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.changes
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  qt6-tools-linguist
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6OpenGLWidgets)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(mpv) >= 1.101.0
%if 0%{?suse_version} > 1500
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc10-c++
%endif

%description
A clone of Media Player Classic reimplemented in Qt.

%prep
%autosetup -p1
rm -rf mpv-dev

%build
export CXX=g++
test -x "$(type -p g++-10)" && export CXX=g++-10
qmake6 \
  QMAKE_CFLAGS+="%{optflags} -fpie" QMAKE_CXXFLAGS+="%{optflags} -fpie" \
  QMAKE_LFLAGS="%{optflags} -pie" QMAKE_CC="${CC}" QMAKE_CXX="${CXX}" \
  PREFIX=%{_prefix} MPCQT_VERSION=%{version} \
  mpc-qt.pro
%make_build

%install
mkdir -p %{buildroot}/%{_bindir} \
         %{buildroot}/%{_datadir}/applications \
         %{buildroot}/%{_datadir}/pixmaps \
         %{buildroot}/%{_datadir}/%{name}/translations
install -m 0755 %{name} %{buildroot}/%{_bindir}
install -m 0644 images/icon/mpc-qt.svg %{buildroot}/%{_datadir}/pixmaps/%{name}.svg
install -m 0644 %{name}_*.qm -t %{buildroot}/%{_datadir}/%{name}/translations
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
