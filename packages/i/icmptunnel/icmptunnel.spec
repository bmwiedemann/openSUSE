#
# spec file for package icmptunnel
#
# Copyright (c) 2022 SUSE LLC
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           icmptunnel
Version:        1.0.0
Release:        0
Summary:        A tunnel for wrapping IP traffic in ICMP
License:        MIT
Group:          Productivity/Networking/Security
URL:            https://dhavalkapil.com/icmptunnel/
Source:         https://github.com/DhavalKapil/icmptunnel/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         icmptunnel-obey-cflags.patch

%description
This program transparently tunnels IP traffic through ICMP echo and reply packets.

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="%{optflags}"
%make_build

%install
install -D -m 0755 icmptunnel %{buildroot}%{_bindir}/icmptunnel

%files
%doc README.md
%doc client.sh server.sh
%{_bindir}/icmptunnel

%changelog
