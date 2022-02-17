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


Name:           gede
Version:        2.18.2
Release:        0
Summary:        Qt-based GUI to GDB
License:        BSD-2-Clause
Group:          Development/Tools/Debuggers
URL:            https://gede.dexar.se
Source0:        https://gede.dexar.se/uploads/source/gede-%{version}.tar.xz
Source1:        gede.desktop
BuildRequires:  libQt5Widgets-devel
BuildRequires:  libqt5-qtbase-common-devel
Requires:       ctags
Recommends:     gdb

%description
Gede is a graphical frontend (GUI) to GDB written in C++ and using the Qt5 toolkit.
Gede supports debugging programs written in Ada, FreeBasic, C++, C, Rust, Fortran and Go.

%prep
%setup -q

%build
cd src
%qmake5
%make_jobs

%install
install -pvDm755 %{_builddir}/%{name}-%{version}/src/gede -t %{buildroot}%{_bindir}
install -pvDm644 %{_sourcedir}/gede.desktop -t %{buildroot}%{_datadir}/applications

%files
%{_bindir}/gede
%{_datadir}/applications/gede.desktop
%license LICENSE
%doc README

%changelog
