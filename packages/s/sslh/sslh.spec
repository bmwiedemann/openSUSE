#
# spec file for package sslh
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2012 by Lars Vogdt
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


Name:           sslh
Version:        2.1.4
Release:        0
Summary:        SSL/SSH multiplexer
License:        GPL-2.0-or-later
Group:          Productivity/Networking/SSH
URL:            https://www.rutschle.net/tech/sslh.shtml
Source:         https://github.com/yrutschle/sslh/archive/refs/tags/v%{version}.tar.gz
Source1:        %{name}.init
Source2:        %{name}.sysconfig
Source3:        %{name}.conf.d
BuildRequires:  autoconf
BuildRequires:  libcap-devel
BuildRequires:  libconfig-devel
BuildRequires:  libev-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libsystemd)
Requires:       openssh
Requires:       openssl
Requires(pre):  group(nobody)
%systemd_requires

%description
sslh lets one accept both HTTPS and SSH connections on the same port. It makes
it possible to connect to an SSH server on port 443 (e.g. from inside a
corporate firewall) while still serving HTTPS on that port.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure
export CFLAGS="%{optflags}"
%make_build PREFIX=%{_prefix}

%install
make PREFIX=%{_prefix} DESTDIR=%{buildroot} install

install -Dm644 scripts/systemd.sslh@.service %{buildroot}%{_unitdir}/%{name}@.service
install -Dm644 scripts/systemd.sslh-select@.service %{buildroot}%{_unitdir}/%{name}-select@.service
install -Dm644 %{SOURCE3} %{buildroot}%{_sysconfdir}/conf.d/%{name}
ln -sf %{_sbindir}/service %{buildroot}/%{_sbindir}/rc%{name}

# install default configuration
mkdir -p %{buildroot}%{_sysconfdir}/default
cp scripts/etc.sysconfig.%{name} %{buildroot}%{_sysconfdir}/default/%{name}

%pre
getent passwd sslh || useradd  -r -g nogroup -s /bin/false -c "User for SSLH" -d %{_localstatedir}/lib/empty sslh
%service_add_pre sslh.service

%post
%service_add_post sslh.service

%preun
%service_del_preun sslh.service

%postun
%service_del_postun sslh.service

%files
%doc ChangeLog README.md
%{_sbindir}/%{name}
%{_sbindir}/rc%{name}
%{_unitdir}/%{name}@.service
%{_unitdir}/%{name}-select@.service
%dir %{_sysconfdir}/conf.d
%config(noreplace) %{_sysconfdir}/conf.d/%{name}
%config(noreplace) %{_sysconfdir}/default/%{name}
%{_mandir}/man8/%{name}.8%{?ext_man}

%changelog
