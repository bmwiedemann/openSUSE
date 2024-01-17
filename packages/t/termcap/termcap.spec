#
# spec file for package termcap
#
# Copyright (c) 2023 SUSE LLC
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


%define libcurses libcurses1
%define libtermcap libtermcap2

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
Patch0:         termcap-2.0.8.dif
Patch1:         curses-bsd4.4-linux.patch
Patch2:         termcap-2.0.8-setuid.patch
Patch3:         termcap-2.0.8-fix-tc.patch

%description
The termcap and curses libraries.

%package -n %libcurses
Summary:        Library for old curses
Group:          System/Libraries
Version:        1.0.0
Provides:       termcap:%{_libdir}/libcurses.so.1.0.0
Obsoletes:      termcap <= 2.0.8

%description -n %libcurses
This library of old curses

%package -n %libtermcap
Summary:        Library for old termcap
Group:          System/Libraries
Version:        2.0.8
Provides:       termcap:%{_libdir}/libtermcap.so.2.0.8
Obsoletes:      termcap <= 2.0.8

%description -n %libtermcap
This library of old termcap

%package devel
Summary:        Development files for termcap
Group:          Development/Libraries/C and C++
Provides:       termcap:%{_includedir}/curses/curses.h
Requires:       %libcurses = 1.0.0
Requires:       %libtermcap = 2.0.8

%description devel
This package contains all necessary include files
and libraries needed to build termcap based applications.

%package devel-static
Summary:        Development files for termcap
Group:          Development/Libraries/C and C++
Provides:       termcap:%{_libdir}/termcap/libtermcap.a
Requires:       %{name}-devel

%description devel-static
This package contains all necessary include files
and libraries needed to build termcap based applications.

%prep
%setup -q -b 1
%patch0 -p0
%patch2 -p1 -b .setuid
%patch3 -p1 -b .tc
cd ../curses-bsd4.4
%patch1 -p0

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
mkdir termcap
ln -sf ../termcap.h termcap/
make -j1 lib=%{_lib} CC="%{__cc}"
cd ../curses-bsd4.4
make -j1 lib=%{_lib} CC="%{__cc}"

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
make install prefix=%{buildroot}%{_prefix} lib=%{_lib}
cd ../curses-bsd4.4
make install prefix=%{buildroot}%{_prefix} lib=%{_lib}
find %{buildroot} \( -name '*.h' -o -name '*.a' \) -exec chmod 644 '{}' \+

%post -n %libcurses -p /sbin/ldconfig
%postun -n %libcurses -p /sbin/ldconfig

%post -n %libtermcap -p /sbin/ldconfig
%postun -n %libtermcap -p /sbin/ldconfig

%files -n %libcurses
%{_libdir}/libcurses.so.1
%{_libdir}/libcurses.so.1.0.0

%files -n %libtermcap
%{_libdir}/libtermcap.so.2
%{_libdir}/libtermcap.so.2.0.8

%files devel
%dir %{_includedir}/curses
%dir %{_includedir}/termcap
%dir %{_libdir}/curses
%dir %{_libdir}/termcap
%{_includedir}/curses/curses.h
%{_includedir}/termcap/termcap.h
%{_libdir}/curses/libcurses.so
%{_libdir}/termcap/libtermcap.so

%files devel-static
%{_libdir}/curses/libcurses.a
%{_libdir}/termcap/libtermcap.a

%changelog
