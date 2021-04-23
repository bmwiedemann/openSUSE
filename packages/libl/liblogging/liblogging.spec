#
# spec file for package liblogging
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


%define with_systemd_journal 0%{?suse_version} >= 1310
%define with_rst2man 0%{?suse_version} >= 1230
%define sover 0
Name:           liblogging
Version:        1.0.6
Release:        0
Summary:        An easy to use logging library
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
Url:            http://www.liblogging.org/
Source0:        http://download.rsyslog.com/liblogging/%{name}-%{version}.tar.gz
BuildRequires:  dos2unix
BuildRequires:  pkgconfig >= 0.9.0
%if %{with_rst2man}
%if 0%{?is_opensuse}
BuildRequires:  python3-docutils
%else
BuildRequires:  python-docutils
%endif
%endif
%if %{with_systemd_journal}
%if 0%{?suse_version} == 1310
BuildRequires:  pkgconfig(libsystemd-journal) >= 197
%else
BuildRequires:  pkgconfig(libsystemd) >= 209
%endif
%endif

%description
Liblogging is an easy to use logging library.

It contains the Libstdlog component is used for standard logging
(syslog replacement) purposes via multiple channels.

%package -n %{name}%{sover}
Summary:        An easy to use logging library
Group:          System/Libraries

%description -n %{name}%{sover}
Liblogging is an easy to use logging library.

It contains the Libstdlog component is used for standard logging
(syslog replacement) purposes via multiple channels.

%package devel
Summary:        Development files for LibLogging stdlog library
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}-%{release}

%description devel
The liblogging-devel package includes header files, libraries necessary for
developing programs which use liblogging library.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--enable-rfc3195 \
%if %{with_systemd_journal}
	--enable-journal \
%else
	--disable-journal \
%endif
%if %{with_rst2man}
	--disable-cached-man-pages \
%else
	--enable-cached-man-pages \
%endif

make %{?_smp_mflags:%{?_smp_mflags}} V=1
dos2unix AUTHORS ChangeLog COPYING README

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm -v rfc3195/doc/html/Makefile*

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%defattr(-,root,root)
%license COPYING
%{_libdir}/liblogging-rfc3195.so.*
%{_libdir}/liblogging-stdlog.so.*
%{_bindir}/stdlogctl
%{_mandir}/man1/stdlogctl*

%files devel
%defattr(-,root,root)
%license COPYING
%doc ChangeLog README
%doc rfc3195/doc/html
%{_libdir}/liblogging-rfc3195.so
%{_libdir}/liblogging-stdlog.so
%dir %{_includedir}/%{name}
%{_includedir}/liblogging/*.h
%{_libdir}/pkgconfig/liblogging-rfc3195.pc
%{_libdir}/pkgconfig/liblogging-stdlog.pc
%{_mandir}/man3/stdlog*

%changelog
