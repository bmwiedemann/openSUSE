#
# spec file for package dropwatch
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


Name:           dropwatch
Version:        1.5.3
Release:        0
Summary:        Kernel dropped packet monitor
License:        GPL-2.0-only
Group:          Productivity/Networking/Diagnostic
URL:            https://github.com/nhorman/dropwatch
Source:         https://github.com/nhorman/dropwatch/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  binutils-devel
BuildRequires:  libnl3-devel
BuildRequires:  libpcap-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  readline-devel

%description
dropwatch is an interactive utility for monitoring and recording packets that
are dropped by the kernel

%prep
%setup -q
./autogen.sh
%configure

%build
export CFLAGS="%{optflags}"
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1

install -m0755 src/dropwatch %{buildroot}%{_bindir}
install -m0755 src/dwdump %{buildroot}%{_bindir}

install -m0644 doc/dropwatch.1 %{buildroot}%{_mandir}/man1
install -m0644 doc/dwdump.1 %{buildroot}%{_mandir}/man1

%files
%{_bindir}/dropwatch
%{_bindir}/dwdump
%{_mandir}/man1/dropwatch.1%{?ext_man}
%{_mandir}/man1/dwdump.1%{?ext_man}
%doc README.md
%license COPYING

%changelog
