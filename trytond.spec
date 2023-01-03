#
# spec file for package trytond
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2015-2022 Dr. Axel Braun
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


%define majorver 6.0
%define base_name tryton
Name:           trytond
Version:        %{majorver}.25
Release:        0
Summary:        An Enterprise Resource Planning (ERP) system
License:        GPL-3.0-or-later
Group:          Productivity/Office/Management
URL:            https://www.tryton.org/
Source0:        http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz
Source1:        tryton-server.README.openSUSE
Source3:        %{name}.conf
Source4:        %{name}_log.conf
Source5:        http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz.asc
Source6:        https://keybase.io/cedrickrier/pgp_keys.asc?fingerprint=7C5A4360F6DF81ABA91FD54D6FF50AFE03489130#/%{name}.keyring
Source7:        openSUSE-trytond-setup
Source20:       %{name}.service
Patch0:         Update_changed_fields_6.0.diff
BuildRequires:  fdupes
BuildRequires:  python3-Werkzeug
BuildRequires:  python3-bcrypt
BuildRequires:  python3-lxml >= 2.0
BuildRequires:  python3-psycopg2 >= 2.5.4
BuildRequires:  python3-pydot3
BuildRequires:  python3-python-sql >= 0.5
BuildRequires:  python3-setuptools
BuildRequires:  python3-wrapt

Requires:       graphviz
Requires:       html2text
Requires:       libreoffice-pyuno
Requires:       python3-Genshi
Requires:       python3-Levenshtein
Requires:       python3-Pillow
Requires:       python3-Werkzeug
Requires:       python3-bcrypt
Requires:       python3-dateutil
Requires:       python3-defusedxml
Requires:       python3-gevent
Requires:       python3-lxml
Requires:       python3-passlib >= 1.7.0
Requires:       python3-polib
Requires:       python3-psycopg2 >= 2.5.4
Requires:       python3-pydot
Requires:       python3-python-sql >= 0.5
Requires:       python3-relatorio >= 0.7.0
Requires:       python3-weasyprint
Requires:       python3-wrapt
Requires:       unoconv
Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/useradd
# Database may run on a different machine, so a hard requirement is not ideal
Recommends:     postgresql-server

BuildArch:      noarch
%{?systemd_ordering}

%description
This package contains the server of the Tryton application platform,
the latter of which is a three-tier high-level general purpose
application platform written in Python, using Postgresql as the
database engine. Tryton provides modularity, scalability and
security.

%prep
%setup -q
cp %{SOURCE1} .

%patch0 -p1

%build
%python3_build

%install
%python3_install --prefix=%{_prefix} --root=%{buildroot}

# only for systemd
mkdir -p %{buildroot}%{_sysconfdir}/%{base_name}
install -p -m 640 %{SOURCE3} %{buildroot}%{_sysconfdir}/%{base_name}/%{name}.conf
install -p -m 640 %{SOURCE4} %{buildroot}%{_sysconfdir}/%{base_name}/%{name}_log.conf

mkdir -p -m 755 %{buildroot}%{_bindir}
install -p -m 755 %{S:7} %{buildroot}%{_bindir}/openSUSE-trytond-setup

mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 %{SOURCE20} %{buildroot}%{_unitdir}/%{name}.service

mkdir -p %{buildroot}%{_localstatedir}/{lib,log}/%{base_name}
%fdupes -s %{buildroot}

%pre
getent group tryton > /dev/null || %{_sbindir}/groupadd -r tryton || :
getent passwd tryton > /dev/null || %{_sbindir}/useradd -r -g tryton \
       -d %{_localstatedir}/lib/tryton -s /sbin/nologin \
	-c 'Tryton ERP' tryton || :
%service_add_pre trytond.service

%post
%service_add_post trytond.service

%preun
%service_del_preun trytond.service

%postun
%service_del_postun trytond.service

%files
%license LICENSE
%doc README.rst tryton-server.README.openSUSE doc/*
%{python3_sitelib}/*
%dir %{_sysconfdir}/%{base_name}
%{_bindir}/openSUSE-trytond-setup
%{_bindir}/%{name}*
%{_unitdir}/%{name}.service
%attr(640,root,tryton) %config(noreplace)%{_sysconfdir}/%{base_name}/%{name}.conf
%attr(640,root,tryton) %config(noreplace)%{_sysconfdir}/%{base_name}/%{name}_log.conf
%attr(755,tryton,tryton) %dir %{_localstatedir}/lib/%{base_name}
%attr(755,tryton,tryton) %dir %{_localstatedir}/log/%{base_name}

%changelog
