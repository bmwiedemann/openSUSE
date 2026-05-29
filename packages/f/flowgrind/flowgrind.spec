#
# spec file for package flowgrind
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           flowgrind
Version:        0.8.2
Release:        0
Summary:        Network performance measurement
License:        GPL-2.0-only
URL:            https://flowgrind.github.io
Source0:        https://github.com/flowgrind/flowgrind/releases/download/flowgrind-%{version}/flowgrind-%{version}.tar.bz2
Source1:        https://github.com/flowgrind/flowgrind/releases/download/flowgrind-%{version}/flowgrind-%{version}.tar.bz2.asc
BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  xmlrpc-c-devel
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(uuid)

%description
Flowgrind is a tool similar to iperf, netperf to measure throughput and other
metrics for TCP and other protocols. It features some unique characteristics
which are of use when exploring the idiosyncrasies of wireless mesh networks.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/flowgrind*
%{_sbindir}/flowgrindd
%{_mandir}/man1/flowgrind*

%changelog
