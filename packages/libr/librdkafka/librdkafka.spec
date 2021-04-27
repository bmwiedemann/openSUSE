#
# spec file for package librdkafka
#
# Copyright (c) 2021 SUSE LLC
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


# lto breaks crc32 detection in configure script
# See https://github.com/edenhill/librdkafka/issues/2426
%ifnarch x86_64
%define _lto_cflags %{nil}
%endif

%define libname %{name}1
Name:           librdkafka
Version:        1.6.1
Release:        0
Summary:        The Apache Kafka C/C++ library
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/edenhill/librdkafka
Source0:        https://github.com/edenhill/librdkafka/archive/v%{version}.tar.gz
BuildRequires:  cyrus-sasl-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
# lz4 is not in SLE12 available
%if 0%{?sle_version} >= 150000 && !0%{?is_opensuse}
BuildRequires:  liblz4-devel
%endif

%description
librdkafka is a C library implementation of the Apache Kafka protocol,
containing both Producer and Consumer support.

%package -n %{libname}
Summary:        A library for changing configuration files
Group:          System/Libraries

%description -n %{libname}
librdkafka is a C library implementation of the Apache Kafka protocol,
containing both Producer and Consumer support.

%package devel
Summary:        Development files for the Kafka C/C++ library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
librdkafka is a C library implementation of the Apache Kafka protocol,
containing both Producer and Consumer support.

This package contains development headers and examples.

%prep
%setup -q

%build
%configure --enable-ssl \
%if 0%{?sle_version} >= 150000 && !0%{?is_opensuse}
           --enable-lz4 \
%else
           --disable-lz4 \
%endif
           --enable-sasl
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install
find %{buildroot} -name '*.a' -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root,-)
%{_docdir}/../%{name}
%doc %attr(0644,root,root) %{_docdir}/../%{name}/README.md
%doc %attr(0644,root,root) %{_docdir}/../%{name}/CONFIGURATION.md
%doc %attr(0644,root,root) %{_docdir}/../%{name}/INTRODUCTION.md
%doc %attr(0644,root,root) %{_docdir}/../%{name}/STATISTICS.md
%license %attr(0644,root,root) %{_docdir}/../%{name}/LICENSE
%license %attr(0644,root,root) %{_docdir}/../%{name}/LICENSES.txt
%{_libdir}/librdkafka.so.*
%{_libdir}/librdkafka++.so.*

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/%{name}
%attr(0644,root,root) %{_includedir}/%{name}/*
%{_libdir}/librdkafka.so
%{_libdir}/librdkafka++.so
%{_libdir}/pkgconfig/rdkafka.pc
%{_libdir}/pkgconfig/rdkafka++.pc
%{_libdir}/pkgconfig/rdkafka-static.pc
%{_libdir}/pkgconfig/rdkafka++-static.pc

%changelog
