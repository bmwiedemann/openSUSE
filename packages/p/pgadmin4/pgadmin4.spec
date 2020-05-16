#
# spec file for package pgadmin4
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


%global	pgadmin4instdir %{_libdir}/pgadmin4-%{version}
Name:           pgadmin4
Version:        4.21
Release:        0
Summary:        Management tool for PostgreSQL
License:        PostgreSQL
Group:          Productivity/Databases/Tools
URL:            http://www.pgadmin.org
Source0:        https://download.postgresql.org/pub/pgadmin/%{name}/v%{version}/source/%{name}-%{version}.tar.gz
Source1:        %{name}.conf
Source2:        %{name}.service.in
Source3:        %{name}.tmpfiles.d
Source4:        %{name}.desktop.in
Source5:        %{name}.config_local.py.in
Source6:        %{name}.qt.conf.in
Source7:        README.SUSE
Patch0:         use-os-makedirs.patch
Patch1:         fix-python3-crypto-call.patch
Patch2:         fix-python-lib.patch
BuildRequires:  Mesa-libGL-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libQt5Core-devel
BuildRequires:  libQt5Network-devel
BuildRequires:  libQt5Widgets-devel
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
Requires:       %{name}-web = %{version}
Requires:       python3 >= 3.3
%{?systemd_requires}

%description
pgAdmin 4 is a rewrite of the pgAdmin3 management tool for the
PostgreSQL database. It is written as a web application in Python,
using jQuery and Bootstrap for the client side processing and UI. On
the server side, Flask is being utilised.

This variant is a Qt-based runtime application intended to allow the
standalone use on a workstation - it is essentially a browser and
Python interpretor in one package which will be capable of hosting
the Python application and presenting it to the user as a desktop
application.

%package web
Summary:        Web package for pgAdmin4
Group:          Productivity/Databases/Tools
Requires:       python3-Babel >= 1.3
Requires:       python3-Flask >= 1.0.2
Requires:       python3-Flask-Babel >= 0.11.1
Requires:       python3-Flask-Compress >= 1.4.0
Requires:       python3-Flask-Gravatar >= 0.5.0
Requires:       python3-Flask-HTMLmin >= 1.3.2
Requires:       python3-Flask-Login >= 0.4.1
Requires:       python3-Flask-Mail >= 0.9.1
Requires:       python3-Flask-Migrate >= 2.4.0
Requires:       python3-Flask-Paranoid >= 0.2.0
Requires:       python3-Flask-Principal >= 0.4.0
Requires:       python3-Flask-SQLAlchemy >= 2.4.1
Requires:       python3-Flask-Security-Too >= 3.0.0
Requires:       python3-Flask-WTF >= 0.14.3
Requires:       python3-Jinja2 >= 2.7.3
Requires:       python3-MarkupSafe >= 0.23
Requires:       python3-SQLAlchemy >= 1.3.13
Requires:       python3-WTForms >= 2.1
Requires:       python3-Werkzeug >= 0.14.1
Requires:       python3-beautifulsoup4 >= 4.4.1
Requires:       python3-blinker >= 1.4
Requires:       python3-click
Requires:       python3-extras >= 1.0.0
Requires:       python3-fixtures >= 3.0.0
Requires:       python3-html5lib >= 1.0.1
Requires:       python3-htmlmin >= 0.1.12
Requires:       python3-itsdangerous >= 0.24
Requires:       python3-ldap3 >= 2.5.1
Requires:       python3-linecache2 >= 1.0.0
Requires:       python3-passlib >= 1.7.1
Requires:       python3-pbr >= 3.1.1
Requires:       python3-psutil >= 5.7.0
Requires:       python3-psycopg2 >= 2.7.4
Requires:       python3-pycrypto >= 2.6.1
Requires:       python3-pyrsistent >= 0.14.2
Requires:       python3-python-dateutil >= 2.7.3
Requires:       python3-python-mimeparse >= 1.6.0
Requires:       python3-pytz >= 2018.3
Requires:       python3-simplejson >= 3.13.2
Requires:       python3-six >= 1.12.0
Requires:       python3-speaklater >= 1.3
Requires:       python3-sqlparse >= 0.2.4
Requires:       python3-sshtunnel >= 0.1.4
Recommends:     python3-mod_wsgi
Suggests:       %{name}-doc
BuildArch:      noarch

%description web
pgAdmin 4 is a rewrite of the pgAdmin3 management tool for the
PostgreSQL database.

This package contains the required files to run pgAdmin4 as a web application

%package	doc
Summary:        Documentation for pgAdmin4
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
pgAdmin 4 is a rewrite of the pgAdmin3 management tool for the
PostgreSQL database.

