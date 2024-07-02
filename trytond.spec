#
# spec file for package trytond
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2015-2024 Dr. Axel Braun
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
%if 0%{?suse_version} >= 1550
%define pythons python3
%define mypython python3
%define mysitelib %python3_sitelib
%else
%{?sle15_python_module_pythons}
%define mypython %pythons
%define mysitelib %{expand:%%%{mypython}_sitelib}
%endif

Name:           trytond
Version:        %{majorver}.48
Release:        0
Summary:        An Enterprise Resource Planning (ERP) system
License:        GPL-3.0-or-later
Group:          Productivity/Office/Management
URL:            https://www.tryton.org/
Source0:        http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz
Source1:        tryton-server.README.openSUSE
Source3:        %{name}.conf
Source4:        %{name}_log.conf
## Source5:        http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz.asc
## Source6:        https://keybase.io/cedrickrier/pgp_keys.asc?fingerprint=7C5A4360F6DF81ABA91FD54D6FF50AFE03489130#/%{name}.keyring
Source7:        openSUSE-trytond-setup
Source20:       %{name}.service
Patch0:         Update_changed_fields_6.0.diff
BuildRequires:  %{mypython}-Werkzeug
BuildRequires:  %{mypython}-bcrypt
BuildRequires:  %{mypython}-devel
BuildRequires:  %{mypython}-lxml >= 2.0
BuildRequires:  %{mypython}-psycopg2 >= 2.7.0
BuildRequires:  %{mypython}-pydot
BuildRequires:  %{mypython}-python-sql >= 0.5
BuildRequires:  %{mypython}-setuptools
BuildRequires:  %{mypython}-wrapt
BuildRequires:  fdupes
BuildRequires:  python-rpm-generators
BuildRequires:  python-rpm-macros
# Wheel
BuildRequires:  %{mypython}-pip
BuildRequires:  %{mypython}-wheel

Requires:       %{mypython}-Genshi
Requires:       %{mypython}-Levenshtein
Requires:       %{mypython}-Pillow
Requires:       %{mypython}-Werkzeug
Requires:       %{mypython}-bcrypt
Requires:       %{mypython}-dateutil
Requires:       %{mypython}-defusedxml
Requires:       %{mypython}-gevent
Requires:       %{mypython}-lxml
Requires:       %{mypython}-passlib >= 1.7.0
Requires:       %{mypython}-polib
Requires:       %{mypython}-psycopg2 >= 2.7.0
Requires:       %{mypython}-pydot
Requires:       %{mypython}-python-sql >= 0.5
Requires:       %{mypython}-relatorio >= 0.7.0
Requires:       %{mypython}-weasyprint
Requires:       %{mypython}-wrapt
Requires:       graphviz
Requires:       html2text
Requires:       libreoffice-pyuno
Requires:       unoconv
Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/useradd
# Database may run on a different machine, so a hard requirement is not ideal
Recommends:     postgresql-server

Provides:       group(tryton)
Provides:       user(tryton)

BuildArch:      noarch
%{?systemd_ordering}

%description
This package contains the server of the Tryton application platform,
the latter of which is a three-tier high-level general purpose
application platform written in Python, using Postgresql as the
database engine. Tryton provides modularity, scalability and
security.

%prep
%autosetup -p1
cp %{SOURCE1} .

#shebag ersetzen
find . -iname "bin/trytond*" -exec sed -i "s/python3 /%{mypython} /" '{}' \;

%build
%pyproject_wheel

%install
%pyproject_install

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
%{mysitelib}/tryton*
%dir %{_sysconfdir}/%{base_name}
%{_bindir}/openSUSE-trytond-setup
%{_bindir}/%{name}*
%{_unitdir}/%{name}.service
%attr(640,root,tryton) %config(noreplace)%{_sysconfdir}/%{base_name}/%{name}.conf
%attr(640,root,tryton) %config(noreplace)%{_sysconfdir}/%{base_name}/%{name}_log.conf
%attr(755,tryton,tryton) %dir %{_localstatedir}/lib/%{base_name}
%attr(755,tryton,tryton) %dir %{_localstatedir}/log/%{base_name}

%changelog
