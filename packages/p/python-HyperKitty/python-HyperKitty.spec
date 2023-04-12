#
# spec file for package python-HyperKitty
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

Name:           python-HyperKitty
Version:        1.3.5
Release:        0
Summary:        A web interface to access GNU Mailman v3 archives
License:        GPL-3.0-only
URL:            https://gitlab.com/mailman/hyperkitty
#
Source0:        https://files.pythonhosted.org/packages/source/H/HyperKitty/HyperKitty-%{version}.tar.gz
Source1:        python-HyperKitty-rpmlintrc
#
Source10:       hyperkitty-manage.sh
Source12:       hyperkitty.uwsgi
#
Source20:       hyperkitty-qcluster.service
Source21:       hyperkitty-runjob.service
Source22:       hyperkitty-runjob.timer
#
Source30:       README.SUSE.md
#
# PATCH-FIX-OPENSUSE hyperkitty-settings.patch mcepl@suse.com
# hard-code locations of configuration files
Patch0:         hyperkitty-settings.patch
# PATCH-FIX-UPSTREAM hyperkitty-fix-mistune-2.0-imports.patch gl#mailman/hyperkitty#379 mcepl@suse.com
# Two elements moved in mistune 2.0
Patch1:         hyperkitty-fix-mistune-2.0-imports.patch
# PATCH-FIX-UPSTREAM hyperkitty-django4.patch gl#mailman/hyperkitty#384 jayvdb@gmail.com
Patch2:         hyperkitty-django4.patch
# https://gitlab.com/mailman/hyperkitty/-/issues/429
Patch3:         python-HyperKitty-no-mock.patch
# https://gitlab.com/mailman/hyperkitty/-/commit/3edc0c58b8dea3b0bdccd77c0794ada28d1c6f61
Patch4:         hyperkitty-fix-qcluster-timeout.patch
# https://gitlab.com/mailman/hyperkitty/-/merge_requests/381 + https://gitlab.com/mailman/hyperkitty/-/merge_requests/449
Patch5:         hyperkitty-fix-py310-tests.patch
# PATCH-FIX-UPSTREAM fix-django41.patch gl#mailman/hyperkitty#467
Patch6:         fix-django41.patch
# PATCH-FIX-UPSTREAM fix-elasticsearch8.patch gl#mailman/hyperkitty#468
Patch7:         fix-elasticsearch8.patch
#
BuildRequires:  %{python_module django-debug-toolbar >= 2.2}
BuildRequires:  %{python_module isort}
BuildRequires:  %{python_module libsass}
BuildRequires:  %{python_module mistune >= 2.0}
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
BuildRequires:  sassc
%endif
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module Whoosh >= 2.5.7}
BuildRequires:  %{python_module beautifulsoup4 >= 4.3.2}
BuildRequires:  %{python_module django-compressor >= 1.3}
BuildRequires:  %{python_module django-extensions >= 1.3.7}
BuildRequires:  %{python_module django-gravatar2 >= 1.0.6}
BuildRequires:  %{python_module django-haystack >= 2.8.0}
BuildRequires:  %{python_module django-mailman3 >= 1.3.7}
BuildRequires:  %{python_module django-q >= 1.3.9}
BuildRequires:  %{python_module djangorestframework >= 3.0.0}
BuildRequires:  %{python_module elasticsearch}
BuildRequires:  %{python_module flufl.lock}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module mailmanclient >= 3.3.2}
BuildRequires:  %{python_module mistune}
BuildRequires:  %{python_module networkx >= 1.9.1}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.0}
BuildRequires:  %{python_module pytz >= 2012}
BuildRequires:  %{python_module robot-detection >= 0.3}
# /SECTION

%description
A web interface to access GNU Mailman v3 archives.

