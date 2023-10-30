#
# spec file for package pgadmin4
#
# Copyright (c) 2023 SUSE LLC
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


%define pythons python3
%global python3_authlib_min_version 1.2.0
%global python3_azure_identity_min_version 1.13
%global python3_azure_mgmt_rdbms_min_version 10.1
%global python3_azure_mgmt_resource_min_version 23.0
%global python3_azure_mgmt_subscription_min_version 3.1
%global python3_bcrypt_min_version 4.0
%global python3_boto3_min_version 1.26
%global python3_botocore_min_version 1.31
%global python3_flask_babel_min_version 3.1.0
%global python3_flask_compress_min_version 1.4.0
%global python3_flask_gravatar_min_version 0.5.0
%global python3_flask_login_min_version 0.4.1
%global python3_flask_mail_min_version 0.9.1
%global python3_flask_migrate_min_version 4.0
%global python3_flask_min_version 2.3
%global python3_flask_paranoid_min_version 0.2.0
%global python3_flask_security_too_min_version 5.1.0
%global python3_flask_socketio_min_version 5.3.0
%global python3_flask_sqlalchemy_min_version 3.0
%global python3_flask_wtf_min_version 1.1
%global python3_httpagentparser_min_version 1.9
%global python3_google_api_python_client_min_version 2.0
%global python3_google_auth_oauthlib_min_version 1.0
%global python3_ldap3_min_version 2.5.1
%global python3_pillow_min_version 9.0
%global python3_pyotp_min_version 2.0
%global python3_keyring_min_version 23.0
%global python3_passlib_min_version 1.7.2
%global python3_psutil_min_version 5.9.0
%global python3_psycopg_min_version 3.1.8
%global python3_python_dateutil_min_version 2.8.0
%global python3_pytz_min_version 2023.0
%global python3_qrcode_min_version 7.0
%global python3_sqlalchemy_min_version 2.0
%global python3_sqlparse_min_version 0.3.0
%global python3_sshtunnel_min_version 0.1.5
%global python3_user_agents_min_version 2.2
%global python3_werkzeug_min_version 2.2
%global python3_wtforms_min_version 3.0

%global	pgadmin4instdir %{_libdir}/pgadmin4-%{version}
%global	pgadmin4homedir %{_localstatedir}/lib/pgadmin
%global user_group_name pgadmin

