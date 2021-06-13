#
# spec file for package pgadmin4
#
# Copyright (c) 2021 SUSE LLC
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


%global python3_babel_min_version 1.3
%global python3_beautifulsoup4_min_version 4.4.1
%global python3_blinker_min_version 1.4
%global python3_extras_min_version 1.0.0
%global python3_fixtures_min_version 3.0.0
%global python3_flask_babelex_min_version 0.9.4
%global python3_flask_compress_min_version 1.4.0
%global python3_flask_gravatar_min_version 0.5.0
%global python3_flask_htmlmin_min_version 1.3.2
%global python3_flask_login_min_version 0.4.1
%global python3_flask_mail_min_version 0.9.1
%global python3_flask_migrate_min_version 2.4.0
%global python3_flask_min_version 1.0.2
%global python3_flask_paranoid_min_version 0.2.0
%global python3_flask_principal_min_version 0.4.0
%global python3_flask_security_too_min_version 3.0.0
%global python3_flask_sqlalchemy_min_version 2.4.1
%global python3_flask_wtf_min_version 0.14.3
%global python3_gssapi_min_version 1.6.11 
%global python3_html5lib_min_version 1.0.1
%global python3_htmlmin_min_version 0.1.12
%global python3_itsdangerous_min_version 0.24
%global python3_jinja2_min_version 2.7.3
%global python3_ldap3_min_version 2.5.1
%global python3_linecache2_min_version 1.0.0
%global python3_markupsafe_min_version 0.23
%global python3_passlib_min_version 1.7.2
%global python3_pbr_min_version 3.1.1
%global python3_psutil_min_version 5.7.0
%global python3_psycopg2_min_version 2.8
%global python3_pycrypto_min_version 2.6.1
%global python3_pyrsistent_min_version 0.14.2
%global python3_python_dateutil_min_version 2.8.0
%global python3_python_mimeparse_min_version 1.6.0
%global python3_pytz_min_version 2020.1
%global python3_simplejson_min_version 3.16.0
%global python3_six_min_version 1.12.0
%global python3_speaklater_min_version 1.3
%global python3_sqlalchemy_min_version 1.3.13
%global python3_sqlparse_min_version 0.3.0
%global python3_sshtunnel_min_version 0.1.5
%global python3_werkzeug_min_version 0.15.0
%global python3_wtforms_min_version 2.2.1

%global	pgadmin4instdir %{_libdir}/pgadmin4-%{version}
%global	pgadmin4homedir /var/lib/pgadmin
%global user_group_name pgadmin

