#
# spec file for package icmptunnel
#
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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


%define realver 1.0.0-alpha
Name:           icmptunnel
Version:        1.0.0~alpha
Release:        0
Summary:        A tunnel for wrapping IP traffic in ICMP
License:        MIT
Group:          Productivity/Networking/Security
URL:            https://dhavalkapil.com/icmptunnel/
Source:         https://github.com/DhavalKapil/icmptunnel/archive/%{realver}.tar.gz#/%{name}-%{realver}.tar.gz
Patch0:         0001-Typo-fix.patch
Patch1:         0002-Change-the-MTU-size-of-tunnel-23.patch
Patch2:         0003-Free-the-unfree-heap.patch
Patch3:         icmptunnel-obey-cflags.patch

%description
This program transparently tunnels IP traffic through ICMP echo and reply packets.

%prep
%setup -q -n %{name}-%{realver}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
install -D -m 0755 icmptunnel %{buildroot}%{_bindir}/icmptunnel

%files
%doc README.md
%doc client.sh server.sh
%{_bindir}/icmptunnel

%changelog
