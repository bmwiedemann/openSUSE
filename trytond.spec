#
# spec file for package trytond
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015-2018 Dr. Axel Braun
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


%define majorver 4.6
%define base_name tryton
Name:           trytond
Version:        %{majorver}.20
Release:        0

Summary:        An Enterprise Resource Planning (ERP) system
License:        GPL-3.0-or-later
Group:          Productivity/Office/Management
Url:            http://www.tryton.org/
Source0:        http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz
Source1:        tryton-server.README.SUSE
Source2:        trytond.conf.example
Source3:        %{name}.conf
Source4:        %{name}_log.conf
Source20:       %{name}.service

Patch0:         get_login_trytond-46.patch

# List of additional build dependencies
BuildRequires:  fdupes
BuildRequires:  python3-Werkzeug
BuildRequires:  python3-bcrypt
BuildRequires:  python3-lxml >= 2.0
BuildRequires:  python3-psycopg2
BuildRequires:  python3-pydot3
BuildRequires:  python3-python-sql
BuildRequires:  python3-setuptools
BuildRequires:  python3-wrapt
BuildRequires:  systemd-rpm-macros
Requires:       html2text
Requires:       libreoffice-pyuno
Requires:       postgresql-server
Requires:       python3-Genshi
Requires:       python3-Levenshtein
Requires:       python3-Sphinx
Requires:       python3-Werkzeug
Requires:       python3-bcrypt
Requires:       python3-dateutil
Requires:       python3-lxml
Requires:       python3-mock
Requires:       python3-polib
Requires:       python3-psycopg2 >= 2.5.4
Requires:       python3-python-sql >= 0.4
Requires:       python3-relatorio >= 0.7.0
Requires:       python3-simpleeval
Requires:       python3-wrapt
Requires:       unoconv
Requires(pre): 	/usr/sbin/groupadd
Requires(pre): 	/usr/sbin/useradd
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%{?systemd_requires}

%description
This package contains the server of the Tryton application platform,
the latter of which is a three-tier high-level general purpose
application platform written in Python, using Postgresql as the
database engine. Tryton provides modularity, scalability and
security.

%prep
%setup -q 
cp %{S:1} .
cp %{S:2} .
%patch0 -p1

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%_prefix --root=%buildroot 
# only for systemd
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{base_name}
install -p -m 640 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/%{base_name}/%{name}.conf
install -p -m 640 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/%{base_name}/%{name}_log.conf

mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -p -m 644 %{SOURCE20} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/{lib,log}/%{base_name}

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%pre

#Write GH Variable /etc/tryton/gnuhealthrc 
cat > /etc/tryton/gnuhealthrc << "EOF"
TRYTON_VERSION=%{version}
EOF

getent group tryton > /dev/null || %{_sbindir}/groupadd -r tryton || :
getent passwd tryton > /dev/null || %{_sbindir}/useradd -r -g tryton \
       -d %{_localstatedir}/lib/%{name} -s /sbin/nologin \
	-c 'Tryton ERP' tryton || :
%service_add_pre trytond.service

%post
%service_add_post trytond.service

%preun
%service_del_preun trytond.service

%postun
%service_del_postun trytond.service

%files 
#%files -f filelist
%defattr(-,root,root)
%doc README tryton-server.README.SUSE trytond.conf.example LICENSE doc/*
%{python3_sitelib}/*
%dir %{_sysconfdir}/%{base_name}
%{_bindir}/%{name}
%{_bindir}/%{name}-admin
%{_bindir}/%{name}-cron
%{_unitdir}/%{name}.service
%attr(640,root,tryton) %config(noreplace)%{_sysconfdir}/%{base_name}/%{name}.conf
%attr(640,root,tryton) %config(noreplace)%{_sysconfdir}/%{base_name}/%{name}_log.conf
%attr(755,tryton,tryton) %dir %{_localstatedir}/lib/%{base_name}
%attr(755,tryton,tryton) %dir %{_localstatedir}/log/%{base_name}

%changelog
