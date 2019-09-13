#
# spec file for package qxtglobalshortcut
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define commit 688715b349f7661f55347252850839e85e0a5e00
%define rhash 688715b
%define rtime 1533120914
Name:           qxtglobalshortcut
Version:        0.0.1+git%{rtime}.%{rhash}
Release:        0
Summary:        Library for handling system-wide shortcuts in Qt applications
License:        BSD-Source-Code
Group:          Development/Libraries/C and C++
URL:            https://github.com/hluk/qxtglobalshortcut
Source:         %{name}-%{commit}.tar.gz
BuildRequires:  cmake >= 3.0
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
Library for handling system-wide shortcuts in Qt applications.

%package devel
Summary:        Development files for qxtglobalshortcut
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}

%description devel
This package provides header files and documentation for developing
applications using qxtglobalshortcut library.

%package -n lib%{name}%{sover}
Summary:        Library for handling system-wide shortcuts in Qt applications
Group:          System/Libraries

%description -n lib%{name}%{sover}
Library for handling system-wide shortcuts in Qt applications.

%prep
%setup -q -n %{name}-%{commit}

# remove windows files
rm -rf utils/appveyor/
rm -f appveyor.yml

%build
%cmake \
	-DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed"
make %{?_smp_mflags} V=1

%install
%cmake_install

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.*

%files devel
%license COPYING
%doc AUTHORS README.md
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