Name:           pgadmin4
Version:        4.30
Release:        0
Summary:        Management tool for PostgreSQL
License:        PostgreSQL
Group:          Productivity/Databases/Tools
URL:            http://www.pgadmin.org
Source0:        https://download.postgresql.org/pub/pgadmin/%{name}/v%{version}/source/%{name}-%{version}.tar.gz
Source10:       https://download.postgresql.org/pub/pgadmin/%{name}/v%{version}/source/%{name}-%{version}.tar.gz.asc
# https://www.pgadmin.org/download/pgadmin-4-source-code/
Source11:       %{name}.keyring
Source1:        %{name}.conf.in
Source2:        %{name}.service.in
Source3:        %{name}.tmpfiles.d
Source4:        %{name}.desktop.in
Source6:        %{name}.qt.conf.in
Source7:        %{name}.uwsgi.in
Source8:        README.SUSE
Source9:        README.SUSE.uwsgi.in
Patch0:         use-os-makedirs.patch
Patch1:         fix-python3-crypto-call.patch
Patch2:         fix-python-lib.patch
Patch3:         0001-Fix-bug-ValueError-unsupported-format-character-D.patch
BuildRequires:  Mesa-libGL-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libQt5Core-devel
BuildRequires:  libQt5Network-devel
BuildRequires:  libQt5Widgets-devel
BuildRequires:  python3-Babel >= %{python3_babel_min_version}
BuildRequires:  python3-Flask >= %{python3_flask_min_version}
BuildRequires:  python3-Flask-BabelEx >= %{python3_flask_babelex_min_version}
BuildRequires:  python3-Flask-Compress >= %{python3_flask_compress_min_version}
BuildRequires:  python3-Flask-Gravatar >= %{python3_flask_gravatar_min_version}
BuildRequires:  python3-Flask-HTMLmin >= %{python3_flask_htmlmin_min_version}
BuildRequires:  python3-Flask-Login >= %{python3_flask_login_min_version}
BuildRequires:  python3-Flask-Mail >= %{python3_flask_mail_min_version}
BuildRequires:  python3-Flask-Migrate >= %{python3_flask_migrate_min_version}
BuildRequires:  python3-Flask-Paranoid >= %{python3_flask_paranoid_min_version}
BuildRequires:  python3-Flask-Principal >= %{python3_flask_principal_min_version}
BuildRequires:  python3-Flask-SQLAlchemy >= %{python3_flask_sqlalchemy_min_version}
BuildRequires:  python3-Flask-Security-Too >= %{python3_flask_security_too_min_version}
BuildRequires:  python3-Flask-WTF >= %{python3_flask_wtf_min_version}
BuildRequires:  python3-Jinja2 >= %{python3_jinja2_min_version}
BuildRequires:  python3-MarkupSafe >= %{python3_markupsafe_min_version}
BuildRequires:  python3-SQLAlchemy >= %{python3_sqlalchemy_min_version}
BuildRequires:  python3-WTForms >= %{python3_wtforms_min_version}
BuildRequires:  python3-Werkzeug >= %{python3_werkzeug_min_version}
BuildRequires:  python3-beautifulsoup4 >= %{python3_beautifulsoup4_min_version}
BuildRequires:  python3-blinker >= %{python3_blinker_min_version}
BuildRequires:  python3-click
BuildRequires:  python3-cryptography
BuildRequires:  python3-devel
BuildRequires:  python3-extras >= %{python3_extras_min_version}
BuildRequires:  python3-fixtures >= %{python3_fixtures_min_version}
BuildRequires:  python3-gssapi >= %{python3_gssapi_min_version}
BuildRequires:  python3-html5lib >= %{python3_html5lib_min_version}
BuildRequires:  python3-htmlmin >= %{python3_htmlmin_min_version}
BuildRequires:  python3-itsdangerous >= %{python3_itsdangerous_min_version}
BuildRequires:  python3-ldap3 >= %{python3_ldap3_min_version}
BuildRequires:  python3-linecache2 >= %{python3_linecache2_min_version}
BuildRequires:  python3-passlib >= %{python3_passlib_min_version}
BuildRequires:  python3-pbr >= %{python3_pbr_min_version}
BuildRequires:  python3-psutil >= %{python3_psutil_min_version}
BuildRequires:  python3-psycopg2 >= %{python3_psycopg2_min_version}
BuildRequires:  python3-pycrypto >= %{python3_pycrypto_min_version}
BuildRequires:  python3-pyrsistent >= %{python3_pyrsistent_min_version}
BuildRequires:  python3-python-dateutil >= %{python3_python_dateutil_min_version}
BuildRequires:  python3-python-mimeparse >= %{python3_python_mimeparse_min_version}
BuildRequires:  python3-pytz >= %{python3_pytz_min_version}
BuildRequires:  python3-simplejson >= %{python3_simplejson_min_version}
BuildRequires:  python3-six >= %{python3_six_min_version}
BuildRequires:  python3-speaklater >= %{python3_speaklater_min_version}
BuildRequires:  python3-sqlparse >= %{python3_sqlparse_min_version}
BuildRequires:  python3-sshtunnel >= %{python3_sshtunnel_min_version}
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
Requires:       python3-Babel >= %{python3_babel_min_version}
Requires:       python3-Flask >= %{python3_flask_min_version}
Requires:       python3-Flask-BabelEx >= %{python3_flask_babelex_min_version}
Requires:       python3-Flask-Compress >= %{python3_flask_compress_min_version}
Requires:       python3-Flask-Gravatar >= %{python3_flask_gravatar_min_version}
Requires:       python3-Flask-HTMLmin >= %{python3_flask_htmlmin_min_version}
Requires:       python3-Flask-Login >= %{python3_flask_login_min_version}
Requires:       python3-Flask-Mail >= %{python3_flask_mail_min_version}
Requires:       python3-Flask-Migrate >= %{python3_flask_migrate_min_version}
Requires:       python3-Flask-Paranoid >= %{python3_flask_paranoid_min_version}
Requires:       python3-Flask-Principal >= %{python3_flask_principal_min_version}
Requires:       python3-Flask-SQLAlchemy >= %{python3_flask_sqlalchemy_min_version}
Requires:       python3-Flask-Security-Too >= %{python3_flask_security_too_min_version}
Requires:       python3-Flask-WTF >= %{python3_flask_wtf_min_version}
Requires:       python3-Jinja2 >= %{python3_jinja2_min_version}
Requires:       python3-MarkupSafe >= %{python3_markupsafe_min_version}
Requires:       python3-SQLAlchemy >= %{python3_sqlalchemy_min_version}
Requires:       python3-WTForms >= %{python3_wtforms_min_version}
Requires:       python3-Werkzeug >= %{python3_werkzeug_min_version}
Requires:       python3-beautifulsoup4 >= %{python3_beautifulsoup4_min_version}
Requires:       python3-blinker >= %{python3_blinker_min_version}
Requires:       python3-click
Requires:       python3-cryptography
Requires:       python3-extras >= %{python3_extras_min_version}
Requires:       python3-fixtures >= %{python3_fixtures_min_version}
Requires:       python3-gssapi >= %{python3_gssapi_min_version}
Requires:       python3-html5lib >= %{python3_html5lib_min_version}
Requires:       python3-htmlmin >= %{python3_htmlmin_min_version}
Requires:       python3-itsdangerous >= %{python3_itsdangerous_min_version}
Requires:       python3-ldap3 >= %{python3_ldap3_min_version}
Requires:       python3-linecache2 >= %{python3_linecache2_min_version}
Requires:       python3-passlib >= %{python3_passlib_min_version}
Requires:       python3-pbr >= %{python3_pbr_min_version}
Requires:       python3-psutil >= %{python3_psutil_min_version}
Requires:       python3-psycopg2 >= %{python3_psycopg2_min_version}
Requires:       python3-pycrypto >= %{python3_pycrypto_min_version}
Requires:       python3-pyrsistent >= %{python3_pyrsistent_min_version}
Requires:       python3-python-dateutil >= %{python3_python_dateutil_min_version}
Requires:       python3-python-mimeparse >= %{python3_python_mimeparse_min_version}
Requires:       python3-pytz >= %{python3_pytz_min_version}
Requires:       python3-simplejson >= %{python3_simplejson_min_version}
Requires:       python3-six >= %{python3_six_min_version}
Requires:       python3-speaklater >= %{python3_speaklater_min_version}
Requires:       python3-sqlparse >= %{python3_sqlparse_min_version}
Requires:       python3-sshtunnel >= %{python3_sshtunnel_min_version}
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

