#
# spec file for package etrophy
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           etrophy
Version:	0.5.1
Release:        1
License:        BSD-2-Clause
Summary:        Library managing scores, trophies and unlockables
Url:            http://enlightenment.org/
Group:          Development/Libraries/C and C++
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  elementary-devel
BuildRequires:  efl-devel

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ETrophy is a library that manages scores, trophies and unlockables. It will
store them and provide views to display them. Could be used by games based
on EFL.

%package -n libetrophy0
Summary:        Etrophy Dynamic Libraries
Group:          System/Libraries

%description -n libetrophy0
Etrophy is core EFL (Enlightenment Foundation Libraries) library to handle various data types.

%package data
Summary:        Etrophy shared data
Group:          Development/Libraries/C and C++
%if 0%{?suse_version} && 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description data
Package containing edje file for ETrophy.

%package devel
Summary:        Etrophy development files
Group:          Development/Libraries/C and C++
Requires:       libetrophy0 = %{version}
Requires:       %{name}-data = %{version}
Requires:       elementary-devel
Requires:       efl-devel
 
%description devel
Headers and other files used for development using etrophy

%prep
%setup -q

%build
%if 0%{?mandriva_version} || 0%{?centos_version}
autoreconf -ifv
%endif
%configure \
        --disable-static \
        --disable-silent-rules \
        --enable-doc
make %{?_smp_mflags} CFLAGS="%optflags"

%install
make install DESTDIR="%buildroot"
find %{buildroot}%{_libdir} -name '*.la' -exec rm -v {} \;

%clean
rm -rf %{buildroot}

%post -n libetrophy0 -p /sbin/ldconfig

%postun -n libetrophy0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README NEWS TODO AUTHORS ChangeLog COPYING

%files -n libetrophy0
%defattr(-,root,root)
%{_libdir}/libetrophy.so.*

%files data
%defattr(-,root,root)
%{_datadir}/etrophy

%files devel
%defattr(-, root, root)
%{_includedir}/etrophy-0/
%{_libdir}/pkgconfig/etrophy.pc
%{_libdir}/libetrophy.so

%changelog
