#
# spec file for package python-postorius
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


%global webapps_dir /srv/www/webapps

%global postorius_pkgname   postorius

%global postorius_basedir   %{webapps_dir}/mailman/postorius
%global postorius_localedir %{postorius_basedir}/locale
%global postorius_staticdir %{postorius_basedir}/static

%global postorius_etcdir    %{_sysconfdir}/postorius
%global postorius_libdir    %{_localstatedir}/lib/postorius
%global postorius_logdir    %{_localstatedir}/log/postorius
%global postorius_datadir   %{postorius_libdir}/data

%{?!python_module:%define python_module() python3-%{**}}
# mailman is built only for primary python3 flavor
%define pythons python3
Name:           python-postorius
Version:        1.3.4
Release:        0
Summary:        A web user interface for GNU Mailman
License:        GPL-3.0-only
URL:            https://gitlab.com/mailman/postorius
#
Source0:        https://files.pythonhosted.org/packages/source/p/postorius/postorius-%{version}.tar.gz
Source1:        python-postorius-rpmlintrc
#
Source10:       postorius-manage.sh
Source11:       postorius-permissions.sh
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
BuildRequires:  sudo
Requires:       python-Django >= 1.11
Requires:       python-django-mailman3 >= 1.2.0
Requires:       python-mailmanclient >= 3.2.3
Requires:       python-readme_renderer
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module cmarkgfm}
BuildRequires:  %{python_module django-mailman3 >= 1.2.0}
BuildRequires:  %{python_module isort}
BuildRequires:  %{python_module mailmanclient >= 3.2.3}
BuildRequires:  %{python_module mailman}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module readme_renderer}
BuildRequires:  %{python_module vcrpy}
# /SECTION
%if 0%{python3_version_nodots} == 38
# help in replacing any previously installed multiflavor package back to the primary python3 package
Provides:       python38-postorius = %{version}-%{release}
Obsoletes:      python38-postorius < %{version}-%{release}
%endif
%python_subpackages

%description
A web user interface for GNU Mailman

%package -n %{postorius_pkgname}-web
Summary:        The webroot for GNU Mailman
Requires:       acl
Requires:       openssl
Requires:       python3-postorius
Requires:       sudo

%description -n %{postorius_pkgname}-web
A web user interface for GNU Mailman.

This package holds the web interface.

%package -n %{postorius_pkgname}-web-uwsgi
Summary:        Postorius - uwsgi configuration
Requires:       %{postorius_pkgname}-web
Requires:       uwsgi

%description -n %{postorius_pkgname}-web-uwsgi
A web user interface for GNU Mailman.

This package holds the uwsgi configuration.

%prep
%autosetup -p1 -n postorius-%{version}
cp %{SOURCE20} .
touch settings_local.py

%build
sed -i 's|^#!/usr/bin/env.*|#!%{_bindir}/python3|' \
    example_project/manage.py

%python_build

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

cp -a example_project/* %{buildroot}%{postorius_basedir}
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
install -m 0750 %{SOURCE11} %{buildroot}%{_sbindir}/postorius-fix-permissions

install -d -m 0755 %{buildroot}%{_sysconfdir}/uwsgi/vassals
install -m 0644 %{SOURCE12} %{buildroot}%{_sysconfdir}/uwsgi/vassals/postorius.ini

%check
pushd example_project
export PYTHONPATH='../src'
export LANG=C.UTF-8
%pytest ..
popd

%pre -n %{postorius_pkgname}-web
/usr/sbin/groupadd -r postorius &>/dev/null || :
/usr/sbin/useradd  -g postorius -s /bin/false -r -c "Postorius" -d %{postorius_basedir} postorius &>/dev/null || :

/usr/sbin/groupadd -r postorius-admin &>/dev/null || :
/usr/sbin/useradd  -g postorius-admin -s /bin/bash  -r -c "Postorius Admin" -d %{postorius_basedir} postorius-admin &>/dev/null || :

%post -n %{postorius_pkgname}-web
%{_sbindir}/postorius-fix-permissions
# We need a SECRET_KEY for manage to work
if ! grep -q "^SECRET_KEY.*" %{postorius_etcdir}/settings_local.py; then
    echo "SECRET_KEY='$(openssl rand -base64 48)'" >> %{postorius_etcdir}/settings_local.py
fi
%{_sbindir}/postorius-manage migrate --pythonpath /srv/www/webapps/mailman/postorius/ --settings settings
%{_sbindir}/postorius-manage collectstatic --pythonpath /srv/www/webapps/mailman/postorius/ --settings settings --clear --noinput

%files %{python_files}
%doc README.rst example_project
%license COPYING
%{python_sitelib}/*

%files -n %{postorius_pkgname}-web
%doc README.SUSE.md
%{_sbindir}/postorius-manage
%{_sbindir}/postorius-fix-permissions
%dir %{webapps_dir}
%dir %{webapps_dir}/mailman

%defattr(-,postorius-admin,postorius)
%{postorius_basedir}

%attr(750,postorius-admin,postorius) %dir %{postorius_etcdir}
%attr(640,postorius-admin,postorius) %config(noreplace) %{postorius_etcdir}/settings_local.py
%attr(750,postorius-admin,postorius) %dir %{postorius_libdir}
%attr(750,postorius-admin,postorius) %dir %{postorius_datadir}
%attr(750,postorius-admin,postorius) %dir %{postorius_logdir}

%files -n %{postorius_pkgname}-web-uwsgi
%dir %{_sysconfdir}/uwsgi
%dir %{_sysconfdir}/uwsgi/vassals
%config (noreplace) %{_sysconfdir}/uwsgi/vassals/postorius.ini

%changelog
