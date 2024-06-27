#
# spec file for package Radicale
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2012-2024 Ákos Szőts <szotsaki@gmail.com>
# Copyright (c) 2011 Marcus Rueckert <darix@opensu.se>
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


%define pkg_name       radicale
%define pkg_config     %{_sysconfdir}/%{pkg_name}
%define pkg_home       %{_localstatedir}/lib/%{pkg_name}
%define pkg_user_group %{pkg_name}
%define py_min_ver 3.8
%define vo_min_ver 0.9.6
%define du_min_ver 2.7.3
%define pk_min_ver 1.1.0
Name:           Radicale
Version:        3.2.2
Release:        0
Summary:        A CalDAV calendar and CardDav contact server
License:        GPL-3.0-or-later
Group:          Productivity/Office/Other
URL:            https://www.radicale.org/
Source:         https://github.com/Kozea/Radicale/archive/v%{version}.tar.gz
Source1:        radicale.service
Source2:        system-user-%{pkg_user_group}.conf
Source3:        radicale.firewalld
Source4:        %{name}.rpmlintrc
BuildRequires:  fdupes
BuildRequires:  firewall-macros
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-defusedxml
BuildRequires:  python3-passlib
BuildRequires:  python3-pika >= %{pk_min_ver}
BuildRequires:  python3-python-dateutil >= %{du_min_ver}
BuildRequires:  python3-setuptools
BuildRequires:  python3-vobject >= %{vo_min_ver}
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(python3) >= %{py_min_ver}
Requires:       python3 >= %{py_min_ver}
Requires:       python3-defusedxml
Requires:       python3-passlib
Requires:       python3-pika >= %{pk_min_ver}
Requires:       python3-python-dateutil >= %{du_min_ver}
Requires:       python3-vobject >= %{vo_min_ver}
Recommends:     apache2-utils
Recommends:     python3-bcrypt
Recommends:     python3-systemd
BuildArch:      noarch
%sysusers_requires

%description
Radicale is a server for CalDAV (calendars, to-do lists) and CardDAV (contacts).

* Shares calendars and contact lists through CalDAV, CardDAV and HTTP.
* Supports events, todos, journal entries and business cards.
* Works out-of-the-box, no setup or configuration required.
* Can limit access by authentication.
* Can secure connections with TLS.
* Works with many CalDAV and CardDAV clients.
* Stores all data on the file system in a directory structure.
* Can be extended with plugins.

%prep
%autosetup

%build
%python3_build
%sysusers_generate_pre %{SOURCE2} %{pkg_user_group} system-user-%{pkg_user_group}.conf

%install
%python3_install
install -m 0750 -d %{buildroot}%{pkg_config}/ %{buildroot}%{pkg_home}/
install -m 0640 config %{buildroot}%{pkg_config}/config
install -m 0755 -d %{buildroot}%{_sbindir}/
install -D -m 444 %{SOURCE1} %{buildroot}%{_unitdir}/%{pkg_name}.service
install -D -m 644 %{SOURCE3} %{buildroot}%{_prefix}/lib/firewalld/services/%{pkg_name}.xml

ln -sfv %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{pkg_name}

mkdir %{buildroot}%{pkg_home}/collections
%fdupes %{buildroot}%{python3_sitelib}

mkdir -p %{buildroot}%{_sysusersdir}
install -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/

%pre -f %{pkg_user_group}.pre
%service_add_pre %{pkg_name}.service

%post
test -e %{pkg_config}/rights || touch %{pkg_config}/rights
test -e %{pkg_config}/users  || touch %{pkg_config}/users
%service_add_post %{pkg_name}.service
%firewalld_reload

%preun
%service_del_preun %{pkg_name}.service

%postun
%service_del_postun %{pkg_name}.service

%files
%license COPYING.md
%doc CHANGELOG.md DOCUMENTATION.md README.md
%{_bindir}/%{pkg_name}
%{python3_sitelib}/%{name}-%{version}-py*.egg-info
%{python3_sitelib}/%{pkg_name}/
%{_sbindir}/rc%{pkg_name}
%{_unitdir}/%{pkg_name}.service
%config(noreplace) %attr(-,root,%{pkg_user_group}) %{pkg_config}/
%dir %attr(-,%{pkg_user_group},%{pkg_user_group}) %{pkg_home}/
%dir %attr(-,%{pkg_user_group},%{pkg_user_group}) %{pkg_home}/collections

# Register configuration files
%ghost %config(noreplace) %attr(660,%{pkg_user_group},%{pkg_user_group}) %{pkg_config}/rights
%ghost %config(noreplace) %attr(660,%{pkg_user_group},%{pkg_user_group}) %{pkg_config}/users

# User/group creation with sysusers.d(5)
%{_sysusersdir}/system-user-%{pkg_user_group}.conf

# Firewalld config
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/%{pkg_name}.xml

%changelog