%package -n %{hyperkitty_pkgname}
Summary:        A web interface to access GNU Mailman v3 archives
Requires:       %{mypython}-Django >= 1.11
Requires:       %{mypython}-django-compressor >= 1.3
Requires:       %{mypython}-django-debug-toolbar >= 2.2
Requires:       %{mypython}-django-extensions >= 1.3.7
Requires:       %{mypython}-django-gravatar2 >= 1.0.6
Requires:       %{mypython}-django-haystack >= 2.8.0
Requires:       %{mypython}-django-mailman3 >= 1.3.7
Requires:       %{mypython}-django-q >= 1.3.9
Requires:       %{mypython}-djangorestframework >= 3.0.0
Requires:       %{mypython}-flufl.lock
Requires:       %{mypython}-libsass
Requires:       %{mypython}-mailmanclient >= 3.3.2
Requires:       %{mypython}-mistune
Requires:       %{mypython}-networkx >= 1.9.1
Requires:       %{mypython}-python-dateutil >= 2.0
Requires:       %{mypython}-pytz >= 2012
Requires:       %{mypython}-robot-detection >= 0.3
Requires:       %{mypython}-xapian-haystack >= 2.1.0
%if "%{expand:%%%{mypython}_provides}" == "python3"
Provides:       python3-%{hyperkitty_pkgname} = %{version}-%{release}
%endif
Obsoletes:      python3-%{hyperkitty_pkgname} < %{version}-%{release}
Provides:       %{mypython}-%{hyperkitty_pkgname} = %{version}-%{release}
Obsoletes:      %{mypython}-%{hyperkitty_pkgname} < %{version}-%{release}
%if 0%{?suse_version} >= 1550
Requires:       sassc
%endif

%description -n %{hyperkitty_pkgname}
A web interface to access GNU Mailman v3 archives.

%package -n %{hyperkitty_pkgname}-web
Summary:        The webroot for GNU Mailman
Requires:       %{hyperkitty_pkgname}
Requires:       acl
Requires:       openssl
Requires:       sudo

%description -n %{hyperkitty_pkgname}-web
A web user interface for GNU Mailman.

This package holds the web interface.

%package -n %{hyperkitty_pkgname}-web-uwsgi
Summary:        HyperKitty - uwsgi configuration
Requires:       %{hyperkitty_pkgname}-web
%if 0%{suse_version} >= 1550
Requires:       %{mypython}-uwsgi-python3
%else
Requires:       uwsgi-python3
%endif

%description -n %{hyperkitty_pkgname}-web-uwsgi
A web user interface for GNU Mailman.

This package holds the uwsgi configuration.

%prep
%setup -n HyperKitty-%{version}
cp %{SOURCE30} .
touch settings_local.py

%patch2 -p1

