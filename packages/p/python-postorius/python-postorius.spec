#
# spec file for package python-postorius
#
# Copyright (c) 2024 SUSE LLC
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


%bcond_without testsuite

# keep in sync with setup.py
%global django_mailman3_min_version 1.3.13
%global django_min_version 4.2
%global django_max_version 5.1
%global mailmanclient_min_version 3.3.3

%global srv_www_dir /srv/www
%global webapps_dir %{srv_www_dir}/webapps

%global postorius_pkgname   postorius

%global postorius_basedir   %{webapps_dir}/mailman/postorius
%global postorius_localedir %{postorius_basedir}/locale
%global postorius_staticdir %{postorius_basedir}/static

%global postorius_etcdir    %{_sysconfdir}/postorius
%global postorius_libdir    %{_localstatedir}/lib/postorius
%global postorius_logdir    %{_localstatedir}/log/postorius
%global postorius_datadir   %{postorius_libdir}/data

# keep in sync with python-HyperKitty/python-mailman-web
# Always only build one flavor: primary python for TW, python311 from the SLE15 python module for 15.x
%if 0%{?suse_version} >= 1550
%define pythons python3
%else
%{?sle15_python_module_pythons}
%endif
%global mypython %pythons
%global mypython_sitelib %{expand:%%{%{mypython}_sitelib}}
%global __mypython %{expand:%%{__%{mypython}}}

Name:           python-postorius
Version:        1.3.13
Release:        0
Summary:        A web user interface for GNU Mailman
License:        GPL-3.0-only
URL:            https://gitlab.com/mailman/postorius
#
Source0:        https://gitlab.com/mailman/postorius/-/releases/v%{version}/downloads/postorius-%{version}.tar.gz
Source1:        https://gitlab.com/mailman/postorius/-/releases/v%{version}/downloads/postorius-%{version}.tar.gz.asc
Source2:        python-postorius.keyring
Source3:        python-postorius-rpmlintrc
#
Source10:       postorius-manage.sh
Source12:       postorius.uwsgi
#
Source20:       README.SUSE.md
#
Patch0:         postorius-settings.patch
#
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  acl
BuildRequires:  fdupes
BuildRequires:  openssl
BuildRequires:  python-rpm-macros
BuildRequires:  rsync
BuildRequires:  sudo
BuildArch:      noarch
%if 0%{?suse_version} >= 1550
# use the real python3 primary for rpm pythondistdeps.py
BuildRequires:  python3-packaging
%endif
# SECTION test requirements
BuildRequires:  mailman3 >= 3.3.5
BuildRequires:  %{python_module Django >= %{django_min_version} with %python-Django < %{django_max_version}}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module cmarkgfm}
BuildRequires:  %{python_module django-debug-toolbar >= 2.2}
BuildRequires:  %{python_module django-mailman3 >= %{django_mailman3_min_version}}
BuildRequires:  %{python_module django-requests-debug-toolbar >= 0.0.3}
BuildRequires:  %{python_module isort}
BuildRequires:  %{python_module mailmanclient >= %{mailmanclient_min_version}}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module readme_renderer}
BuildRequires:  %{python_module vcrpy}
# /SECTION
%python_subpackages

%description
A web user interface for GNU Mailman

%package -n %{postorius_pkgname}
Summary:        A web user interface for GNU Mailman
Requires:       %{mypython}-django-debug-toolbar >= 2.2.0
Requires:       %{mypython}-django-mailman3 >= %{django_mailman3_min_version}
Requires:       %{mypython}-django-requests-debug-toolbar >= 0.0.3
Requires:       %{mypython}-mailmanclient >= %{mailmanclient_min_version}
Requires:       %{mypython}-readme_renderer
Requires:       (%{mypython}-Django >= %{django_min_version} with %{mypython}-Django < %{django_max_version})
# help in replacing any previously installed flavor package back to the unprefixed package
%if 0%{?suse_version} < 1550
Obsoletes:      python3-%{postorius_pkgname} < %{version}-%{release}
%endif
Provides:       %{mypython}-%{postorius_pkgname} = %{version}-%{release}
Obsoletes:      %{mypython}-%{postorius_pkgname} < %{version}-%{release}

