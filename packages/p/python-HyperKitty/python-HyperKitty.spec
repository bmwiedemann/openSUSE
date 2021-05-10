#
# spec file for package python-HyperKitty
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

%global hyperkitty_pkgname   HyperKitty

%global hyperkitty_basedir   %{webapps_dir}/mailman/hyperkitty
%global hyperkitty_localedir %{hyperkitty_basedir}/locale
%global hyperkitty_staticdir %{hyperkitty_basedir}/static

%global hyperkitty_etcdir    %{_sysconfdir}/hyperkitty
%global hyperkitty_libdir    %{_localstatedir}/lib/hyperkitty
%global hyperkitty_logdir    %{_localstatedir}/log/hyperkitty
%global hyperkitty_datadir   %{hyperkitty_libdir}/data

%global hyperkitty_services hyperkitty-qcluster.service hyperkitty-runjob-daily.service hyperkitty-runjob-daily.timer hyperkitty-runjob-hourly.service hyperkitty-runjob-hourly.timer hyperkitty-runjob-minutely.service hyperkitty-runjob-minutely.timer hyperkitty-runjob-monthly.service hyperkitty-runjob-monthly.timer hyperkitty-runjob-quarter-hourly.service hyperkitty-runjob-quarter-hourly.timer hyperkitty-runjob-weekly.service hyperkitty-runjob-weekly.timer hyperkitty-runjob-yearly.service hyperkitty-runjob-yearly.timer

%{?!python_module:%define python_module() python3-%{**}}
# mailman is built only for primary python3 flavor
%define pythons python3
Name:           python-HyperKitty
Version:        1.3.4
Release:        0
Summary:        A web interface to access GNU Mailman v3 archives
License:        GPL-3.0-only
URL:            https://gitlab.com/mailman/hyperkitty
#
Source0:        https://files.pythonhosted.org/packages/source/H/HyperKitty/HyperKitty-%{version}.tar.gz
Source1:        python-HyperKitty-rpmlintrc
#
Source10:       hyperkitty-manage.sh
Source11:       hyperkitty-permissions.sh
Source12:       hyperkitty.uwsgi
#
Source20:       hyperkitty-qcluster.service
Source21:       hyperkitty-runjob.service
Source22:       hyperkitty-runjob.timer
#
Source30:       README.SUSE.md
#
Patch0:         hyperkitty-settings.patch
#
BuildRequires:  %{python_module django-debug-toolbar >= 2.2}
BuildRequires:  %{python_module isort}
BuildRequires:  %{python_module libsass}
BuildRequires:  %{python_module setuptools}
BuildRequires:  acl
BuildRequires:  fdupes
BuildRequires:  openssl
BuildRequires:  python-rpm-macros
BuildRequires:  sudo
Requires:       python-Django >= 1.11
Requires:       python-django-compressor >= 1.3
Requires:       python-django-debug-toolbar >= 2.2
Requires:       python-django-extensions >= 1.3.7
Requires:       python-django-gravatar2 >= 1.0.6
Requires:       python-django-haystack >= 2.8.0
Requires:       python-django-mailman3 >= 1.2.0
Requires:       python-django-q >= 1.0.0
Requires:       python-djangorestframework >= 3.0.0
Requires:       python-flufl.lock
Requires:       python-libsass
Requires:       python-mailmanclient >= 3.1.1
Requires:       python-networkx >= 1.9.1
Requires:       python-python-dateutil >= 2.0
Requires:       python-pytz >= 2012
Requires:       python-robot-detection >= 0.3
Requires:       python-xapian-haystack >= 2.1.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module Whoosh >= 2.5.7}
BuildRequires:  %{python_module beautifulsoup4 >= 4.3.2}
BuildRequires:  %{python_module django-compressor >= 1.3}
BuildRequires:  %{python_module django-extensions >= 1.3.7}
BuildRequires:  %{python_module django-gravatar2 >= 1.0.6}
BuildRequires:  %{python_module django-haystack >= 2.8.0}
BuildRequires:  %{python_module django-mailman3 >= 1.2.0}
BuildRequires:  %{python_module django-q >= 1.0.0}
BuildRequires:  %{python_module djangorestframework >= 3.0.0}
BuildRequires:  %{python_module elasticsearch}
BuildRequires:  %{python_module flufl.lock}
BuildRequires:  %{python_module mailmanclient >= 3.1.1}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module networkx >= 1.9.1}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.0}
BuildRequires:  %{python_module pytz >= 2012}
BuildRequires:  %{python_module robot-detection >= 0.3}
# /SECTION
%if 0%{python3_version_nodots} == 38
# help in replacing any previously installed multiflavor package back to the primary python3 package
Provides:       python38-Hyperkitty = %{version}-%{release}
Obsoletes:      python38-Hyperkitty < %{version}-%{release}
%endif
%python_subpackages

