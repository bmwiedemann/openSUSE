#
# spec file for package gede
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2022 Bruno Pitrus <brunopitrus@hotmail.com>
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

Version:        2.21.1
Release:        0

%if "@BUILD_FLAVOR@" == "qt6"
Name:           gede-qt6
%global QTVER 6
Provides:       gede = %version
Conflicts:      gede
%else
Name:           gede
%global QTVER 5
%endif
Summary:        Qt{%QTVER}-based GUI to GDB
License:        BSD-2-Clause
Group:          Development/Tools/Debuggers
URL:            https://gede.dexar.se
Source0:        https://github.com/jhn98032/gede/archive/refs/tags/v%{version}.tar.gz
Source1:        gede.desktop
BuildRequires:  pkgconfig(Qt%{QTVER}SerialPort)
BuildRequires:  pkgconfig(Qt%{QTVER}Widgets)
%if "@BUILD_FLAVOR@" == "qt6"
BuildRequires:  qt6-macros
%else
BuildRequires:  libqt5-qtbase-common-devel
%endif
Requires:       /usr/bin/ctags
Recommends:     gdb

%description
Gede is a graphical frontend (GUI) to GDB written in C++ and using the Qt5 toolkit.
Gede supports debugging programs written in Ada, FreeBasic, C++, C, Rust, Fortran and Go.
%prep
%setup -q -n gede-%{version}

%build
cd src
%if "@BUILD_FLAVOR@" == "qt6"
%qmake6
%else
%qmake5
%endif
#Qmake adds this relocation model which is not needed for the main binary and produces worse code
sed -i 's/ -fPIC / /g' Makefile
%make_jobs

%install
install -pvDm755 src/gede -t %{buildroot}%{_bindir}
install -pvDm644 AppDir/gede_icon.png -t %{buildroot}%{_datadir}/pixmaps
install -pvDm644 %{_sourcedir}/gede.desktop -t %{buildroot}%{_datadir}/applications

%check

#The other programs in tests/ are samples/debug tools for the embedded highlighter library, not test suites.
cd tests/ini
%if "@BUILD_FLAVOR@" == "qt6"
%qmake6
%else
%qmake5
%endif
sed -i 's/ -fPIC / /g' Makefile
%make_jobs
./test_ini





%files
%{_bindir}/gede
%{_datadir}/applications/gede.desktop
%{_datadir}/pixmaps/gede_icon.png
%license LICENSE
%doc README.rst

%changelog
