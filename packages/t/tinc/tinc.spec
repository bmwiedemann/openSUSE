#
# spec file for package tinc
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


Name:           tinc
Version:        1.0.37
Release:        0
Summary:        A virtual private network daemon
License:        GPL-2.0-or-later
URL:            http://www.tinc-vpn.org
Source0:        %{url}/packages/%{name}-%{version}.tar.gz
Source1:        %{url}/packages/%{name}-%{version}.tar.gz.sig
Source2:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xd62bdd168efbe48bc60e8e234a6084b9c0d71f4a#/%{name}.keyring
Source3:        %{name}.service
Source4:        %{name}@.service
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)
%systemd_ordering

%description
tinc is a Virtual Private Network (VPN) daemon that uses tunnelling
and encryption to create a secure private network between hosts on
the Internet. Because the tunnel appears to the IP level network
code as a normal network device, there is no need to adapt any
existing software. This tunnelling allows VPN sites to share
information with each other over the Internet without exposing any
information to others.

%prep
%autosetup -p1

%build
%configure --with-systemd=%{_unitdir}
%make_build

%install
%make_install

#install our own service files
install -Dpm0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
install -Dpm0644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}@.service

#don't ship info file
rm %{buildroot}%{_infodir}/%{name}.info

%pre
%service_add_pre %{name}.service %{name}@.service

%post
%service_add_post %{name}.service %{name}@.service

%preun
%service_del_preun %{name}.service %{name}@.service

%postun
%service_del_postun %{name}.service %{name}@.service

%files
%license COPYING COPYING.README
%doc AUTHORS NEWS README THANKS doc/sample* doc/*.tex
%{_mandir}/man?/%{name}.conf.?%{?ext_man}
%{_mandir}/man?/%{name}d.?%{?ext_man}
%{_sbindir}/%{name}d
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}@.service

%changelog
