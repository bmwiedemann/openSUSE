#
# spec file for package disomaster
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

%define  sover  1

Name:           disomaster
Version:        5.0.5
Release:        0
License:        GPL-3.0+
Summary:        A libisoburn wrapper
Url:            https://github.com/linuxdeepin/disomaster
Group:          Hardware/Other
Source0:        https://github.com/linuxdeepin/disomaster/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(libisoburn-1)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A libisoburn wrapper class for Qt.

%package -n lib%{name}%{sover}
Group:          System/Libraries
Summary:        Disomaster Libraries

%description -n lib%{name}%{sover}
A libisoburn wrapper class for Qt.

The lib%{name}%{sover} package contains the Libraries for
disomaster movie.

%package devel
Summary:        Development tools for deepin movie
Group:          Development/Languages/C and C++
Requires:       lib%{name}%{sover} = %{version}

%description devel
The disomaster-devel package contains the header files and developer docs for
disomaster movie.

%prep
%setup
sed -i 's|target.path = $$PREFIX/lib|target.path = $$LIBDIR|g' libdisomaster/libdisomaster.pro

%build
%qmake5 PREFIX=%{_prefix} \
        LIBDIR=%{_libdir}
%make_build

%install
%qmake5_install

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%defattr(-,root,root,-)
%{_libdir}/lib%{name}.so.*

%files devel
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
