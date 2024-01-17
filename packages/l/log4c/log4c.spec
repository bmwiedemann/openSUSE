#
# spec file for package log4c
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           log4c
Version:        1.2.4
Release:        0
Summary:        A library of C for flexible logging to files, syslog and other destinations
License:        LGPL-2.1+
Group:          System/Libraries
Url:            http://log4c.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz-gd
BuildRequires:  libexpat-devel
BuildRequires:  pkg-config

%description
Log4c is a library of C for flexible logging to files, syslog and other
destinations. It is modeled after the Log for Java library
(http://jakarta.apache.org/log4j/), staying as close to their API as is
reasonable.

%package -n liblog4c3
Summary:        A library of C for flexible logging to files, syslog and other destinations
Group:          System/Libraries

%description -n liblog4c3
Log4c is a library of C for flexible logging to files, syslog and other
destinations. It is modeled after the Log for Java library
(http://jakarta.apache.org/log4j/), staying as close to their API as is
reasonable.

%package -n liblog4c-devel
Summary:        Development files for log4c
Group:          Development/Libraries/C and C++
Requires:       liblog4c3 = %{version}

%description -n liblog4c-devel
The liblog4c-devel package contains the static libraries and header
files needed for development with log4c.

%package -n liblog4c-doc
Summary:        Documentation for log4c
Group:          Development/Languages/C and C++
Requires:       liblog4c3 = %{version}

%description -n liblog4c-doc
The liblog4c-doc package contains the log4c documentation.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--with-pic \
	--enable-test \
 	--enable-doc \
	--enable-debug
make -j1 # parallel make is broken
# check fails on symlinks, so run before install
make %{?_smp_mflags} check

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
rm %{buildroot}%{_libdir}/liblog4c.la
rm -rf %{buildroot}%{_datadir}/doc/log4c-%{version}/
rm -rf %{buildroot}/%{_sysconfdir}

%fdupes -s %{buildroot}/%{_mandir}
%fdupes -s doc/

# make check does generate documentation twice for unknown reason and fail because of fdupes and symlinks
# moved to % build
# % check
# % {__make} check

%post -n liblog4c3 -p /sbin/ldconfig

%postun -n liblog4c3 -p /sbin/ldconfig

%files -n liblog4c3
%defattr(-,root,root)
%doc COPYING
%{_libdir}/liblog4c.so.*

%files -n liblog4c-devel
%defattr(-,root,root)
%doc ChangeLog COPYING AUTHORS README log4crc.sample
%{_bindir}/log4c-config
%{_includedir}/log4c.h
%{_includedir}/log4c
%{_libdir}/liblog4c.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/aclocal
%{_mandir}/man?/log4c*

%files -n liblog4c-doc
%defattr(-,root,root)
%doc doc/html

%changelog