This package contains the documentation for pgadmin4.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%if %{?pkg_vcmp:%{pkg_vcmp python3-devel >= 3.8}}%{!?pkg_vcmp:0}
%patch2 -p1
%endif
cp %{S:7} .
# rpmlint
chmod -x docs/en_US/theme/pgadmin4/static/style.css
chmod -x docs/en_US/theme/pgadmin4/theme.conf

%build
cd runtime
export PYTHON_CONFIG=%{_bindir}/python3-config
export PYTHON_VERSION=%{python3_version}
export CFLAGS=%{RPM_OPT_FLAGS}
qmake-qt5 -o Makefile pgAdmin4.pro
make %{?_smp_mflags} VERBOSE=1

%install
cd runtime
install -d -m 755 %{buildroot}%{_docdir}/%{name}-docs/
cp -pr ../docs/* %{buildroot}%{_docdir}/%{name}-docs

install -d -m 755 %{buildroot}%{_bindir}
cp pgAdmin4 %{buildroot}%{_bindir}

install -d -m 755 %{buildroot}%{python3_sitelib}/pgadmin4-web
cp -pR ../web/* %{buildroot}%{python3_sitelib}/pgadmin4-web

install -d %{buildroot}%{_sysconfdir}/apache2/conf.d/
install -m 0644 -p %{SOURCE1} %{buildroot}%{_sysconfdir}/apache2/conf.d/%{name}.conf

# Install desktop file
install -d %{buildroot}%{_datadir}/applications/
sed -e 's@PYTHONDIR@%{_bindir}/python3@g' -e 's@PYTHONSITELIB@%{python3_sitelib}@g' < %{SOURCE4} > %{buildroot}%{_datadir}/applications/%{name}.desktop

# Install config_local
install -m 0644 %{SOURCE5} %{buildroot}%{python3_sitelib}/%{name}-web/config_local.py

# Install QT conf file
# This directory will/may change in future releases.
install -d "%{buildroot}%{_sysconfdir}/xdg/pgadmin/"
sed -e 's@PYTHONSITELIB64@%{python3_sitearch}@g' -e 's@PYTHONSITELIB@%{python3_sitelib}@g'<%{SOURCE6} > "%{buildroot}%{_sysconfdir}/xdg/pgadmin/pgadmin4.conf"

# Install unit file/init script
# This is only for systemd supported distros:
install -d %{buildroot}%{_unitdir}
sed -e 's@PYTHONDIR@%{_bindir}/python3@g' -e 's@PYTHONSITELIB@%{python3_sitelib}@g' < %{SOURCE2} > %{buildroot}%{_unitdir}/%{name}.service

# ... and make a tmpfiles script to recreate it at reboot.
mkdir -p %{buildroot}/%{_tmpfilesdir}
install -m 0644 %{SOURCE3} %{buildroot}/%{_tmpfilesdir}/%{name}.conf

cd %{buildroot}%{python3_sitelib}/%{name}-web
rm -f %{name}.db
echo "SERVER_MODE = False" > config_distro.py
echo "HTML_HELP = '%{_datadir}/doc/%{name}-docs/en_US/html/'" >> config_distro.py
chmod -x %{buildroot}%{_docdir}/%{name}-docs/en_US/images/*
rm %{buildroot}%{python3_sitelib}/%{name}-web/regression/.gitignore
rm %{buildroot}%{_docdir}/%{name}-docs/en_US/.gitignore
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcpgadmin4
%fdupes %{buildroot}/%{_prefix}

%pre web
%service_add_pre %{name}.service

%post web
%service_add_post %{name}.service
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf

%preun web
%service_del_preun %{name}.service

%postun web
%service_del_postun %{name}.service

%files
%defattr(-,root,root,-)
%doc README README.SUSE
%license LICENSE
%{_bindir}/pgAdmin4
%{_datadir}/applications/%{name}.desktop
%dir %{_sysconfdir}/xdg/pgadmin
%config %{_sysconfdir}/xdg/pgadmin/pgadmin4.conf

%files web
%defattr(-,root,root,-)
%dir %{python3_sitelib}/%{name}-web/
%{python3_sitelib}/%{name}-web/*
%dir %{_sysconfdir}/apache2
%dir %{_sysconfdir}/apache2/conf.d
%config(noreplace) %{_sysconfdir}/apache2/conf.d/%{name}.conf
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%{_sbindir}/rcpgadmin4
%ghost %dir %{_rundir}/%{name}

%files doc
%defattr(-,root,root,-)
%dir %{_docdir}/%{name}-docs
%doc %{_docdir}/%{name}-docs/*

%changelog