%package web-uwsgi
Summary:        Pgamdin4 - uwsgi configuration
Group:          Productivity/Networking/Web/Utilities
BuildArch:      noarch
Requires:       pgadmin4-web
Requires:       uwsgi

%description web-uwsgi
pgadmin4 is a management tool for PostgreSQL.

This package holds the uwsgi configuration.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%if %{?pkg_vcmp:%{pkg_vcmp python3-devel >= 3.8}}%{!?pkg_vcmp:0}
%patch2 -p1
%endif
%patch3 -p1

sed -e 's@PYTHONSITELIB@%{python3_sitelib}@g' <%{SOURCE1} > %{name}.conf
sed -e 's@PYTHONDIR@%{_bindir}/python3@g' -e 's@PYTHONSITELIB@%{python3_sitelib}@g' < %{SOURCE2} > %{name}.service
sed -e 's@PYTHONDIR@%{_bindir}/python3@g' -e 's@PYTHONSITELIB@%{python3_sitelib}@g' < %{SOURCE4} > %{name}.desktop
sed -e 's@PYTHONSITELIB64@%{python3_sitearch}@g' -e 's@PYTHONSITELIB@%{python3_sitelib}@g' <%{SOURCE6} > %{name}.qt.conf
sed -e 's@PYTHONSITELIB@%{python3_sitelib}@g' <%{SOURCE7} > %{name}.uwsgi
sed -e 's@PYTHONSITELIB@%{python3_sitelib}@g' <%{SOURCE9} > README.SUSE.uwsgi

cp %{SOURCE8} .
cp %{SOURCE9} .
# rpmlint
chmod -x docs/en_US/theme/pgadmin4/static/style.css
chmod -x docs/en_US/theme/pgadmin4/theme.conf

%build
cd runtime
export PYTHON_CONFIG=%{_bindir}/python3-config
export PYTHON_VERSION=%{python3_version}
export PGADMIN_PYTHON_DIR=%{_prefix}
export CFLAGS=%{RPM_OPT_FLAGS}
qmake-qt5 -o Makefile pgAdmin4.pro
make %{?_smp_mflags} VERBOSE=1