%description
A web interface to access GNU Mailman v3 archives.

%package -n %{hyperkitty_pkgname}-web
Summary:        The webroot for GNU Mailman
Requires:       acl
Requires:       openssl
Requires:       python3-HyperKitty
Requires:       sudo

%description -n %{hyperkitty_pkgname}-web
A web user interface for GNU Mailman.

This package holds the web interface.

%package -n %{hyperkitty_pkgname}-web-uwsgi
Summary:        HyperKitty - uwsgi configuration
Requires:       %{hyperkitty_pkgname}-web
Requires:       uwsgi

%description -n %{hyperkitty_pkgname}-web-uwsgi
A web user interface for GNU Mailman.

This package holds the uwsgi configuration.

%prep
%autosetup -p1 -n HyperKitty-%{version}
cp %{SOURCE30} .
touch settings_local.py

%build
sed -i 's|^#!/usr/bin/env.*|#!%{_bindir}/python3|' \
    example_project/manage.py

%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

install -d -m 0750 \
    %{buildroot}%{hyperkitty_etcdir} \
    %{buildroot}%{hyperkitty_libdir} \
    %{buildroot}%{hyperkitty_datadir} \
    %{buildroot}%{hyperkitty_datadir}/attachments \
    %{buildroot}%{hyperkitty_logdir}

install -d -m 0755 \
    %{buildroot}%{hyperkitty_basedir} \
    %{buildroot}%{hyperkitty_localedir} \
    %{buildroot}%{hyperkitty_staticdir} \
    %{buildroot}%{hyperkitty_staticdir}/CACHE \
    %{buildroot}%{_unitdir}

