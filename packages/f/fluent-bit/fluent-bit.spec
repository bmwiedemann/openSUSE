#
# spec file for package fluent-bit
#
# Copyright (c) 2020 SUSE LLC
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


Name:           fluent-bit
Version:        1.5.6
Release:        0
Summary:        Fast Log Processor and Forwarder
License:        Apache-2.0
URL:            https://github.com/fluent/fluent-bit
Source:         https://github.com/fluent/fluent-bit/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  cyrus-sasl-devel
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gtest
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(libsystemd)

%description
Fluent Bit is a fast Log Processor and Forwarder. Its part of the Fluentd Ecosystem and a CNCF sub-project.
Fluent Bit allows to collect log events or metrics from different sources, process them and deliver them to different backends such as Fluentd, Elasticsearch, NATS, InfluxDB or any custom HTTP end-point within others.
In addition, Fluent Bit comes with full Stream Processing capabilities: data manipulation and analytics using SQL queries.

%package devel
Summary:        Devel files for Fluent Bit

%description devel
Devel files for Fluent Bit

%prep
%setup -q

%build
%cmake -Wno-dev \
          -DBUILD_SHARED_LIBS=OFF \
          -DFLB_DEBUG=Off \
          -DFLB_TRACE=Off \
          -DFLB_JEMALLOC=On \
          -DFLB_TLS=On \
          -DFLB_SHARED_LIB=Off \
          -DFLB_EXAMPLES=Off \
          -DFLB_HTTP_SERVER=On \
          -DFLB_IN_SYSTEMD=On \
          -DFLB_OUT_KAFKA=On
%cmake_build

%install
%cmake_install
install -m 644 conf/parsers_*.conf %{buildroot}%{_prefix}%{_sysconfdir}/fluent-bit

%files
%license LICENSE
%{_bindir}/fluent-bit
%dir %{_prefix}%{_sysconfdir}/fluent-bit
%{_prefix}%{_sysconfdir}/fluent-bit/fluent-bit.conf
%{_prefix}%{_sysconfdir}/fluent-bit/parsers.conf
%{_prefix}%{_sysconfdir}/fluent-bit/plugins.conf
%{_prefix}%{_sysconfdir}/fluent-bit/parsers_ambassador.conf
%{_prefix}%{_sysconfdir}/fluent-bit/parsers_cinder.conf
%{_prefix}%{_sysconfdir}/fluent-bit/parsers_extra.conf
%{_prefix}%{_sysconfdir}/fluent-bit/parsers_java.conf
%{_prefix}%{_sysconfdir}/fluent-bit/parsers_openstack.conf

%files devel
%{_includedir}/fluent-bit.h
%{_includedir}/fluent-bit/

%changelog