%install
install -d -m 755 %{buildroot}%{_docdir}/%{name}-docs/
cp -pr docs/* %{buildroot}%{_docdir}/%{name}-docs

pushd runtime
install -d -m 755 %{buildroot}%{_bindir}
cp pgAdmin4 %{buildroot}%{_bindir}
popd

install -d -m 755 %{buildroot}%{python3_sitelib}/pgadmin4-web
cp -pR web/* %{buildroot}%{python3_sitelib}/pgadmin4-web

install -d %{buildroot}%{_sysconfdir}/apache2/conf.d/
install -m 0644 -p %{name}.conf %{buildroot}%{_sysconfdir}/apache2/conf.d/%{name}.conf

# Install desktop file
install -d %{buildroot}%{_datadir}/applications/
install -m 0644 -p %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

# Install config system for webapp
install -d -m 0755 %{buildroot}%{_sysconfdir}/pgadmin/
echo "# SERVER_MODE = True" > %{buildroot}%{_sysconfdir}/pgadmin/config_system.py

# Install QT conf file
# This directory will/may change in future releases.
install -d "%{buildroot}%{_sysconfdir}/xdg/pgadmin/"
install -m 0644 -p %{name}.qt.conf %{buildroot}%{_sysconfdir}/xdg/pgadmin/pgadmin4.conf

# Install unit file/init script
# This is only for systemd supported distros:
install -d %{buildroot}%{_unitdir}
install -m 0644 -p %{name}.service %{buildroot}%{_unitdir}/%{name}.service

# ... and make a tmpfiles script to recreate it at reboot.
mkdir -p %{buildroot}/%{_tmpfilesdir}
install -m 0644 %{SOURCE3} %{buildroot}/%{_tmpfilesdir}/%{name}.conf

pushd %{buildroot}%{python3_sitelib}/%{name}-web
rm -f %{name}.db

cat << EOF > config_distro.py
# SERVER_MODE = True
HTML_HELP = '%{_datadir}/doc/%{name}-docs/en_US/html/'
UPGRADE_CHECK_ENABLED = False
DEFAULT_BINARY_PATHS = {
    "pg": "%{_bindir}"
}
EOF
popd

chmod -x %{buildroot}%{_docdir}/%{name}-docs/en_US/images/*
rm %{buildroot}%{python3_sitelib}/%{name}-web/regression/.gitignore
rm %{buildroot}%{_docdir}/%{name}-docs/en_US/.gitignore
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcpgadmin4
%fdupes %{buildroot}/%{_prefix}

install -d -m 0755 %{buildroot}%{pgadmin4homedir}
install -d -m 0755 %{buildroot}%{pgadmin4homedir}/storage
install -d -m 0700 %{buildroot}%{pgadmin4homedir}/sessions

install -d -m 0755 %{buildroot}%{_sysconfdir}/uwsgi/vassals
install -m 0644 %{name}.uwsgi %{buildroot}%{_sysconfdir}/uwsgi/vassals/pgadmin4.ini

%pre web
/usr/sbin/groupadd -r %{user_group_name} &>/dev/null || :
/usr/sbin/useradd  -g %{user_group_name} -s /bin/false -r -c "%{name}" -d %{pgadmin4homedir} %{user_group_name} &>/dev/null || :
%service_add_pre %{name}.service

%post web
%service_add_post %{name}.service
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf

%preun web
%service_del_preun %{name}.service

%postun web
chown -R %{user_group_name}:%{user_group_name} %{pgadmin4homedir}
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
%dir %{_sysconfdir}/apache2
%dir %{_sysconfdir}/apache2/conf.d
%config(noreplace) %{_sysconfdir}/apache2/conf.d/%{name}.conf

%dir %{python3_sitelib}/%{name}-web/
%{python3_sitelib}/%{name}-web/*

%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%{_sbindir}/rcpgadmin4

%defattr(-,root,%{user_group_name})
%dir %{_sysconfdir}/pgadmin
%config(noreplace) %{_sysconfdir}/pgadmin/config_system.py

%defattr(-,%{user_group_name},%{user_group_name})
%ghost %dir %{_rundir}/%{name}
%dir %{pgadmin4homedir}
%dir %{pgadmin4homedir}/storage
%attr(700,%{user_group_name},%{user_group_name}) %dir %{pgadmin4homedir}/sessions

%files doc
%defattr(-,root,root,-)
%dir %{_docdir}/%{name}-docs
%doc %{_docdir}/%{name}-docs/*

%files web-uwsgi
%defattr(-,root,root,-)
%doc README.SUSE.uwsgi
%dir %{_sysconfdir}/uwsgi
%dir %{_sysconfdir}/uwsgi/vassals
%config (noreplace) %{_sysconfdir}/uwsgi/vassals/pgadmin4.ini

%changelog
