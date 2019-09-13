#
# spec file for package libmaia
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

%define _sover  1
Name:           libmaia
Version:        0.9.0
Release:        0
Summary:        XML-RPC library for Qt
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
Url:            https://github.com/wiedi/libmaia
Source0:        https://github.com/wiedi/libmaia/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libmaia is a XML-RPC library for Qt.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/C and C++
Requires:       %{name}%{_sover} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package     -n %{name}%{_sover}
Summary:        XML-RPC library for Qt
Group:          System/Libraries

%description -n %{name}%{_sover}
libmaia is a XML-RPC library for Qt.

%prep
%setup -q
sed -e 's|/lib|/%{_lib}|' -e 's|staticlib|sharedlib|' -i maia.pro

%build
export CXXFLAGS="-fPIC"
%qmake5 PREFIX=%{_prefix}
make %{?_smp_mflags}

%install
%qmake5_install
mkdir -pv %{buildroot}%{_libdir}/pkgconfig
# creates support file for pkg-config
tee %{buildroot}/%{_libdir}/pkgconfig/maia.pc << "EOF"
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=${exec_prefix}/%{_lib}
includedir=${prefix}/include

Name: maia
Description: XML-RPC library for Qt
Version: %{version}
Libs: -L${libdir} -lmaia
Cflags: -I${includedir}/maia
EOF

%post -n %{name}%{_sover} -p /sbin/ldconfig
%postun -n %{name}%{_sover} -p /sbin/ldconfig

%files -n %{name}%{_sover}
%defattr(-,root,root)
%doc Changelog LICENSE README.md
%{_libdir}/%{name}.so.%{_sover}*

%files devel
%defattr(-,root,root)
%doc Changelog LICENSE README.md
%dir %{_includedir}/maia
%{_includedir}/maia/maiaObject.h
%{_includedir}/maia/maiaXmlRpcClient.h
%{_includedir}/maia/maiaXmlRpcServer.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/maia.pc

%changelog
