#
# spec file for package qperf
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


%define git_ver .0.c706363815a3

Name:           qperf
Summary:        Tool to measure socket and RDMA performance
License:        BSD-2-Clause OR GPL-2.0-only
Group:          Productivity/Networking/Diagnostic
Version:        0.4.11
Release:        0
Source:         %{name}-%{version}%{git_ver}.tar.bz2
URL:            http://github.com/linux-rdma/qperf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libibverbs-devel
BuildRequires:  librdmacm-devel
BuildRequires:  libtool

%description
qperf measures bandwidth and latency between two nodes. It can work
over TCP/IP as well as the RDMA transports.

%prep
%setup -q -n  %{name}-%{version}%{git_ver}

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
install -D -m 0755 src/qperf %{buildroot}%{_bindir}/qperf
install -D -m 0644 src/qperf.1 %{buildroot}%{_mandir}/man1/qperf.1
# As they're empty just delete them
rm -f NEWS ChangeLog

%files
%defattr(-, root, root)
%license COPYING
%_bindir/qperf
%_mandir/man1/qperf.1*

%changelog
