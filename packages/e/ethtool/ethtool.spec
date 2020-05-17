#
# spec file for package ethtool
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


Name:           ethtool
Version:        5.6
Release:        0
Summary:        Utility for examining and tuning Ethernet-based network interfaces
License:        GPL-2.0-only
Group:          Productivity/Networking/Diagnostic
URL:            https://www.kernel.org/pub/software/network/ethtool/

#Git-Clone:	git://git.kernel.org/pub/scm/network/ethtool/ethtool
Source:         https://www.kernel.org/pub/software/network/ethtool/%{name}-%{version}.tar.xz
Source2:        https://www.kernel.org/pub/software/network/ethtool/%{name}-%{version}.tar.sign
Source3:        %{name}.keyring
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(libmnl)

Patch1:         netlink-fix-build-warnings.patch
Patch2:         netlink-show-netlink-error-even-without-extack.patch
Patch3:         features-accept-long-legacy-flag-names-when-setting-.patch
Patch4:         refactor-interface-between-ioctl-and-netlink-code.patch
Patch5:         netlink-use-genetlink-ops-information-to-decide-abou.patch

%description
Ethtool is a small utility for examining and tuning ethernet-based
network interfaces.  See the man page for more details.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
export CFLAGS="%optflags -W -Wall -Wstrict-prototypes -Wformat-security -Wpointer-arith -Wno-missing-field-initializers"
%configure
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"

%files
%defattr(-,root,root)
%{_sbindir}/ethtool
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/ethtool
%{_mandir}/man8/ethtool.8*
%if (0%{?suse_version} >= 1500) || (0%{?sle_version} >= 120300)
%license COPYING
%else
%doc COPYING
%endif
%doc AUTHORS NEWS

%changelog
