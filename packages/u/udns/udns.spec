#
# spec file for package udns
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


Name:           udns
Version:        0.4
Release:        0
Summary:        DNS resolver tools
License:        LGPL-2.1
Group:          Productivity/Networking/DNS/Utilities
Url:            http://www.corpit.ru/mjt/udns.html
Source:         http://www.corpit.ru/mjt/udns/udns-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
UDNS is a stub DNS resolver library with ability to perform both
synchronous and asynchronous DNS queries.

%package -n libudns0
Summary:        DNS resolver library
Group:          System/Libraries

%description -n libudns0
UDNS is a stub DNS resolver library with ability to perform both
synchronous and asynchronous DNS queries.

%package devel
Summary:        Development files for libudns
Group:          Development/Libraries/C and C++
Requires:       libudns0 = %{version}

%description devel
UDNS is a stub DNS resolver library with ability to perform both
synchronous and asynchronous DNS queries.

This package contains header files and documentation needed for writing
or compiling programs that use UDNS.

%prep
%setup -q

%build
./configure --enable-ipv6
make %{?_smp_mflags} shared

%install
mkdir -p %{buildroot}{%{_libdir},%{_includedir},%{_bindir},%{_mandir}/man{1,3}}
install -m755 libudns.so.0 %{buildroot}%{_libdir}
ln -s libudns.so.0 %{buildroot}%{_libdir}/libudns.so
install -m644 udns.h %{buildroot}%{_includedir}
for f in *_s; do install -m 755 $f %{buildroot}%{_bindir}/${f%%_s}; done
for f in *.[13]; do install -m644 $f %{buildroot}%{_mandir}/man${f#*.}; done

%post -n libudns0 -p /sbin/ldconfig
%postun -n libudns0 -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING.LGPL NEWS NOTES TODO
%{_bindir}/dnsget
%{_bindir}/rblcheck
%{_bindir}/ex-rdns
%{_mandir}/man1/dnsget.1%{ext_man}
%{_mandir}/man1/rblcheck.1%{ext_man}

%files -n libudns0
%defattr(-,root,root,-)
%{_libdir}/libudns.so.0

%files devel
%defattr(-,root,root,-)
%{_libdir}/libudns.so
%{_includedir}/udns.h
%{_mandir}/man3/udns.3%{ext_man}

%changelog
