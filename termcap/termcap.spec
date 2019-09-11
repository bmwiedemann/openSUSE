#
# spec file for package termcap
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           termcap
# bug437293
%ifarch ppc64
Obsoletes:      termcap-64bit
%endif
#
Version:        2.0.8
Release:        0
Summary:        The Termcap Library
License:        LGPL-2.1-or-later
Group:          System/Libraries
Source:         termcap-2.0.8.tar.gz
Source1:        curses-bsd4.4.tar.gz
Source2:        baselibs.conf
Patch:          termcap-2.0.8.dif
Patch1:         curses-bsd4.4-linux.patch
Patch2:         termcap-2.0.8-setuid.patch
Patch3:         termcap-2.0.8-fix-tc.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The termcap library.

%prep
%setup -q -b 1
%patch  -p0
%patch2 -p1 -b .setuid
%patch3 -p1 -b .tc
cd ../curses-bsd4.4
%patch1 -p0

%build
mkdir termcap
ln -sf ../termcap.h termcap/
make -j1 lib=%{_lib} CC="%{__cc}"
cd ../curses-bsd4.4
make -j1 lib=%{_lib} CC="%{__cc}"

%install
mkdir -p ${RPM_BUILD_ROOT}/usr/%{_lib}
mkdir -p ${RPM_BUILD_ROOT}/usr/include
make install prefix=${RPM_BUILD_ROOT}/usr lib=%{_lib}
cd ../curses-bsd4.4
make install prefix=${RPM_BUILD_ROOT}/usr lib=%{_lib}

%clean
test -z "${RPM_BUILD_ROOT}" || rm -rf "${RPM_BUILD_ROOT}"

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%dir /usr/include/curses
%dir /usr/%{_lib}/curses
/usr/include/curses/curses.h
/usr/%{_lib}/curses/libcurses.a
/usr/%{_lib}/curses/libcurses.so
/usr/%{_lib}/libcurses.so.1
/usr/%{_lib}/libcurses.so.1.0.0
%dir /usr/include/termcap
%dir /usr/%{_lib}/termcap
/usr/include/termcap/termcap.h
/usr/%{_lib}/libtermcap.so.2
/usr/%{_lib}/libtermcap.so.2.0.8
/usr/%{_lib}/termcap/libtermcap.a
/usr/%{_lib}/termcap/libtermcap.so

%changelog
