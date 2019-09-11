#
# spec file for package tslib
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Guillaume GARDET <guillaume@opensuse.org>
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


Name:           tslib
Version:        1.16
Release:        0
Summary:        Abstraction layer for touchscreen
License:        LGPL-2.1-or-later AND GPL-2.0-only
Group:          Hardware/Other
Url:            https://github.com/kergoth/tslib.git
#Git-Clone:	git://github.com/kergoth/tslib
Source0:        https://github.com/kergoth/tslib/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/kergoth/tslib/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Source3:        baselibs.conf
BuildRequires:  fdupes
BuildRequires:  pkgconfig

%description
Tslib is an abstraction layer for touchscreen panel events.

The idea of tslib is to have a core library and a set of plugins to
manage the conversion and filtering as needed.

%package -n libts0
Summary:        Abstraction layer for touchscreens
Group:          System/Libraries

%description -n libts0
Tslib is an abstraction layer for touchscreen panel events.

The idea of tslib is to have a core library and a set of plugins to
manage the conversion and filtering as needed.

%package plugins
Summary:        Driver plugins for tslib, an abstraction layer for touchscreens
Group:          Hardware/Other

%description plugins
Tslib is an abstraction layer for touchscreen panel events.

The idea of tslib is to have a core library and a set of plugins to
manage the conversion and filtering as needed.

This subpackage contains the hardware driver plugins for tslib.

%package devel
Summary:        Development files for tslib, a touchscreen panel event layer
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       %{name}-plugins = %{version}
Requires:       glibc-devel

%description devel
Devel package for tslib. Tslib is an abstraction layer for touchscreen panel events.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
%fdupes %{buildroot}/%{_mandir}

%post -n libts0 -p /sbin/ldconfig
%postun -n libts0 -p /sbin/ldconfig

%files devel
%defattr(-,root,root)
%dir %{_libdir}/ts
%{_includedir}/tslib.h
%{_libdir}/libts.la
%{_libdir}/pkgconfig/tslib.pc
%dir %{_libdir}/ts
%{_libdir}/ts/*.la
%{_libdir}/libts.so

%files -n libts0
%defattr(-,root,root)
%{_libdir}/libts.so.0*

%files plugins
%defattr(-,root,root)
%dir %{_libdir}/ts
%{_libdir}/ts/*.so

%files
%defattr(-,root,root)
%config %{_sysconfdir}/ts.conf
%{_bindir}/ts_calibrate
%{_bindir}/ts_finddev
%{_bindir}/ts_harvest
%{_bindir}/ts_print
%{_bindir}/ts_print_mt
%{_bindir}/ts_print_raw
%{_bindir}/ts_test
%{_bindir}/ts_test_mt
%{_bindir}/ts_uinput
%{_bindir}/ts_verify
%{_mandir}/*/*

%changelog
