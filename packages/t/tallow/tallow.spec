#
# spec file for package tallow
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


Name:           tallow
Version:        21+git20200401.03f4d64
Release:        0
Summary:        Temporary IP address ban issuance daemon
License:        GPL-3.0-or-later
URL:            https://github.com/clearlinux/tallow
Source:         tallow-%{version}.tar.xz
Source1:        tallow-man-pages.tar.gz
Patch:          fwcmd_path.patch
Patch1:         no-pandoc.patch
Requires:       ipset
Requires:       iptables
#For systemd macros:
PreReq:         /usr/bin/mkdir /usr/bin/rm /usr/bin/touch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libjson-c-devel
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libsystemd)

%description
Tallow is a fail2ban/lard replacement that uses systemd's native
journal API to scan for attempted SSH logins, and issues temporary IP
address bans for clients that violate certain login patterns.

This is not a security application! Tallow is meant to reduce log
clutter and system resource usage at the cost of denying access to
potentially valid users.

%prep
%setup -qa1
%patch -p1
%patch1 -p1

%build
./autogen.sh
%configure
export LANG=en_US.UTF-8
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_sysconfdir}
touch %{buildroot}%{_sysconfdir}/tallow.conf
rm -rf %{buildroot}%{_datadir}/doc/tallow
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system
install -m 644 data/tallow.service %{buildroot}%{_prefix}/lib/systemd/system/
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rctallow
# For customer provided *.json files:
mkdir -p %{buildroot}%{_sysconfdir}/tallow

%pre
%service_add_pre tallow.service

%post
%service_add_post tallow.service

%preun
%service_del_preun tallow.service

%postun
%service_del_postun tallow.service

%files
%license COPYING
%doc README.md tallow.conf
%dir %{_sysconfdir}/tallow
%{_sbindir}/tallow
%{_sbindir}/rctallow
%{_prefix}/lib/systemd/system/tallow.service
%{_mandir}/man1/tallow.1%{?ext_man}
%{_mandir}/man5/tallow.conf.5%{?ext_man}
%{_mandir}/man5/tallow.patterns.5%{?ext_man}
%dir %{_datadir}/tallow
%{_datadir}/tallow/sshd.json
%ghost %{_sysconfdir}/tallow.conf

%changelog
