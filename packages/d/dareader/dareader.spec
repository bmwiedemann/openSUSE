#
# spec file for package dareader
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

%define   sover           1
%define   commit          2d7d79c45d5c8a1dc5102d9e29fbfdd2e404b966
%define   shortcommit     2d7d79c

Name:           dareader
Version:        0.0.0+git20220726.%{shortcommit}
Release:        0
Summary:        Read image/video from socket file
License:        GPL-3.0+
URL:            https://github.com/linuxdeepin/dareader
Source0:        https://github.com/linuxdeepin/dareader/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# PATCH-FOR-OPENSUSE fix-link-library.patch hillwood@opensuse.org - Fix library link
Patch0:         fix-link-library.patch
Group:          Productivity/Multimedia/Other
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Read image/video from socket file

%package -n lib%{name}%{sover}
Summary:        Read image/video from socket file
Group:          System/Libraries

%description -n lib%{name}%{sover}
Read image/video from socket file

%package devel
Summary:        Development tools for dareader
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}-%{release}

%description devel
The dareader-devel package contains the header files for dareader.

%prep
%setup -q -n %{name}-%{commit}
%if 0%{?suse_version} <= 1500
%patch0 -p1
%endif

%build
%cmake
%cmake_build

%install
%cmake_install

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.*

%files devel
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/reader.h

%changelog