Name:           pgadmin4
Version:        7.8
Release:        0
Summary:        Management tool for PostgreSQL
License:        PostgreSQL
Group:          Productivity/Databases/Tools
URL:            http://www.pgadmin.org
Source0:        https://download.postgresql.org/pub/pgadmin/%{name}/v%{version}/source/%{name}-%{version}.tar.gz
Source1:        %{name}.conf.in
Source2:        %{name}.service.in
Source3:        %{name}.tmpfiles.d
Source4:        %{name}.desktop
Source7:        %{name}.uwsgi.in
Source8:        README.SUSE
Source9:        README.SUSE.uwsgi.in
Source10:       https://download.postgresql.org/pub/pgadmin/%{name}/v%{version}/source/%{name}-%{version}.tar.gz.asc
# https://www.pgadmin.org/download/pgadmin-4-source-code/
Source11:       %{name}.keyring
Source12:       vendor.tar.xz
Source13:       %{name}-desktop
Source99:       update-vendor.sh
Patch0:         use-os-makedirs.patch
Patch1:         fix-python3-crypto-call.patch
Patch2:         support-new-azure-mgmt-rdbms.patch
Patch3:         support-new-werkzeug.patch
Patch4:         support-new-flask.patch
Patch5:         fix-eventlet-select_epoll.patch
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  optipng
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Authlib >= %{python3_authlib_min_version}
BuildRequires:  python3-Flask >= %{python3_flask_min_version}
BuildRequires:  python3-Flask-Babel >= %{python3_flask_babel_min_version}
BuildRequires:  python3-Flask-Compress >= %{python3_flask_compress_min_version}
BuildRequires:  python3-Flask-Gravatar >= %{python3_flask_gravatar_min_version}
BuildRequires:  python3-Flask-Login >= %{python3_flask_login_min_version}
BuildRequires:  python3-Flask-Mail >= %{python3_flask_mail_min_version}
BuildRequires:  python3-Flask-Migrate >= %{python3_flask_migrate_min_version}
BuildRequires:  python3-Flask-Paranoid >= %{python3_flask_paranoid_min_version}
BuildRequires:  python3-Flask-SQLAlchemy >= %{python3_flask_sqlalchemy_min_version}
BuildRequires:  python3-Flask-Security-Too >= %{python3_flask_security_too_min_version}
BuildRequires:  python3-Flask-SocketIO >= %{python3_flask_socketio_min_version}
BuildRequires:  python3-Flask-WTF >= %{python3_flask_wtf_min_version}
BuildRequires:  python3-SQLAlchemy >= %{python3_sqlalchemy_min_version}
BuildRequires:  python3-WTForms >= %{python3_wtforms_min_version}
BuildRequires:  python3-Werkzeug >= %{python3_werkzeug_min_version}
BuildRequires:  python3-azure-identity >= %{python3_azure_identity_min_version}
BuildRequires:  python3-azure-mgmt-rdbms >= %{python3_azure_mgmt_rdbms_min_version}
BuildRequires:  python3-azure-mgmt-resource >= %{python3_azure_mgmt_resource_min_version}
BuildRequires:  python3-azure-mgmt-subscription >= %{python3_azure_mgmt_subscription_min_version}
BuildRequires:  python3-bcrypt >= %{python3_bcrypt_min_version}
BuildRequires:  python3-boto3 >= %{python3_boto3_min_version}
BuildRequires:  python3-botocore >= %{python3_botocore_min_version}
BuildRequires:  python3-cryptography
BuildRequires:  python3-eventlet
BuildRequires:  python3-google-api-python-client >= %{python3_google_api_python_client_min_version}
BuildRequires:  python3-google-auth-oauthlib >= %{python3_google_auth_oauthlib_min_version}
BuildRequires:  python3-httpagentparser >= %{python3_httpagentparser_min_version}
BuildRequires:  python3-keyring >= %{python3_keyring_min_version}
BuildRequires:  python3-ldap3 >= %{python3_ldap3_min_version}
BuildRequires:  python3-passlib >= %{python3_passlib_min_version}
BuildRequires:  python3-pip
BuildRequires:  python3-psutil >= %{python3_psutil_min_version}
BuildRequires:  python3-psycopg >= %{python3_psycopg_min_version}
BuildRequires:  python3-pyotp >= %{python3_pyotp_min_version}
BuildRequires:  python3-python-dateutil >= %{python3_python_dateutil_min_version}
BuildRequires:  python3-pytz >= %{python3_pytz_min_version}
BuildRequires:  python3-qrcode >= %{python3_qrcode_min_version}
BuildRequires:  python3-sqlparse >= %{python3_sqlparse_min_version}
BuildRequires:  python3-sshtunnel >= %{python3_sshtunnel_min_version}
BuildRequires:  python3-testscenarios
BuildRequires:  python3-urllib3 < 2
BuildRequires:  python3-user-agents >= %{python3_user_agents_min_version}
BuildRequires:  python3-wheel
BuildRequires:  systemd-rpm-macros
BuildRequires:  yarn
Requires:       python3 >= 3.7
Requires:       python3-Authlib >= %{python3_authlib_min_version}
Requires:       python3-Flask >= %{python3_flask_min_version}
Requires:       python3-Flask-Babel >= %{python3_flask_babel_min_version}
Requires:       python3-Flask-Compress >= %{python3_flask_compress_min_version}
Requires:       python3-Flask-Gravatar >= %{python3_flask_gravatar_min_version}
Requires:       python3-Flask-Login >= %{python3_flask_login_min_version}
Requires:       python3-Flask-Mail >= %{python3_flask_mail_min_version}
Requires:       python3-Flask-Migrate >= %{python3_flask_migrate_min_version}
Requires:       python3-Flask-Paranoid >= %{python3_flask_paranoid_min_version}
Requires:       python3-Flask-SQLAlchemy >= %{python3_flask_sqlalchemy_min_version}
Requires:       python3-Flask-Security-Too >= %{python3_flask_security_too_min_version}
Requires:       python3-Flask-SocketIO >= %{python3_flask_socketio_min_version}
Requires:       python3-Flask-WTF >= %{python3_flask_wtf_min_version}
Requires:       python3-SQLAlchemy >= %{python3_sqlalchemy_min_version}
Requires:       python3-WTForms >= %{python3_wtforms_min_version}
Requires:       python3-Werkzeug >= %{python3_werkzeug_min_version}
Requires:       python3-azure-identity >= %{python3_azure_identity_min_version}
Requires:       python3-azure-mgmt-rdbms >= %{python3_azure_mgmt_rdbms_min_version}
Requires:       python3-azure-mgmt-resource >= %{python3_azure_mgmt_resource_min_version}
Requires:       python3-azure-mgmt-subscription >= %{python3_azure_mgmt_subscription_min_version}
Requires:       python3-bcrypt >= %{python3_bcrypt_min_version}
Requires:       python3-boto3 >= %{python3_boto3_min_version}
Requires:       python3-botocore >= %{python3_botocore_min_version}
Requires:       python3-cryptography
Requires:       python3-eventlet
Requires:       python3-google-api-python-client >= %{python3_google_api_python_client_min_version}
Requires:       python3-google-auth-oauthlib >= %{python3_google_auth_oauthlib_min_version}
Requires:       python3-httpagentparser >= %{python3_httpagentparser_min_version}
Requires:       python3-keyring >= %{python3_keyring_min_version}
Requires:       python3-ldap3 >= %{python3_ldap3_min_version}
Requires:       python3-passlib >= %{python3_passlib_min_version}
Requires:       python3-psutil >= %{python3_psutil_min_version}
Requires:       python3-psycopg >= %{python3_psycopg_min_version}
Requires:       python3-pyotp >= %{python3_pyotp_min_version}
Requires:       python3-python-dateutil >= %{python3_python_dateutil_min_version}
Requires:       python3-pytz >= %{python3_pytz_min_version}
Requires:       python3-qrcode >= %{python3_qrcode_min_version}
Requires:       python3-sqlparse >= %{python3_sqlparse_min_version}
Requires:       python3-sshtunnel >= %{python3_sshtunnel_min_version}
Requires:       python3-urllib3 < 2
Requires:       python3-user-agents >= %{python3_user_agents_min_version}
Suggests:       python3-mod_wsgi
Suggests:       %{name}-doc
Recommends:     %{name}-desktop
Obsoletes:      %{name}-web < %{version}
%{?systemd_requires}
BuildArch:      noarch

