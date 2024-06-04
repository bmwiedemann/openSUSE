#
# spec file for package ethtool
#
# Copyright (c) 2024 SUSE LLC
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
Version:        6.9
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

%description
Ethtool is a small utility for examining and tuning ethernet-based
network interfaces.  See the man page for more details.

%package bash-completion
Summary:        Bash completion for ethtool
Group:          System/Shells
Requires:       %{name}
Requires:       bash-completion
%if 0%{?suse_version} >= 1500
Supplements:    (%{name} and bash-completion)
%else
Supplements:    packageand(%{name}:bash-completion)
%endif
BuildArch:      noarch

%description bash-completion
bash command line completion support for ethtool.

%prep
%setup -q

%build
export CFLAGS="%optflags -Wall -Wextra -Wstrict-prototypes -Wformat-security -Wpointer-arith"
%configure
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"

%files
%defattr(-,root,root)
%{_sbindir}/ethtool
%{_mandir}/man8/ethtool.8*
%if (0%{?suse_version} >= 1500) || (0%{?sle_version} >= 120300)
%license COPYING
%else
%doc COPYING
%endif
%doc AUTHORS NEWS

%files bash-completion
%defattr(-,root,root)
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/ethtool

%changelog
