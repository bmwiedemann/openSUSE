#
# spec file for package python-postorius
#
# Copyright (c) 2022 SUSE LLC
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


%global webapps_dir /srv/www/webapps

%global postorius_pkgname   postorius

%global postorius_basedir   %{webapps_dir}/mailman/postorius
%global postorius_localedir %{postorius_basedir}/locale
%global postorius_staticdir %{postorius_basedir}/static

%global postorius_etcdir    %{_sysconfdir}/postorius
%global postorius_libdir    %{_localstatedir}/lib/postorius
%global postorius_logdir    %{_localstatedir}/log/postorius
%global postorius_datadir   %{postorius_libdir}/data

%if 0%{?suse_version} >= 1550
# Newest python supported by mailman is Python 3.9 -- https://gitlab.com/mailman/mailman/-/issues/936
%define pythons python39
%define mypython python39
%define __mypython %{__python39}
%define mypython_sitelib %{python39_sitelib}
%else
%{?!python_module:%define python_module() python3-%{**}}
%define pythons python3
%define mypython python3
%define __mypython %{__python3}
%define mypython_sitelib %{python3_sitelib}
%endif

Name:           python-postorius
Version:        1.3.7
Release:        0
Summary:        A web user interface for GNU Mailman
License:        GPL-3.0-only
URL:            https://gitlab.com/mailman/postorius
#
Source0:        https://files.pythonhosted.org/packages/source/p/postorius/postorius-%{version}.tar.gz
Source1:        python-postorius-rpmlintrc
#
Source10:       postorius-manage.sh
Source12:       postorius.uwsgi
#
Source20:       README.SUSE.md
#
Patch0:         postorius-settings.patch
#
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
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
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module cmarkgfm}
BuildRequires:  %{python_module django-debug-toolbar >= 2.2}
BuildRequires:  %{python_module django-mailman3 >= 1.3.7}
BuildRequires:  %{python_module django-requests-debug-toolbar >= 0.0.3}
BuildRequires:  %{python_module isort}
BuildRequires:  %{python_module mailmanclient >= 3.3.3}
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
Requires:       %{mypython}-Django >= 1.11
Requires:       %{mypython}-django-debug-toolbar >= 2.2.0
Requires:       %{mypython}-django-mailman3 >= 1.3.7
Requires:       %{mypython}-django-requests-debug-toolbar >= 0.0.3
Requires:       %{mypython}-mailmanclient >= 3.3.2
Requires:       %{mypython}-readme_renderer
%if "%{expand:%%%{mypython}_provides}" == "python3"
Provides:       python3-%{postorius_pkgname} = %{version}-%{release}
%endif
Obsoletes:      python3-%{postorius_pkgname} < %{version}-%{release}
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

%description -n %{postorius_pkgname}-web
A web user interface for GNU Mailman.

This package holds the web interface.

%package -n %{postorius_pkgname}-web-uwsgi
Summary:        Postorius - uwsgi configuration
Requires:       %{postorius_pkgname}-web
%if 0%{suse_version} >= 1550
Requires:       %{mypython}-uwsgi-python3
%else
Requires:       uwsgi-python3
%endif

%description -n %{postorius_pkgname}-web-uwsgi
A web user interface for GNU Mailman.

This package holds the uwsgi configuration.

%prep
%setup -q -n postorius-%{version}
cp %{SOURCE20} .
touch settings_local.py

# Copy exmaple_project to just build the static files
rsync -a example_project/* build_static_files

%autopatch -p1

%build
sed -i 's|^#!/usr/bin/env.*|#!%{__mypython}|' \
    example_project/manage.py
sed -i 's|/usr/bin/python3|%{__mypython}|' %{SOURCE10}
sed -i 's|python3|%{mypython}|' %{SOURCE12}

%python_build

# Build static files
install -d -m 0755 build_static_files/logs
export PYTHONPATH=$(pwd)/src
%python_exec build_static_files/manage.py collectstatic --clear --noinput

%install
%python_install
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

rm -f %{buildroot}%{postorius_basedir}/README.rst
rm -f %{buildroot}%{postorius_basedir}/mailman.cfg

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

%check
export PYTHONPATH="$(pwd):$(pwd)/src"
export LANG=C.UTF-8
%pytest
# clean flavored alternatives created by test setup, because we are going to install the example_project as docs
rm -rf build/flavorbin
rm -rf build/xdgflavorconfig

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

%files -n %{postorius_pkgname}
%doc README.rst example_project
%license COPYING
%{mypython_sitelib}/postorius
%{mypython_sitelib}/postorius-%{version}*-info

%files -n %{postorius_pkgname}-web
%doc README.SUSE.md
%{_sbindir}/postorius-manage
%dir %{webapps_dir}
%dir %{webapps_dir}/mailman

%defattr(-,root,postorius)
%dir %{postorius_basedir}
%{postorius_basedir}/__init__.py
%{postorius_basedir}/manage.py
%{postorius_basedir}/settings.py
%{postorius_basedir}/settings_local.py
%{postorius_basedir}/test_settings.py
%{postorius_basedir}/urls.py
%{postorius_basedir}/wsgi.py

%dir %{postorius_basedir}/static
%{postorius_basedir}/static/admin
%{postorius_basedir}/static/django-mailman3
%{postorius_basedir}/static/postorius
%{postorius_basedir}/static/debug_toolbar

%attr(750,root,postorius) %dir %{postorius_etcdir}
%attr(640,root,postorius) %config(noreplace) %{postorius_etcdir}/settings_local.py
%attr(750,root,postorius) %dir %{postorius_libdir}
%attr(750,postorius,postorius) %dir %{postorius_datadir}
%attr(750,postorius,postorius) %dir %{postorius_logdir}

%files -n %{postorius_pkgname}-web-uwsgi
%dir %{_sysconfdir}/uwsgi
%dir %{_sysconfdir}/uwsgi/vassals
%config (noreplace) %{_sysconfdir}/uwsgi/vassals/postorius.ini

%changelog