%description  -n %{postorius_pkgname}
A web user interface for GNU Mailman

%package -n %{postorius_pkgname}-web
Summary:        The webroot for GNU Mailman
Requires:       %{postorius_pkgname}
Requires:       acl
Requires:       openssl
Requires:       sudo
Requires:       system-user-%{postorius_pkgname}

%description -n %{postorius_pkgname}-web
A web user interface for GNU Mailman.

This package holds the web interface.

%package -n %{postorius_pkgname}-web-uwsgi
Summary:        Postorius - uwsgi configuration
Requires:       %{postorius_pkgname}-web
%if 0%{suse_version} >= 1550 || 0%{?sle_version} >= 150500
Requires:       %{mypython}-uwsgi-python3
%else
Requires:       uwsgi-python3
%endif

%description -n %{postorius_pkgname}-web-uwsgi
A web user interface for GNU Mailman.

This package holds the uwsgi configuration.

%package -n system-user-%{postorius_pkgname}
Summary:        System user for HyperKitty
BuildArch:      noarch
BuildRequires:  sysuser-tools
%sysusers_requires

%description -n system-user-%{postorius_pkgname}
System user for HyperKitty.

%prep
%setup -q -n postorius-%{version}
cp %{SOURCE20} .
touch settings_local.py

# Copy exmaple_project to just build the static files
rsync -a example_project/* build_static_files

%autopatch -p1

tee > %{postorius_pkgname}.sysuser <<EOF
u %{postorius_pkgname} - "Postorius" %{postorius_basedir} -
EOF

%build
sed -i 's|^#!/usr/bin/env.*|#!%{__mypython}|' \
    example_project/manage.py
sed -i 's|/usr/bin/python3|%{__mypython}|' %{SOURCE10}
sed -i 's|python3|%{mypython}|' %{SOURCE12}

%pyproject_wheel

# Build static files
install -d -m 0755 build_static_files/logs
export PYTHONPATH=$(pwd)/src
%python_exec build_static_files/manage.py collectstatic --clear --noinput

%sysusers_generate_pre %{postorius_pkgname}.sysuser %{postorius_pkgname}

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

install -d -m 0750 \
    %{buildroot}%{postorius_etcdir} \
    %{buildroot}%{postorius_libdir} \
    %{buildroot}%{postorius_datadir} \
    %{buildroot}%{postorius_logdir}

install -d -m 0755 \
    %{buildroot}%{postorius_basedir} \
    %{buildroot}%{postorius_localedir} \
    %{buildroot}%{postorius_staticdir} \

# Copy static files
rsync -a build_static_files/static %{buildroot}%{postorius_basedir}

rsync -a example_project/* %{buildroot}%{postorius_basedir}
chmod -x %{buildroot}%{postorius_basedir}/wsgi.py

%python_expand rm -rf %{buildroot}%{$python_sitelib}/example_project

rm -f %{buildroot}%{postorius_basedir}/README.rst
rm -f %{buildroot}%{postorius_basedir}/mailman.cfg
rm -f %{buildroot}%{postorius_basedir}/logs/.keep

# Create an empty settings_local.py. This will be filled with a SECRET_KEY in post
install -m 0644 settings_local.py %{buildroot}%{postorius_etcdir}/settings_local.py

ln -svf %{postorius_etcdir}/settings_local.py \
    %{buildroot}/%{postorius_basedir}/settings_local.py

%fdupes %{buildroot}%{postorius_basedir}

# Manage script
install -d -m 0755 %{buildroot}%{_sbindir}
install -m 0750 %{SOURCE10} %{buildroot}%{_sbindir}/postorius-manage

install -d -m 0755 %{buildroot}%{_sysconfdir}/uwsgi/vassals
install -m 0644 %{SOURCE12} %{buildroot}%{_sysconfdir}/uwsgi/vassals/postorius.ini

install -d -m 0755 %{buildroot}%{_sysusersdir}
install -m 0644 %{postorius_pkgname}.sysuser %{buildroot}%{_sysusersdir}/%{postorius_pkgname}.conf

%if %{with testsuite}
%check
export PYTHONPATH="$(pwd):$(pwd)/src"
export LANG=C.UTF-8
%pytest
# clean flavored alternatives created by test setup, because we are going to install the example_project as docs
rm -rf build/flavorbin
rm -rf build/xdgflavorconfig
%endif

%pre -n %{postorius_pkgname}-web
/usr/sbin/groupadd -r postorius &>/dev/null || :
/usr/sbin/useradd  -g postorius -s /bin/false -r -c "Postorius" -d %{postorius_basedir} postorius &>/dev/null || :

%post -n %{postorius_pkgname}-web
# We need a SECRET_KEY for manage to work
if ! grep -q "^SECRET_KEY.*" %{postorius_etcdir}/settings_local.py; then
    echo "SECRET_KEY='$(openssl rand -base64 48)'" >> %{postorius_etcdir}/settings_local.py
fi
%{_sbindir}/postorius-manage makemigrations --pythonpath /srv/www/webapps/mailman/postorius/ --settings settings
%{_sbindir}/postorius-manage migrate --pythonpath /srv/www/webapps/mailman/postorius/ --settings settings

%pre -n system-user-%{postorius_pkgname} -f %{postorius_pkgname}.pre

%files -n %{postorius_pkgname}
%doc README.rst example_project src/postorius/doc/*.rst
%license COPYING
%{mypython_sitelib}/postorius
%{mypython_sitelib}/postorius-%{version}*-info

%files -n %{postorius_pkgname}-web
%doc README.SUSE.md
%{_sbindir}/postorius-manage
%dir %{webapps_dir}
%dir %{webapps_dir}/mailman

%dir %{srv_www_dir}
%attr(-,root,postorius) %dir %{postorius_basedir}
%attr(-,root,postorius) %{postorius_basedir}/__init__.py
%attr(-,root,postorius) %{postorius_basedir}/manage.py
%attr(-,root,postorius) %{postorius_basedir}/settings.py
%attr(-,root,postorius) %{postorius_basedir}/settings_local.py
%attr(-,root,postorius) %{postorius_basedir}/test_settings.py
%attr(-,root,postorius) %{postorius_basedir}/urls.py
%attr(-,root,postorius) %{postorius_basedir}/wsgi.py

%attr(-,root,postorius) %dir %{postorius_basedir}/static
%attr(-,root,postorius) %{postorius_basedir}/static/admin
%attr(-,root,postorius) %{postorius_basedir}/static/django-mailman3
%attr(-,root,postorius) %{postorius_basedir}/static/postorius
%attr(-,root,postorius) %{postorius_basedir}/static/debug_toolbar

%attr(750,root,postorius) %dir %{postorius_etcdir}
%attr(640,root,postorius) %config(noreplace) %{postorius_etcdir}/settings_local.py
%attr(750,root,postorius) %dir %{postorius_libdir}
%attr(750,postorius,postorius) %dir %{postorius_datadir}
%attr(750,postorius,postorius) %dir %{postorius_logdir}

%files -n %{postorius_pkgname}-web-uwsgi
%dir %{_sysconfdir}/uwsgi
%dir %{_sysconfdir}/uwsgi/vassals
%config (noreplace) %{_sysconfdir}/uwsgi/vassals/postorius.ini

%files -n system-user-%{postorius_pkgname}
%{_sysusersdir}/%{postorius_pkgname}.conf

%changelog
