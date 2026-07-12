#
# spec file for package ethtool
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


Name:           ethtool
Version:        7.1
Release:        0
Summary:        Utility for examining and tuning Ethernet-based network interfaces
License:        GPL-2.0-only
Group:          Productivity/Networking/Diagnostic
URL:            https://www.kernel.org/pub/software/network/ethtool/

#Git-Clone:	git://git.kernel.org/pub/scm/network/ethtool/ethtool
Source:         https://www.kernel.org/pub/software/network/ethtool/%{name}-%{version}.tar.xz
Source2:        https://www.kernel.org/pub/software/network/ethtool/%{name}-%{version}.tar.sign
Source3:        %{name}.keyring
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  pkgconfig(libmnl)
Obsoletes:      %{name}-bash-completion < %{version}-%{release}
Provides:       %{name}-bash-completion = %{version}-%{release}

%description
Ethtool is a small utility for examining and tuning ethernet-based
network interfaces.  See the man page for more details.

%prep
%autosetup -p1

%build
export CFLAGS="%optflags -Wall -Wextra -Wstrict-prototypes -Wformat-security -Wpointer-arith"
%configure
%make_build

%install
%make_install

%files
%{_sbindir}/ethtool
%{_mandir}/man8/ethtool.8*
%{_datadir}/metainfo/org.kernel.software.network.ethtool.metainfo.xml
%if (0%{?suse_version} >= 1500) || (0%{?sle_version} >= 120300)
%license COPYING
%else
%doc COPYING
%endif
%doc AUTHORS NEWS
%{_datadir}/bash-completion/

%changelog