%description
pgAdmin 4 is a rewrite of the pgAdmin3 management tool for the
PostgreSQL database. It is written as a web application in Python,
using jQuery and Bootstrap for the client side processing and UI. On
the server side, Flask is being utilised.

This package contains the required files to run pgAdmin4 as a web application

%package	doc
Summary:        Documentation for pgAdmin4
Group:          Documentation/HTML

%description doc
pgAdmin 4 is a rewrite of the pgAdmin3 management tool for the
PostgreSQL database.

This package contains the documentation for pgadmin4.

%package web-uwsgi
Summary:        Pgamdin4 - uwsgi configuration
Group:          Productivity/Networking/Web/Utilities
Requires:       pgadmin4
Requires:       uwsgi

%description web-uwsgi
pgadmin4 is a management tool for PostgreSQL.

This package holds the uwsgi configuration.

%package desktop
Summary:        Desktop application for pgAdmin4
Group:          Documentation/HTML
Requires:       %{name}
Requires:       python3-PyQt6

%description desktop
pgAdmin 4 is a rewrite of the pgAdmin3 management tool for the
PostgreSQL database.

This package provides a small python script that can be used
to start pgAdmin4 as a regular user and provides a simple ui
as a system tray icon to open more windows or quit.

Note that his script is not related to the official pgAdmin4
runtime application and is NOT supported by the pgAdmin project
but only provided for convenience.

%prep
%autosetup -p1

sed -e 's@PYTHONSITELIB@%{python3_sitelib}@g' <%{SOURCE1} > %{name}.conf
sed -e 's@PYTHONDIR@%{_bindir}/python3@g' -e 's@PYTHONSITELIB@%{python3_sitelib}@g' < %{SOURCE2} > %{name}.service
sed -e 's@PYTHONDIR@%{_bindir}/python3@g' -e 's@PYTHONSITELIB@%{python3_sitelib}@g' < %{SOURCE4} > %{name}.desktop
sed -e 's@PYTHONSITELIB@%{python3_sitelib}@g' <%{SOURCE7} > %{name}.uwsgi
sed -e 's@PYTHONSITELIB@%{python3_sitelib}@g' <%{SOURCE9} > README.SUSE.uwsgi

# speaklater isn't really used
sed -i -e 's/^speaklater.*//' requirements.txt

cp %{SOURCE8} .
cp %{SOURCE9} .

# rpmlint
chmod -x docs/en_US/theme/pgadmin4/static/style.css
chmod -x docs/en_US/theme/pgadmin4/theme.conf
# This package is run using the interpreter so it doesn't need the executable bit set
chmod -x web/pgadmin/misc/bgprocess/process_executor.py
chmod -x web/pgadmin/static/fonts/*.ttf

# Uncompress the vendor sources
tar xvfJ %{SOURCE12}
# Use the system optipng, not the one built when creating the vendor package in the developer workstation
ln -s %{_bindir}/optipng web/node_modules/optipng-bin/vendor/optipng

# Do not use env as script interpreter
find web/node_modules -type f -executable -exec sed -i -e '1{s,^#! */usr/bin/env \(node\|python3|bash\),#!%{_bindir}/\1,}' "{}" \;
find web/pgacloud -type f -executable -exec sed -i -e '1{s,^#! */usr/bin/env \(node\|python3\),#!%{_bindir}/\1,}' "{}" \;