cp -a example_project/* %{buildroot}%{hyperkitty_basedir}
chmod -x %{buildroot}%{hyperkitty_basedir}/wsgi.py

for f in \
         README.rst \
         apache.conf \
         crontab \
         qcluster.service \
    ; do
    rm -f %{buildroot}%{hyperkitty_basedir}/$f
done
rm -f %{buildroot}%{hyperkitty_localedir}/.keep
rm -f %{buildroot}%{hyperkitty_basedir}/logs/.keep

%python_expand rm -rf %{buildroot}%{$python_sitelib}/example_project

# Create an empty settings_local.py. This will be filled with a SECRET_KEY in post
install -m 0644 settings_local.py %{buildroot}%{hyperkitty_etcdir}/settings_local.py

ln -svf %{hyperkitty_etcdir}/settings_local.py \
    %{buildroot}/%{hyperkitty_basedir}/settings_local.py

%fdupes %{buildroot}%{hyperkitty_basedir}

# Manage script
install -d -m 0755 %{buildroot}%{_sbindir}
install -m 0750 %{SOURCE10} %{buildroot}%{_sbindir}/hyperkitty-manage
install -m 0750 %{SOURCE11} %{buildroot}%{_sbindir}/hyperkitty-fix-permissions

install -d -m 0755 %{buildroot}%{_sysconfdir}/uwsgi/vassals
install -m 0644 %{SOURCE12} %{buildroot}%{_sysconfdir}/uwsgi/vassals/hyperkitty.ini

install -m 0644 %{SOURCE20} %{buildroot}%{_unitdir}/hyperkitty-qcluster.service
ln -s /sbin/service %{buildroot}%{_sbindir}/rchyperkitty-qcluster

for job in \
           minutely \
           quarter-hourly \
           hourly \
           daily \
           weekly \
           monthly \
           yearly \
           ; do
    install -m 0644 %{SOURCE21} %{buildroot}%{_unitdir}/hyperkitty-runjob-${job}.service
    sed -i "s/@HYPERKITTY_RUNJOB@/${job}/g" %{buildroot}%{_unitdir}/hyperkitty-runjob-${job}.service
    ln -s /sbin/service %{buildroot}%{_sbindir}/rchyperkitty-runjob-${job}

    install -m 0644 %{SOURCE22} %{buildroot}%{_unitdir}/hyperkitty-runjob-${job}.timer

    hyperkitty_runjob_calendar="OnCalendar=${job}"
    hyperkitty_runjob_delay="RandomizedDelaySec=15m"
    hyperkitty_runjob_name="${job}"

    if [ "${job}" = "minutely" ]; then
        hyperkitty_runjob_delay="RandomizedDelaySec=15s"
    elif [ "${job}" = "quarter-hourly" ]; then
        hyperkitty_runjob_calendar="OnCalendar=*:0/15"
        hyperkitty_runjob_delay="RandomizedDelaySec=2m"
        # The real jobname is with an underscore
        hyperkitty_runjob_name="quarter_hourly"
    fi
    sed -i "s#@HYPERKITTY_RUNJOB_CALENDAR@#${hyperkitty_runjob_calendar}#g" %{buildroot}%{_unitdir}/hyperkitty-runjob-${job}.timer
    sed -i "s#@HYPERKITTY_RUNJOB_DELAY@#${hyperkitty_runjob_delay}#g" %{buildroot}%{_unitdir}/hyperkitty-runjob-${job}.timer
    sed -i "s#@HYPERKITTY_RUNJOB@#${hyperkitty_runjob_name}#g" %{buildroot}%{_unitdir}/hyperkitty-runjob-${job}.timer
done

%check
export DJANGO_SETTINGS_MODULE="hyperkitty.tests.settings_test"
export PYTHONPATH='.'
%python_exec example_project/manage.py test

%pre -n %{hyperkitty_pkgname}-web
/usr/sbin/groupadd -r hyperkitty &>/dev/null || :
/usr/sbin/useradd  -g hyperkitty -s /bin/false -r -c "HyperKitty" -d %{hyperkitty_basedir} hyperkitty &>/dev/null || :

/usr/sbin/groupadd -r hyperkitty-admin &>/dev/null || :
/usr/sbin/useradd  -g hyperkitty-admin -s /bin/bash  -r -c "HyperKitty Admin" -d %{hyperkitty_basedir} hyperkitty-admin &>/dev/null || :

%service_add_pre %{hyperkitty_services}

%post -n %{hyperkitty_pkgname}-web
%{_sbindir}/hyperkitty-fix-permissions
# We need a SECRET_KEY for manage to work
if ! grep -q "^SECRET_KEY.*" %{hyperkitty_etcdir}/settings_local.py; then
    echo "SECRET_KEY='$(openssl rand -base64 48)'" >> %{hyperkitty_etcdir}/settings_local.py
fi
%{_sbindir}/hyperkitty-manage migrate --pythonpath /srv/www/webapps/mailman/hyperkitty/ --settings settings
%{_sbindir}/hyperkitty-manage collectstatic --pythonpath /srv/www/webapps/mailman/hyperkitty/ --settings settings --clear --noinput
%{_sbindir}/hyperkitty-manage compress --pythonpath /srv/www/webapps/mailman/hyperkitty/ --settings settings --force
# Run hyperkitty-fix-permissions again for cache dir permissions
%{_sbindir}/hyperkitty-fix-permissions

%service_add_post %{hyperkitty_services}

%preun -n %{hyperkitty_pkgname}-web
%service_del_preun %{hyperkitty_services}

%postun -n %{hyperkitty_pkgname}-web
%service_del_postun %{hyperkitty_services}

%files %{python_files}
%doc AUTHORS.txt README.rst example_project doc/*.rst
%license COPYING.txt
%{python_sitelib}/hyperkitty
%{python_sitelib}/HyperKitty*.egg-info

%files -n %{hyperkitty_pkgname}-web
%doc README.SUSE.md
%{_sbindir}/hyperkitty-manage
%{_sbindir}/hyperkitty-fix-permissions
%{_sbindir}/rchyperkitty-qcluster
%{_sbindir}/rchyperkitty-runjob-*
%dir %{webapps_dir}
%dir %{webapps_dir}/mailman
%{_unitdir}/hyperkitty-qcluster.service
%{_unitdir}/hyperkitty-runjob-*.service
%{_unitdir}/hyperkitty-runjob-*.timer

%defattr(-,hyperkitty-admin,hyperkitty)
%dir %{hyperkitty_basedir}
%{hyperkitty_basedir}/__init__.py
%{hyperkitty_basedir}/manage.py
%{hyperkitty_basedir}/settings.py
%{hyperkitty_basedir}/settings_local.py
%{hyperkitty_basedir}/urls.py
%{hyperkitty_basedir}/wsgi.py

%dir %{hyperkitty_localedir}

%dir %{hyperkitty_staticdir}
%dir %{hyperkitty_staticdir}/CACHE

%attr(750,hyperkitty-admin,hyperkitty) %dir %{hyperkitty_etcdir}
%attr(640,hyperkitty-admin,hyperkitty) %config(noreplace) %{hyperkitty_etcdir}/settings_local.py
%attr(750,hyperkitty-admin,hyperkitty) %dir %{hyperkitty_libdir}
%attr(750,hyperkitty-admin,hyperkitty) %dir %{hyperkitty_datadir}
%attr(750,hyperkitty-admin,hyperkitty) %dir %{hyperkitty_logdir}

%files -n %{hyperkitty_pkgname}-web-uwsgi
%dir %{_sysconfdir}/uwsgi
%dir %{_sysconfdir}/uwsgi/vassals
%config (noreplace) %{_sysconfdir}/uwsgi/vassals/hyperkitty.ini

%changelog
