#
# spec file for package iperf2
#
# Copyright (c) 2025 SUSE LLC
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


Name:           iperf2
Version:        2.2.1
Release:        0
Summary:        Network throughput and latency measurement tool
License:        NCSA
URL:            https://sourceforge.net/projects/iperf2/
Source:         https://downloads.sourceforge.net/project/iperf2/iperf-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  make

%description
Iperf here is a means of measuring networks - capacity & latency (including
dual queue L4S) over sockets both TCP and UDP.

%prep
%autosetup -n iperf-%{version}

%build
%configure
%make_build

%install
%make_install


%files
%license COPYING
%doc doc/RELEASE_NOTES
%{_bindir}/iperf
%{_mandir}/man1/iperf*

%changelog