rm web/regression/.gitignore

%build
make bundle
rm -Rf web/node_modules web/yarn.lock

export EVENTLET_NO_GREENDNS='yes'
mkdir -p pip-build/pgadmin4
cp -a web/* pip-build/pgadmin4
echo recursive-include pgadmin4 \* > pip-build/MANIFEST.in
find pip-build -name '.gitignore' -o -name '.coverage*' -delete
cat << EOF > pip-build/pgadmin4/config_distro.py
# SERVER_MODE = True
MINIFY_HTML = False
HTML_HELP = '%{_datadir}/doc/%{name}-docs/en_US/html/'
UPGRADE_CHECK_ENABLED = False
DEFAULT_BINARY_PATHS = {
    "pg": "%{_bindir}"
}
EOF
pushd pip-build
python3 ../pkg/pip/setup_pip.py bdist_wheel
popd
mv -v pip-build/dist/*.whl .

%install
%pyproject_install
mkdir -p %{buildroot}%{_docdir}/%{name}
cp README.md %{buildroot}%{_docdir}/%{name}

install -d -m 755 %{buildroot}%{_docdir}/%{name}-docs/
cp -pr docs/* %{buildroot}%{_docdir}/%{name}-docs
find %{buildroot}%{_docdir}/%{name}-docs -name '.gitignore' -delete

install -d %{buildroot}%{_sysconfdir}/apache2/conf.d/
install -m 0644 -p %{name}.conf %{buildroot}%{_sysconfdir}/apache2/conf.d/%{name}.conf

# Install desktop file
install -d %{buildroot}%{_datadir}/applications/
install -m 0644 -p %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

# Install config system for webapp
install -d -m 0755 %{buildroot}%{_sysconfdir}/pgadmin/
echo "# SERVER_MODE = True" > %{buildroot}%{_sysconfdir}/pgadmin/config_system.py

# Install unit file/init script
# This is only for systemd supported distros:
install -d %{buildroot}%{_unitdir}
install -m 0644 -p %{name}.service %{buildroot}%{_unitdir}/%{name}.service

# ... and make a tmpfiles script to recreate it at reboot.
mkdir -p %{buildroot}/%{_tmpfilesdir}
install -m 0644 %{SOURCE3} %{buildroot}/%{_tmpfilesdir}/%{name}.conf

chmod -x %{buildroot}%{_docdir}/%{name}-docs/en_US/images/*
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcpgadmin4

install -d -m 0755 %{buildroot}%{pgadmin4homedir}
install -d -m 0755 %{buildroot}%{pgadmin4homedir}/storage
install -d -m 0700 %{buildroot}%{pgadmin4homedir}/sessions
install -d -m 0755 %{buildroot}%{_localstatedir}/log/pgadmin

install -d -m 0755 %{buildroot}%{_sysconfdir}/uwsgi/vassals
install -m 0644 %{name}.uwsgi %{buildroot}%{_sysconfdir}/uwsgi/vassals/pgadmin4.ini

install -d -m 0755 %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -m 0644 web/pgadmin/static/img/logo-256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/pgadmin4.png

install -d -m 0755 %{buildroot}%{python3_sitelib}/%{name}/assets
install -m 0644 ./runtime/assets/welcome_logo.svg %{buildroot}%{python3_sitelib}/%{name}/assets/welcome_logo.svg

install -m 0755 %{SOURCE13} %{buildroot}%{_bindir}

%fdupes %{buildroot}%{python3_sitelib}

##%% check
## Requires Postgres running
##PYTHONPATH=%%{buildroot}%%{python3_sitelib} python3 -B web/regression/runtests.py --exclude feature_tests

%pre
/usr/sbin/groupadd -r %{user_group_name} &>/dev/null || :
/usr/sbin/useradd  -g %{user_group_name} -s /bin/false -r -c "%{name}" -d %{pgadmin4homedir} %{user_group_name} &>/dev/null || :
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf

%preun
%service_del_preun %{name}.service

%postun
chown -R %{user_group_name}:%{user_group_name} %{pgadmin4homedir}
%service_del_postun %{name}.service

%files
%defattr(-,root,root,-)
%doc README.md README.SUSE
%license LICENSE
%{_bindir}/pgadmin4

%dir %{_sysconfdir}/apache2
%dir %{_sysconfdir}/apache2/conf.d
%config(noreplace) %{_sysconfdir}/apache2/conf.d/%{name}.conf

%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}.dist-info

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
%dir %{_localstatedir}/log/pgadmin

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

%files desktop
%defattr(-,root,root,-)
%{_bindir}/pgadmin4-desktop
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/pgadmin4.png

%changelog
