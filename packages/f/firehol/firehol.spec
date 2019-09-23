#
# spec file for package firehol
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           firehol
Version:        3.1.6
Release:        0
Summary:        Tools to build stateful firewalls and traffic shaping
License:        GPL-2.0-only
Group:          Productivity/Networking/Security
Url:            http://firehol.org/
Source:         https://github.com/firehol/firehol/releases/download/v%{version}/firehol-%{version}.tar.xz
Source99:       %{name}-rpmlintrc
BuildRequires:  curl
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  iprange
BuildRequires:  iproute2
BuildRequires:  ipset
BuildRequires:  iptables
BuildRequires:  iputils
BuildRequires:  jq
BuildRequires:  kmod-compat
BuildRequires:  less
BuildRequires:  ncurses-utils
BuildRequires:  nfacct
BuildRequires:  pkgconfig
BuildRequires:  procps
BuildRequires:  screen
BuildRequires:  tcpdump
BuildRequires:  traceroute
BuildRequires:  unzip
BuildRequires:  util-linux-systemd
BuildRequires:  wget
BuildRequires:  whois
BuildRequires:  pkgconfig(systemd)
Requires:       curl
Requires:       iprange
Requires:       iproute2
Requires:       ipset
Requires:       iptables
Requires:       iputils
Requires:       kmod-compat
Requires:       nfacct
Requires:       procps
Requires:       screen
Requires:       tcpdump
Requires:       traceroute
Requires:       util-linux-systemd
Recommends:     git-core
Recommends:     jq
Recommends:     less
Recommends:     ncurses-utils
Recommends:     unzip
Recommends:     wget
Recommends:     whois
BuildArch:      noarch

%description
FireHOL is a language (and a program to run it) which builds stateful firewalls
from human-readable configuration files.

FireQOS is a program which sets up traffic shaping from human-readable
configuration files.

Both programs abstract away the differences between IPv4 and IPv6, and rules
for each protocol can be applied as needed.

%package doc
Summary:        FireHOL documentation
Group:          Documentation/Other
BuildArch:      noarch

%description doc
Contains documentation and configuration examples for FireHOL.


%prep
%setup -q

%build
%configure --docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
%make_install
install -d %{buildroot}%{_unitdir}

cp %{buildroot}%{_docdir}/%{name}/contrib/*.service %{buildroot}%{_unitdir}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcfirehol
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcfireqos

chmod -Rv o= %{buildroot}%{_sysconfdir}/firehol/

%fdupes -s %{buildroot}%{_mandir}

%pre
%service_add_pre firehol.service fireqos.service

%preun
%service_del_preun firehol.service fireqos.service

%post
%service_add_post firehol.service fireqos.service

%postun
%service_del_postun firehol.service fireqos.service

%files
%config(noreplace) %{_sysconfdir}/firehol/
%{_sbindir}/firehol
%{_sbindir}/fireqos
%{_sbindir}/link-balancer
%{_sbindir}/update-ipsets
%{_sbindir}/vnetbuild
%{_libexecdir}/firehol/
%{_datadir}/update-ipsets/
%{_sbindir}/rcfirehol
%{_sbindir}/rcfireqos
%{_unitdir}/fire*service

%files doc
%doc ChangeLog README THANKS
%license COPYING
%{_docdir}/%{name}
%{_mandir}/man1/firehol.1%{ext_man}
%{_mandir}/man1/fireqos.1%{ext_man}
%{_mandir}/man1/vnetbuild.1%{ext_man}
%{_mandir}/man5/firehol*.5%{ext_man}
%{_mandir}/man5/fireqos*.5%{ext_man}
%{_mandir}/man5/vnetbuild*.5%{ext_man}

%changelog