# Copy example_project to just build the static files
rsync -a example_project/* build_static_files

%patch0 -p1
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
sed -i 's|^#!/usr/bin/env.*|#!%{__mypython}|' \
    example_project/manage.py
sed -i 's|/usr/bin/python3|%{__mypython}|' %{SOURCE10} %{SOURCE20} %{SOURCE21}
sed -i 's|python3|%{mypython}|' %{SOURCE12}

%python_build

# Build static files
export PYTHONPATH=$(pwd)
%python_exec build_static_files/manage.py collectstatic --clear --noinput
%python_exec build_static_files/manage.py compress --force

%install
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

%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Copy static files
rsync -a build_static_files/static %{buildroot}%{hyperkitty_basedir}
# Remove the directory
rm -rf %{buildroot}%{python_sitelib}/build_static_files

rsync -a example_project/* %{buildroot}%{hyperkitty_basedir}
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
export PYTHONPATH=$(pwd)
%python_exec example_project/manage.py test

%pre -n %{hyperkitty_pkgname}-web
/usr/sbin/groupadd -r hyperkitty &>/dev/null || :
/usr/sbin/useradd  -g hyperkitty -s /bin/false -r -c "HyperKitty" -d %{hyperkitty_basedir} hyperkitty &>/dev/null || :

%service_add_pre %{hyperkitty_services}

%post -n %{hyperkitty_pkgname}-web
# We need a SECRET_KEY for manage to work
if ! grep -q "^SECRET_KEY.*" %{hyperkitty_etcdir}/settings_local.py; then
    echo "SECRET_KEY='$(openssl rand -base64 48)'" >> %{hyperkitty_etcdir}/settings_local.py
fi
%{_sbindir}/hyperkitty-manage makemigrations --pythonpath /srv/www/webapps/mailman/hyperkitty/ --settings settings
%{_sbindir}/hyperkitty-manage migrate --pythonpath /srv/www/webapps/mailman/hyperkitty/ --settings settings

%service_add_post %{hyperkitty_services}

%preun -n %{hyperkitty_pkgname}-web
%service_del_preun %{hyperkitty_services}

%postun -n %{hyperkitty_pkgname}-web
%service_del_postun %{hyperkitty_services}

%files -n %{hyperkitty_pkgname}
%doc AUTHORS.txt README.rst example_project doc/*.rst
%license COPYING.txt
%{mypython_sitelib}/hyperkitty
%{mypython_sitelib}/HyperKitty-%{version}*-info

%files -n %{hyperkitty_pkgname}-web
%doc README.SUSE.md
%{_sbindir}/hyperkitty-manage
%{_sbindir}/rchyperkitty-qcluster
%{_sbindir}/rchyperkitty-runjob-*
%dir %{webapps_dir}
%dir %{webapps_dir}/mailman
%{_unitdir}/hyperkitty-qcluster.service
%{_unitdir}/hyperkitty-runjob-*.service
%{_unitdir}/hyperkitty-runjob-*.timer

%defattr(-,root,hyperkitty)
%dir %{hyperkitty_basedir}
%{hyperkitty_basedir}/__init__.py
%{hyperkitty_basedir}/manage.py
%{hyperkitty_basedir}/settings.py
%{hyperkitty_basedir}/settings_local.py
%{hyperkitty_basedir}/urls.py
%{hyperkitty_basedir}/wsgi.py

%dir %{hyperkitty_basedir}/static
%{hyperkitty_basedir}/static/admin
%{hyperkitty_basedir}/static/debug_toolbar
%{hyperkitty_basedir}/static/django-mailman3
%{hyperkitty_basedir}/static/django_extensions
%{hyperkitty_basedir}/static/facebook
%{hyperkitty_basedir}/static/hyperkitty
%{hyperkitty_basedir}/static/rest_framework

# The wsgi needs to write to static/CACHE
%attr(755,hyperkitty,hyperkitty) %dir %{hyperkitty_basedir}/static/CACHE
%attr(644,hyperkitty,hyperkitty) %{hyperkitty_basedir}/static/CACHE/manifest.json

%attr(755,hyperkitty,hyperkitty) %dir %{hyperkitty_basedir}/static/CACHE/css
%attr(644,hyperkitty,hyperkitty) %{hyperkitty_basedir}/static/CACHE/css/output.*.css

%attr(755,hyperkitty,hyperkitty) %dir %{hyperkitty_basedir}/static/CACHE/js
%attr(644,hyperkitty,hyperkitty) %{hyperkitty_basedir}/static/CACHE/js/output.*.js

%dir %{hyperkitty_localedir}

%attr(750,root,hyperkitty) %dir %{hyperkitty_etcdir}
%attr(640,root,hyperkitty) %config(noreplace) %{hyperkitty_etcdir}/settings_local.py
%attr(750,root,hyperkitty) %dir %{hyperkitty_libdir}
%attr(750,hyperkitty,hyperkitty) %dir %{hyperkitty_datadir}
%attr(770,hyperkitty,hyperkitty) %dir %{hyperkitty_logdir}

%files -n %{hyperkitty_pkgname}-web-uwsgi
%dir %{_sysconfdir}/uwsgi
%dir %{_sysconfdir}/uwsgi/vassals
%config (noreplace) %{_sysconfdir}/uwsgi/vassals/hyperkitty.ini

%changelog
