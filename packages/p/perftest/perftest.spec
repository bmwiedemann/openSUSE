#
# spec file for package perftest
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


%define extra_version -0.29
Name:           perftest
Version:        4.4
Release:        0
Summary:        IB Performance tests
License:        BSD-3-Clause OR GPL-2.0-or-later
Group:          Productivity/Networking/Diagnostic
URL:            https://github.com/linux-rdma/perftest
Source0:        %{name}-%{version}%{extra_version}.tar.gz
Patch4:         perftest-armv6.patch
# For transition to rdma-core make sure the new packages are selected
# Once the transition is made the version check can be removed
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libibumad-devel
BuildRequires:  libibverbs-devel
BuildRequires:  librdmacm-devel
BuildRequires:  libtool

%description
gen2 uverbs microbenchmarks

%prep
%setup -q -n %{name}-%{version}%{extra_version}
%patch4 -p1

%build
./autogen.sh
%configure
%make_build
chmod -x runme

%install
%make_install

%files
%doc README runme
%license COPYING
%{_bindir}/ib_atomic_lat
%{_bindir}/ib_atomic_bw
%{_bindir}/ib_write_lat
%{_bindir}/ib_write_bw
%{_bindir}/ib_send_lat
%{_bindir}/ib_send_bw
%{_bindir}/ib_read_lat
%{_bindir}/ib_read_bw
%{_bindir}/raw_ethernet_burst_lat
%{_bindir}/raw_ethernet_bw
%{_bindir}/raw_ethernet_fs_rate
%{_bindir}/raw_ethernet_lat
%{_bindir}/run_perftest_loopback
%{_bindir}/run_perftest_multi_devices

%changelog
