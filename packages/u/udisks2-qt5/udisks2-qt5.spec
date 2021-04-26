#
# spec file for package udisks2-qt5
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define sover 0

Name:           udisks2-qt5
Version:        5.0.5
Release:        0
Summary:        UDisks2 library with Qt5
License:        LGPL-3.0+
URL:            https://github.com/linuxdeepin/udisks2-qt5
Source0:        https://github.com/linuxdeepin/udisks2-qt5/archive/%{version}/%{name}-%{version}.tar.gz
Group:          System/Libraries
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
UDisks2 library with Qt5

UDisks2 DBus interfaces binding of Qt5.

%package -n lib%{name}-%{sover}
Summary:        Development tools for Deepin Anything
Group:          System/Libraries


%description -n lib%{name}-%{sover}
UDisks2 library with Qt5

UDisks2 DBus interfaces binding of Qt5.

%package devel
Summary:        Development tools for Deepin Anything
Group:          Development/Languages/C and C++
Requires:       lib%{name}-%{sover} = %{version}-%{release}

%description devel
The %{name}-devel package contains the header files and developer
docs for udisks2-qt5.

%prep
%setup -q

%build
%qmake5 LIB_INSTALL_DIR=%{_libdir}
%make_build

%install
%qmake5_install

%post -n lib%{name}-%{sover} -p /sbin/ldconfig

%postun -n lib%{name}-%{sover} -p /sbin/ldconfig

%files -n lib%{name}-%{sover}
%defattr(-,root,root,-)
%doc CHANGELOG.md
%license LICENSE
%{_libdir}/lib%{name}.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
